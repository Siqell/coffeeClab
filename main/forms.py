from django import forms
from .models import review

class add_review(forms.ModelForm):
	class Meta:
		model = review
		fields = ['username_client', 'review']
	def __init__(self, *args, **kwargs):
		super(add_review, self).__init__(*args, **kwargs)

