from django.shortcuts import render
from .forms import CatalogueForm

# Create your views here.

def add(request):
	
	#context variables
	title = "Add Catalogue"
	submit_label = "Add"
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
			"submit_label": "Add More"
		}

	return render(request, "catalogue/add.html", context)
