from django.db import models

# Create your models here.
class Post(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	date  = models.DateField(blank=True, null=True)

	def __str__(self):
		return self.name