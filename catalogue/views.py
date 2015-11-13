from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .models import Catalogue
from document.models import Document
from .forms import AddCatalogueForm

# Create your views here.

def add(request):
	if request.user.is_authenticated():

		if request.GET and 'catalogueID' in request.GET:
                	catalogueID = request.GET.get('catalogueID')
			catalogue = Catalogue.objects.get(id = catalogueID)
			
			form = AddCatalogueForm(request.POST or None, initial={'name': catalogue.name, 'description': catalogue.description}, instance=catalogue)
			title = "Edit Catalogue"
			button = "Edit"
			status = "Modified"
		else:
			form = AddCatalogueForm(request.POST or None)
			title = "Add Catalogue"
			button = "Add"
			status = "Added"

		#context
		title_content1 = "This area allows you to add new catalogues to your account."
		title_content2 = "There is no limit to the number of Catalogues one can create."

		context = {
                	"title": title,
			"title_content1": title_content1,
			"title_content2": title_content2,
			"button": button,
                	"form": form,
        	}

		if form.is_valid():
			try:
				#Save form data
				form.save()

				#Set new context
				title_content2 = "You can continue to " + button + " more Catalogues."

				context = {
					"title": title,
					"title_content2" : title_content2,
					"status": '<div class="alert alert-success" role="alert">Successfully ' + status + ' Catalogue!</div>',
					"button": button + " More",
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

def delete(request):
	if request.user.is_authenticated():

		if request.GET and 'catalogueID' in request.GET:
			catalogueID = request.GET.get('catalogueID')
			document = Document.objects.filter(catalogue = catalogueID).delete()
                        catalogue = Catalogue.objects.filter(id = catalogueID).delete()
			
			return redirect('catalogue.views.CatList')
        else:
                return render(request, "unauthorized.html", {})

def CatList(request):
        if request.user.is_authenticated():

                relatedCats = Catalogue.objects.all().order_by('name')

                #Setup Pagination
                paginator = Paginator(relatedCats, 6)

                #Check if a page number exists, if not set to page 1
                try:
                        page = int(request.GET.get('page', '1'))
                except:
                        page = 1

                #If page is empty or invalid, return to last page
                try:
                        catList = paginator.page(page)
                except(EmptyPage, InvalidPage):
                        catList = paginator.page(paginator.num_pages)

                title = "Catalogues"
                title_content1 = "This area allows you to view your catalogues."
                title_content2 = "You may also view associated documents for a catalogue."

                #Context Data
                context = {
                        "title": title,
                        "title_content1": title_content1,
                        "title_content2": title_content2,
                        "catalogues": catList,
                }

                return render(request, "catalogue/cat_list.html", context)
        else:
                return render(request, "unauthorized.html", {})
