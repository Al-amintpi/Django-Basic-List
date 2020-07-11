from django.shortcuts import render,HttpResponse

def get_drf_view(request):
	return render(request, 'drf/home_drf.html')
