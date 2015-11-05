from django.contrib import admin

# Register your models here.

from .models import Document
from .forms import AddDocumentForm

class DocumentAdmin(admin.ModelAdmin):
        list_display = ["__unicode__", "catalogue", "document", "date_added", "date_modified", "id"]
        form = AddDocumentForm

admin.site.register(Document, DocumentAdmin)
