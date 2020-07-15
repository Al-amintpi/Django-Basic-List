from django.shortcuts import render,redirect

#---------------------------------------------
from django.contrib.auth import logout, login, authenticate
def get_login_view(request):	
	if request.method == "POST":
		user = request.POST.get('user')
		password = request.POST.get('pass')
		auth = authenticate(username=user, password=password)
		if auth:
			login(request, auth)
			return redirect("login") 
	return render(request, "accounts/login.html")


def get_logout_view(request):
	logout(request)
	return redirect('login')


from .forms import registerUserForm
def get_register_view(request):
	form = registerUserForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()

	context = {
		'form':form
	}
	return render(request, "accounts/register.html", context)	



