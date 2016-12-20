from django import forms
from login.models import logins

class PostForm(forms.ModelForm):
	class Meta:
		model = logins
		fields=[
          "title",
          "password",
		]