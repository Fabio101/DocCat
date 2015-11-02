from django.shortcuts import render
from .forms import CatalogueForm

# Create your views here.

def home(request):
	
	#context variables
	title = "Document Catalogues"
	submit_label = "Add Catalogue"
	form = CatalogueForm(request.POST or None)

	context = {
                "title": title,
		"submit_label": submit_label,
                "form": form,
        }

	if form.is_valid():
		formData = form.save(commit=False)
		formData.save()

		context = {
			"title": "Thank you",
			"submit_label": "Add Another Catalogue"
		}

	return render(request, "catalogue/home.html", context)
