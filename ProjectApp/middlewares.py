# import requests
# from django.http import HttpResponse
# from django.conf import settings
# from django.utils.deprecation import MiddlewareMixin

# class StackOverflowMiddleware(MiddlewareMixin):
# 	def __init__(self, get_response):
# 		self.get_response = get_response

# 	def __call__(self, request):
# 		return self.get_response(request)
#
# 	def process_request(self, request):
# 		if request.user.is_authenticated:
# 			print('newww')
# 		else:
# 			pass	
    
# 	def process_response(self, request, response): 
# 		pass

#step2 settings.py
#'ProjectApp.middlewares.StackOverflowMiddleware',
