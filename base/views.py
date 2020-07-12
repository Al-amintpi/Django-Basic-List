from django.shortcuts import render
from base.models import Post
# Create your views here.
from django.utils.translation import gettext as _

def home(request): 
	posts = Post.objects.all().order_by('name')
	title = _('Home')
	context={
    'posts':posts,
    'title':title
    }
	return render(request, 'translate.html', context)