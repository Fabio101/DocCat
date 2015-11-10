from django.shortcuts import render
from .forms import AddCatalogueForm

# Create your views here.

def add(request):
	if request.user.is_authenticated():

		#context variables
		form = AddCatalogueForm(request.POST or None)
		title = "Add Catalogue"
		title_content1 = "This area allows you to add new catalogues to your account."
		title_content2 = "There is no limit to the number of Catalogues one can create."

		context = {
                	"title": title,
			"title_content1": title_content1,
			"title_content2": title_content2,
			"button": "Add",
                	"form": form,
        	}

		if form.is_valid():
			try:
				#Save form data
				form.save()

				#Set new context
				title_content2 = "You can continue to add more Catalogues."

				context = {
					"title": title,
					"title_content2" : title_content2,
					"status": '<div class="alert alert-success" role="alert">Successfully Added Catalogue!</div>',
					"button": "Add More",
				}
			
			except Exception, e:
				#Display expection in new context
				title_content2 = "It appears that something has gone wrong. Please try again."
				context = {
                                	"title": title,
					"title_content2" : title_content2,
					"status": '<div class="alert alert-danger" role="alert">Failure: ' + str(e) + '</div>',
                                	"button": "Try Again",
					"form": form,
                        	}

		return render(request, "catalogue/add.html", context)
	else:
		return render(request, "unauthorized.html", {})
