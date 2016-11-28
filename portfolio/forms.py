from django import forms
from .models import *

class ProjectForm(forms.ModelForm):
	class Meta:
		model=Project
		fields=('title','text',)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('author','text',)
	
		