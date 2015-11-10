from django import forms

from .models import Document
from catalogue.models import Catalogue

class AddDocumentForm(forms.ModelForm):
        class Meta:
                model = Document
                fields = ['name', 'catalogue', 'description', 'document']

	#To sort the Catalogue list 
	def __init__(self, *args, **kwargs):
		super(AddDocumentForm, self).__init__(*args, **kwargs)
		self.fields['catalogue'] = forms.ModelChoiceField(queryset=Catalogue.objects.all().order_by('name'))

class ListDocumentForm(forms.Form):
	Catalogue = forms.ModelChoiceField(queryset=Catalogue.objects.all().order_by('name'))
