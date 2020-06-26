from django.db import models
from django.core.exceptions import ValidationError




# Create your models here.
class Photo(models.Model):
    file = models.ImageField()
    
    def clean(self):
        if len(self.file) > 1048576:
            raise ValidationError("This image maximum size 1mb")
        else:
            print('fine')    

    



class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name



class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='entries')
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateField(null=True)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(blank=True, null=True)
    number_of_pingbacks = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    

    def __str__(self):
        return self.headline

class ThemeBlog(Blog):
    theme = models.CharField(max_length=30)        

class ExampleBlog(models.Model): 
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name   




#-------------------------Django Geolocation--------------------
from geoposition.fields import GeopositionField

class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField() 

          

#----------------------django simple history------------------------


from simple_history.models import HistoricalRecords
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    history = HistoricalRecords()
    def __str__(self):
        return str(self.question)

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    history = HistoricalRecords()

    def __str__(self):
        return self.choice_text 


