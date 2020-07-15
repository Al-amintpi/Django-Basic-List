from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse, get_object_or_404
from .forms import registerUserForm
from django.http import JsonResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from bothajax.models import ForgetPasswordRequest
from django.contrib.auth.password_validation import validate_password
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail


def get_login_view(request):
	if request.user.is_authenticated:
		return HttpResponse('User authenticated')
	else:		
		if request.method == "POST":
			user = request.POST.get('user')
			password = request.POST.get('pass')
			print(user)
			auth = authenticate(username=user, password=password)
			if auth:
				login(request, auth)
				return JsonResponse({'status': 'ok'})
			else:
				return JsonResponse({'status':'failed'})

	return render(request, "bothajax/login.html")



def get_logout_view(request):
	logout(request)
	return redirect('both_login')



def get_register_view(request):
	form = registerUserForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			instance = form.save()
			return JsonResponse({'msg':'success'})
		else:
			return JsonResponse({"error": "failed"})


	context = {
		'form':form
	}
	return render(request, "bothajax/register.html", context)


import random as r
def forget_password_view(request):
	if request.user.is_authenticated:
		return HttpResponse('you still login not password forget')
	else:	
		if request.method == 'POST':
			email = request.POST['email']
			if User.objects.filter(email=email).exists():
				user = get_object_or_404(User, email=email)

				token = r.randint(0,9999)
				print(type(token))

				create = ForgetPasswordRequest.objects.create(user=user, token = token)
				#------Send Email------------------------
				domain = get_current_site(request)
				mail_subject = "Confirmation Messages"
				message = render_to_string('bothajax/account/confirm_email.html',{
					'user':user,
					'domain':domain,
					'uid':user.id,
					"token": token, 
					})
				to_email = [email] # instance.email
				to_email = str(to_email[0])
				from_email = settings.EMAIL_HOST_USER
				send_mail(mail_subject, message, from_email, [to_email,], fail_silently=True)
				return JsonResponse({ "status": "success" });
			else:
				return JsonResponse({"status": "failed"});	
	return render(request, 'bothajax/account/forget_password.html')


def update_forget_password_view(request, username, token):
	user = get_object_or_404(User, username=username, is_active=True)
	req_obj = get_object_or_404(ForgetPasswordRequest, user=user, token=token, status=True)
	
	print(req_obj.user)
	print(req_obj.token)
	if request.method == 'POST':
		pass1 = request.POST['pass1']
		pass2 = request.POST['pass2']
		print(type(pass1))
		print(type(pass2))

		if pass1 != pass2:
			print('password do not match')
		else:
			user.set_password(pass1)
			req_obj.status=False 
			user.save()
			req_obj.save()
			return JsonResponse({'status':'success'});
		return JsonResponse({'status':'failed'})

	context = {
	 'req_obj':req_obj
	}	
	return render(request, 'bothajax/account/forget_password_form.html', context)


def password_reset_view(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			pass1 = request.POST['pass1']
			pass2 = request.POST['pass2']

			if pass1 == pass2:
				request.user.set_password(pass1)
				request.user.save()
				return JsonResponse({'status':'success'})
				 
			else:
				return JsonResponse({'status':'failed'})
				
	else:
		return redirect('both_login')
	return render(request, 'bothajax/account/password_reset.html')	

