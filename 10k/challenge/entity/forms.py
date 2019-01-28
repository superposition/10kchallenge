from django import forms
from .models import Entity

class PostForm(forms.ModelForm):
	class Meta:
		model = Entity
		fields = ('symbol',)