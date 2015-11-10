from django import forms

from .models import Document
from catalogue.models import Catalogue

class AddDocumentForm(forms.ModelForm):
        class Meta:
                model = Document
                fields = ['name', 'catalogue', 'description', 'document']

class ListDocumentForm(forms.Form):
	Catalogue = forms.ModelChoiceField(queryset=Catalogue.objects.all().order_by('name'))
