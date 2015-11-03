from django.shortcuts import render
from .forms import AddCatalogueForm

# Create your views here.

def add(request):
	#context variables
	form = AddCatalogueForm(request.POST or None)

	context = {
                "title": "Add Catalogue",
		"submit_label": "Add",
                "form": form,
        }

	if form.is_valid():
		try:
			#Save form data
			form.save()

			#Set new context
			context = {
				"title": "Catalogue Created",
				"submit_label": "Add More",
			}

		except Exception, e:
			#Display expection in new context
			context = {
                                "title": "Error",
				"error": str(e),
                                "submit_label": "Try Again",
                        }

	return render(request, "catalogue/add.html", context)
