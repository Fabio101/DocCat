from django import forms

from .models import Document

class AddDocumentForm(forms.ModelForm):
        class Meta:
                model = Document
                fields = ['name', 'catalogue', 'description', 'document']
