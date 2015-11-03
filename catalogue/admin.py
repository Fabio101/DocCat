from django.contrib import admin

# Register your models here.
from .models import Catalogue
from .forms import AddCatalogueForm

class CatalogueAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "date_added", "date_modified", "id"]
	form = AddCatalogueForm

admin.site.register(Catalogue, CatalogueAdmin)
