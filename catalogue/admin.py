from django.contrib import admin

# Register your models here.
from .models import Catalogue
from .forms import CatalogueForm

class CatalogueAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "date_added", "date_modified", "id"]
	form = CatalogueForm
	#class Meta:
	#	model = Catalogue

admin.site.register(Catalogue, CatalogueAdmin)
