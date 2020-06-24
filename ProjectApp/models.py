from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


class AdminArticlecreate(models.Manager):
	def get_admin_post(self, username):
		return self.filter(created_by__username=username)

class Article(models.Model):
	created_by     = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
	content        = models.TextField()
	created_date   = models.DateTimeField(auto_now=False,auto_now_add=True)
	admin_object   = AdminArticlecreate()

	def __str__(self):
		return str(self.created_by)


# class EmployeeQueryset(models.QuerySet):

# 	def objectactive(self):
# 		return self.filter(active=True)

# 	def juniors(self):
# 		return self.filter(role='J')	

# 	def seniors(self):
# 		return self.filter(role='S')

	
# class EmployeeManager(models.Manager):
# 	def get_queryset(self):
# 		return EmployeeQueryset(self.model, using=self._db)

# 	def objectactive(self):
# 		return self.get_queryset().objectactive()

# 	def juniors(self):
# 		return self.get_queryset().juniors()

# 	def seniors(self):
# 		return self.get_queryset().seniors()		


class EmployeeManager(models.Manager):
	def get_queryset(self):
		return super(EmployeeManager, self).get_queryset().filter(active=True)

class SeniorManager(models.Manager):
	def get_queryset(self):
		return super(SeniorManager, self).get_queryset().filter(role="S").count()

class JuniorManager(models.Manager):
	def get_queryset(self):
		return super(JuniorManager, self).get_queryset().filter(role="J")

class Employeetitle(models.Manager):
	def get_title_count(self, title):
		return self.filter(title__icontains=title).count()

class Employeename(models.Manager):
	def get_employeename(self, firstname):
		return self.filter(first_name=firstname)

class Employee(models.Model):
      gender_choices = (
           ("M", "Male"),
           ("F", "Female")
      )
      roles_choices = (
           ("J", "Junior"),
           ("S", "Senior"),
      )
      first_name = models.CharField(max_length=200)
      last_name = models.CharField(max_length=200)
      email = models.CharField(max_length=250)
      gender = models.CharField(max_length=1, choices=gender_choices)
      role = models.CharField(max_length=120, choices=roles_choices, default="J")
      active = models.BooleanField(default=True)
      title = models.CharField(max_length=100)
      # custom manager replaces objects manger
      objects = Employeetitle()

      active_objects = EmployeeManager() # The EmployeeManager manager.

      senior_objects = SeniorManager() # The SeniorManager

      junior_objects = JuniorManager() #The JuniorManager

      employee = Employeename() 

      def __str__(self):
            return str(self.first_name) + str(self.last_name)		



