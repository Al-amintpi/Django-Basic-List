from django import forms
from ProjectApp.models import Article

class UpdatedForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = [
             'content',
		]
class CreateForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = [
		   'content'
		]		