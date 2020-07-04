from django.test import TestCase
from QueryApp.models import Author, Entry,Blog, Person

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

from django.test import Client
from django.urls import reverse
class ViewTest(TestCase):
	def setUp(self):
		self.client = Client()
		

	def test_blog_get(self):
		response = self.client.get('/home_page/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'QueryApp/home.html')




class EntryTest(TestCase):
	
	def setUp(self):
		self.blog = Blog.objects.create(name="alamin", tagline="nice to meet you", active='False')
		self.blog.save()
        
		
		from django.utils import timezone
		self.entry = Entry.objects.create(blog=self.blog,headline="headline1",body_text="new body",
		    pub_date=timezone.now(),
		    mod_date=timezone.now()

		     )
		self.entry.save()

	def test_read_task(self):
		self.assertEqual(self.entry.headline, "headline1")	



		






