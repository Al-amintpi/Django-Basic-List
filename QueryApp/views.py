from django.db.models import Count, Min, Max, Sum, Avg
from django.utils.timezone import utc
import datetime
from datetime import timedelta, datetime, date
from django.db.models import F
from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Blog, Author, Entry, ThemeBlog, Poll, Choice, Photo
from .forms import PhotoForm
from .forms import PersonForm
# Create your views here.

#django import and export
from django.http import HttpResponse, JsonResponse
from .resources import PersonResource
from .models import Person

from tablib import Dataset

import csv
import requests



#django django pdf response (file download and preview in browser both option)
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

def download_view(request):
    person = Person.objects.all()
    html_string = render_to_string('pdf_template.html', {"person":person})

    html = HTML(string=html_string)
    html.write_pdf(target='templates/mypdf.pdf');

    fs = FileSystemStorage('templates')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

    return response

def preview_view(request):
	person = Person.objects.all()
	html_string = render_to_string('pdf_template.html', {"person":person})

	html = HTML(string=html_string)
	html.write_pdf(target='templates/mypdf.pdf');

	fs = FileSystemStorage('templates')
	with fs.open('mypdf.pdf') as pdf:
	    response = HttpResponse(pdf, content_type='application/pdf')
	    response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'
	    return response

	return response

def pdf(request):
	return render(request, 'pdf.html') 


#Manually export and import
def export1(request):
	model_class=Person
	meta = model_class._meta
	field_names = [field.name for field in meta.fields]
	
	with open('templates/export.csv', 'w')as f:
		writer = csv.writer(f)

		writer.writerow(field_names)
		for obj in model_class.objects.all():
			row = writer.writerow([getattr(obj, field) for field in field_names])
			

	return redirect('import_export')

def import1(request):
	person = Person.objects.all()
	with open('templates/persons.csv', 'r')as f:
		read = csv.reader(f)
		objs = [
			Person(
				name=i[0],
				email=i[1],
				location=i[2]
			)
			for i in read
		]

		persons = Person.objects.bulk_create(objs)
			
	return redirect('import_export')


def import_export(request):
	person = Person.objects.all()
	return render(request, 'import_export.html', {'person':person})
 	
#Package import and export

def importpackage(request):
	person = Person.objects.all()
	print(person)
	if request.method == 'POST':
	    person_resource = PersonResource()
	    dataset = Dataset()
	    new_persons = request.FILES['myfile']

	    imported_data = dataset.load(new_persons.read().decode('utf-8'),format='csv')
	    result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

	    if not result.has_errors():
	        person_resource.import_data(dataset, dry_run=False)  # Actually import now

	return render(request, 'import.html', {"person":person})


def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    # response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    # response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    # response = HttpResponse(dataset.json, content_type='application/json')
    # response['Content-Disposition'] = 'attachment; filename="persons.json"'
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return response


def get_request(request):
	response = requests.get('https://httpbin.org/get', params={"page":2, "count":2})
	print(response.json())
	print('Http response code', response.status_code)
	


	# with open('templates/csv.txt', 'w')as f:
	# 	field = ['serialnumber', 'name', 'email']
	# 	write = csv.DictWriter(f, fieldnames=field)
	# 	write.writeheader()
	# 	write.writerow({'serialnumber':'2', 'name':'alamin2', 'email':'alamin@gmail.com'})	

	# response = requests.get('https://cdn.pixabay.com/photo/2013/07/02/22/20/roses-142876_960_720.jpg')
	# payload = {'page':2, 'count':5 }
	# response = requests.get('https://httpbin.org/get', params={'page':2, 'count':5})
	# r = requests.get('http://127.0.0.1:8000/')
	# with open('templates/text.png', 'wb')as f:
	# 	f.write(response.content)
	# print(response.status_code)
	# print(response.headers)
	# print(response.ok)

	# print(response.text)
	# print(response.url)
	# r = requests.get('https://vaid.tech/en/')
	# print(r.cookies)
	# print(r.headers['Content-Type'])
	# print(r.json())
	# print(r.status_code)
	# print(r.encoding)
     #------------------POST-----------
	# response = requests.post('https://en.wikipedia.org/wiki/Nanotechnology')
	# response.raise_for_status()
	# with open('templates/Nanotechnology.html', 'wb')as f:
	# 	f.write(response.content)

	# url = 'https://httpbin.org/set/cookies/headers'
	# headers = {'user-agent': 'your-own-user-agent/0.0.1'}
	# cookies = {'visit-month': 'March'}
	# req = requests.get(url, headers=headers, cookies=cookies)
	# print(req)
	#return HttpResponse('Http request is :'+ request.method)
	return HttpResponse("abcd")






def get_photo(request):
	photos = Photo.objects.all()
	if request.method == 'POST':
		form = PhotoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('photo')
	else:
		form = PhotoForm()
	context = {
	   "form":form,
	   "photos":photos
	}	
	return render(request, 'fileupload.html', context)
	
	

