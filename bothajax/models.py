from django.db import models
from django.contrib.auth.models import User

class ForgetPasswordRequest(models.Model):
	user 		= models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	token 		= models.CharField(max_length=50)
	status 		= models.BooleanField(default=True)
	create_by   = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.user.username
