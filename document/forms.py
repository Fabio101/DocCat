from django import forms

from .models import Document
from catalogue.models import Catalogue
from django.contrib.auth.models import Group, User

class AddDocumentForm(forms.ModelForm):
        class Meta:
                model = Document
                fields = ['name', 'catalogue', 'description', 'document']

	#To sort the Catalogue list and only show allowed catalogues by group
	def __init__(self, *args, **kwargs):
		usergroup = kwargs.pop('userGroup')

		super(AddDocumentForm, self).__init__(*args, **kwargs)
		self.fields['catalogue'] = forms.ModelChoiceField(queryset=Catalogue.objects.filter(group_id = usergroup).order_by('name'))

class ListDocumentForm(forms.Form):
	#We need to override the constructor for this form sothat we can pass the group ID for its queryset
	catalogues = forms.ChoiceField()

	def __init__(self, *args, **kwargs):
		usergroup = kwargs.pop('userGroup')

		super(ListDocumentForm, self).__init__(*args, **kwargs)
		self.fields['catalogues'] = forms.ModelChoiceField(queryset=Catalogue.objects.filter(group_id = usergroup).order_by('name'), empty_label=None)