def handler404(request, *args, **kwargs):
	return render(request, '404.html')

def handler500(request, *args, **kwargs):
	return render(request, '500.html')




from django.contrib.auth.decorators import login_required

def index(request):
	blog = Blog.objects.all()
	# blog = Blog.object.all()[:5] #Limiting QuerySets ,[5:10]
	# blog = Blog.objects.filter(name="new")
	# entry = Entry.objects.filter(pub_date__year=2020)
	# entry = Entry.objects.filter(headline__startswith='alamin').filter(pub_date__gte=datetime.date(2020,1,1)).exclude(pub_date__gt=datetime.date.today())
	#blog = Entry.objects.order_by('-id')
	# blog = Blog.objects.get(id__exact=7)
	# obj = Blog.objects.filter(entry__headline__contains="alamin1")
	# qs = Blog.objects.filter(entry__authors__name="Alamin")
	# print(qs)
	# nullqs = Blog.objects.filter(entry__authors__name__isnull=True)
	# nullqs1 = Blog.objects.filter(entry__blog__isnull=True)
	# spaningqs = Blog.objects.filter(entry__headline__contains='alamin', entry__pub_date__year=2020) #jodi headline alamin r pub_date=2020 hoi tahle shudhu return korba
	# spaningqs = Blog.objects.filter(entry__headline__contains='alamin').filter(entry__pub_date__year=2020) # aite jodi pub_date 2020 theke r 2020 year headline kon alamin na theke toba o return korba
	# Fqs = Entry.objects.filter(number_of_comments__gt=F('number_of_pingbacks'))
	# Fmulti = Entry.objects.filter(number_of_comments__gt=F('number_of_pingbacks')*2)
	# Fadd   = Entry.objects.filter(rating__lt=F('number_of_comments')+F('number_of_pingbacks'))
	# Fsub   = Entry.objects.filter(number_of_comments__gte=F('number_of_pingbacks')-1)
	#Fspan   = Entry.objects.filter(authors__name=F('blog__name'))
	#delta  = Entry.objects.filter(mod_date__gt=F('pub_date')+timedelta(days=3))
	#pk = Blog.objects.filter(id__in=[14,10])
	#pk = Blog.objects.filter(id__gt=4)
	#Complex lookups with Q objects
	#comqs = Entry.objects.filter(Q(headline__startswith="new headline")|Q(headline__startswith="what"))
	#comqs = Entry.objects.filter(Q(headline__startswith='new headline')&Q(pub_date__gt=datetime.date(2019,1,1)))
	#comqs = Entry.objects.filter(Q(headline__startswith='gfghhg') | ~Q(mod_date__year=2021))
	#comqs = Entry.objects.get(Q(pub_date__lt=datetime.date(2019,1,1))|Q(pub_date__gt=datetime.date(2020,1,1)), headline__startswith='new')
	#delete = Entry.objects.filter(pub_date__year=2020).delete()
	#Copying model instances
	# cmi = Blog(name="Alamin", tagline="new tagline")
	# cmi.save()
	# cmi.pk = None 
	# cmi.save()

	# cmi_django_blog = ThemeBlog(name="alamin", tagline="newtagline", theme="new theme text")
	# cmi_django_blog.save()
	# cmi_django_blog.pk = None
	# cmi_django_blog.save()

	# entry = Entry.objects.all()[0]
	# old_author = entry.authors.all()
	# entry.pk = None
	# entry.save()
	# entry.authors.set(old_author)
	#u = Entry.objects.filter(pub_date__year=2020).update(headline="new headline ")
	# b = Blog.objects.get(pk=13)
	# entry = Entry.objects.all().update(blog=b)
	# print(entry)

	# name = Blog.objects.get(id=13)
	# entry = Entry.objects.get(id=6)
	# entry.blog = name
	# entry.save()
	# select = Entry.objects.select_related('blog').get(id=6)
	# print(select.blog)
	#.............................Foreignkey relation........................................
	# back = Blog.objects.get(id=13)
	# setback = back.entry_set.all()
	# print(setback)
	# single = Blog.objects.get(id=13)
	# qs = single.entry_set.filter(headline__contains='new headline')
	# print(single.entry_set.count())
	# related_name = Blog.objects.get(id=18)
	# qs = related_name.entries.all()
	# print(qs)

	#----------------------------django aggregate----------------------
	# maximum = Entry.objects.aggregate(maximum=Max('number_of_comments'))
	# print(maximum)
	# Minumum=Entry.objects.aggregate(Minimum=Min('number_of_comments'))
	# print(Minumum)
	# total_add = Entry.objects.aggregate(Sum=Sum('number_of_comments'))
	# print(total_add)
	# averge = Entry.objects.aggregate(averge=Avg('number_of_comments'))
	# print(averge)
	#--------------------------------------django annotate------------

	# count = Blog.objects.count()
	# choice_blog = Blog.objects.annotate(choice_count=Count('entries'))
	# print(choice_blog)
	# print(choice_blog.count())
	# print(choice_blog[1].choice_count)
	# for i in choice_blog:
	# 	print(" choice ", i, i.choice_count)
	# filtering = Blog.objects.filter(tagline="nice_to_meet_you1").annotate(filtering_choice=Count('entries'))
	# print(filtering)
	# print(filtering[0].filtering_choice)

	# sum_per_comment = Blog.objects.annotate(number_per_comment=Sum('entries__number_of_comments'))
	# print(sum_per_comment)
	# print(sum_per_comment[0].number_per_comment)

	# max_comment = Blog.objects.annotate(max_comment_blog=Sum('entries__number_of_comments')).filter(max_comment_blog__isnull=False).order_by('-max_comment_blog')[0]
	# print(max_comment)
	# min_comment = Blog.objects.annotate(min_comment_blog=Sum('entries__number_of_comments')).filter(min_comment_blog__isnull=False).order_by('min_comment_blog')[0]
	# print(min_comment)

	# max1_comment = Blog.objects.annotate(max1_comment1_blog=Max('entries__number_of_comments')).filter(max1_comment1_blog__isnull=False).order_by('-max1_comment1_blog')
	# print("Max1_comment", max1_comment)
	# for maxcomment in max1_comment:
	# 	print("sorted-by", maxcomment, maxcomment.max1_comment1_blog)

	#Django queryset api dates

	#print(entry)
	#entry1 = Entry.objects.none()
	#print(entry1)

	#entry = Entry.objects.filter(pub_date__week__gte=23)
	#entry = Entry.objects.filter(pub_date__week_day__gte=3)
	#entry = Entry.objects.filter(pub_date__hour=14) #probleam
	#Entry.objects.filter(pub_date__time__range=(datetime.time(8), datetime.time(17)))#probleam
	#entry = Entry.objects.filter(pub_date__timestamp__hour=23)
	context = {
	    "blog":blog,
		#'qs':qs,
		# 'u':u,
		# 'comqs':comqs,
		# 'pk':pk,
		# 'delta':delta,
		# 'Fspan':Fspan,
		# 'Fsub':Fsub,
		# 'Fadd':Fadd,
		# 'Fmulti':Fmulti,
		# 'Fqs':Fqs,
		# 'spaningqs':spaningqs,
		# 'nullqs1':nullqs1,
		# 'nullqs':nullqs,
		# 'qs':qs,
		# 'obj':obj,
		# 'blog':blog,
		# 'entry':entry,
		# 'pk':pk,
		# 'cmi':cmi,
	}
	return render(request, 'QueryApp/home.html', context)


