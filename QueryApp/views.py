from django.db.models import Count, Min, Max, Sum, Avg
from django.utils.timezone import utc
import datetime
from datetime import timedelta, datetime, date
from django.db.models import F
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Blog, Author, Entry, ThemeBlog, Poll, Choice
# Create your views here.

	

def handler404(request, *args, **kwargs):
	return render(request, '404.html')

def handler500(request, *args, **kwargs):
	return render(request, '500.html')





def index(request):
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
	# related_name = Blog.objects.get(id=13)
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

	max1_comment = Blog.objects.annotate(max1_comment1_blog=Max('entries__number_of_comments')).filter(max1_comment1_blog__isnull=False).order_by('-max1_comment1_blog')
	print("Max1_comment", max1_comment)
	for maxcomment in max1_comment:
		print("sorted-by", maxcomment, maxcomment.max1_comment1_blog)

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
		# 'qs':qs,
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




