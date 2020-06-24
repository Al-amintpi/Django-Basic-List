from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from ProjectApp.models import Article, Employee
#from ProjectApp.decorators import user_is_entry_author
from django.contrib.auth.decorators import login_required
from ProjectApp.decorators import staff_required, superuser_required
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from ProjectApp.forms import UpdatedForm,CreateForm



def get_manager(request):
	total_employee = Employee.active_objects.all()
	total_senior_employee = Employee.senior_objects.all()
	total_junior_employee = Employee.junior_objects.all()
	title_count = Employee.objects.get_title_count(title="al")
	employee = Employee.employee.get_employeename(firstname="Al-amin")
	print(title_count)
	article = Article.admin_object.get_admin_post(username='Test')
	print(article)
	context = {
	   'total_employee':total_employee,
	   'total_senior_employee':total_senior_employee,
	   'total_junior_employee':total_junior_employee,
	   'title_count':title_count,
	   'employee':employee,
	   'article':article

	}
	return render(request, "manager/manager.html", context)








class ArticleobjectMixin(object):
	model = Article

	def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj  = get_object_or_404(self.model, id=id)
			print('model-obj', obj)
		return obj


class ArticleHomeView(ListView):
	model = Article

class PostDetailsView(DetailView):
	model = Article
	template_name = 'ProjectApp/detailsview.html'	
	
class UpdateView(UpdateView):
	model = Article
	template_name = 'ProjectApp/update.html'
	fields = [ 
        "content",
    ] 
	success_url ="/"


class ArticleCreateView(CreateView):
	model = Article
	template_name = 'ProjectApp/create.html'
	fields = [
		"content"
	]

	success_url = "/"

class ArticledeleteView(ArticleobjectMixin, View):
	template = 'mixin/delete.html'
	def get(self, request, id=None, *args, **kwargs):
        # GET method
		context = {}
		obj = self.get_object()
		print(" object title ",obj)
		if obj is not None:
			context['object'] = obj
		return render(request, self.template, context)

	
	def post(self, request, id=None,*args, **kwargs):
		#Post REQUEST
		context = {}
		obj = self.get_object()
		if obj is not None:
			obj.delete()
			context['object'] = None

			
		return render(request, self.template, context)


class ArticleupdateView(ArticleobjectMixin, View):
	template = 'mixin/update.html'

	def get(self, request, id=None, *args, **kwargs):
        # GET method
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = UpdatedForm(instance=obj)
			context['object'] = obj
			context['form'] = form
		return render(request, self.template, context)

	def post(self, request, id=None,  *args, **kwargs):
        # POST method
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = UpdatedForm(request.POST, instance=obj)
			if form.is_valid():
				form.save()
			context['object'] = obj
			context['form'] = form
		return render(request, self.template, context)

#decorators code................
@login_required
@staff_required(login_url='/', redirect_field_name='', message='You are not authorised to view this page.')
def staff_required_action(request, id):
	create = get_object_or_404(Article, id=id)
	context = {
		'create':create
		}
	return render(request, 'index.html', context)


@login_required(login_url='/login', redirect_field_name='')
@superuser_required(login_url='/', redirect_field_name='', message='You are not authorised to perform this action.')
def superuser_required_action(request):
    return render(request, 'about.html')

#@user_is_entry_author
# def get_index(request, id):
# 	create = get_object_or_404(Article,id=id)
# 	context = {
# 	  'create':create
# 	}
# 	return render(request, 'index.html', context)