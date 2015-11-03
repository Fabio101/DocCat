from django import forms

from .models import Catalogue

class AddCatalogueForm(forms.ModelForm):
	class Meta:
		model = Catalogue
		fields = ['name', 'description']
