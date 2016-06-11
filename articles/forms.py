from django import forms
from functools import partial
from .models import Post, User

class DateInput(forms.DateInput):
	input_type = 'date'
	
class PostForm(forms.ModelForm):
	user = forms.ModelChoiceField(queryset=User.objects.all())

	class Meta:
		model = Post
		fields = ('title','lead', 'text','user','tag','published_date','created_date')
		widgets = {'published_date': DateInput(),'created_date': DateInput(),}

		
class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('name','nickname','mail')
		