#ai view ta json datagula ke just show korei template te
def get_objects_temp_show(request):	
	person = Person.objects.all()

	return render(request, 'QueryApp/person.html', {'person':person})


# ai view theke get kore json format te object gula ke show korano hossche
def get_object_json_format(request):
	queryset = list(Person.objects.values_list('id', 'name', 'email', 'location','file'))
	print(queryset)
	return JsonResponse(queryset,safe=False)

import json
from django.db.models.fields.files import FileField
from django.core.serializers.json import DjangoJSONEncoder

#a view ea POST o UPDATE kora hossche
def get_post_or_update(request):
	obj_id = request.POST.get('obj_id', None)
	name = request.POST.get('name', None)
	email = request.POST.get('email', None)
	location = request.POST.get('location', None)
	file = request.FILES.get('file')
	

	print(file)

	if obj_id:
		person_obj = get_object_or_404(Person, id=obj_id)
		person_obj.name=name
		person_obj.email=email
		person_obj.location = location
		person_obj.file = file
		person_obj.save()
		print(person_obj.name)
		print(person_obj.email)
		print(person_obj.location)
		print(person_obj.file)
		

	else:
		person_obj=Person.objects.create(name=name, email=email, location=location, file=file)
		

	instance={"id": person_obj.id, "name": person_obj.name, "email": person_obj.email, "location": person_obj.location, "file":str(person_obj.file.url)}
	
	return JsonResponse(instance, safe=False)



#a view objects gula ke single vabe JsonResponse kore hossche update somoi a function ke call kore hoba...
def get_single_object(request, id):
	person_obj = get_object_or_404(Person, id=id)
	return JsonResponse({'id':person_obj.id, 'name':person_obj.name, 'email': person_obj.email, 'location': person_obj.location}, safe=False)


#a view ta objects gula ke delete kora hossche
def get_delete_view(request, id):
	person_obj_delete = get_object_or_404(Person, id=id)
	person_obj_delete.delete()
	return redirect('home')

			