from django.core.management.base import BaseCommand
from QueryApp.models import Entry

#print(datetime.now())

def datetime():
	from datetime import datetime
	entry = Entry.objects.all()
	for i in entry:
		i.mod_date = datetime.now()
		i.save()

class Command(BaseCommand):
    def handle(self,*args, **kwargs):
        pass