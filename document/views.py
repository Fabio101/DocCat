from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from catalogue.models import Catalogue
from .forms import ListDocumentForm
from .forms import AddDocumentForm
from .models import Document

# Create your views here.

def add(request):
        if request.user.is_authenticated():

                #context variables
                form = AddDocumentForm(request.POST or None, request.FILES or None)
                title = "Add Document"
                title_content1 = "This area allows you to add new documents to a catalogue."
                title_content2 = "There is no limit to the number of Documents one can upload."

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
                                title_content2 = "You can continue to add more Documents."

                                context = {
                                        "title": title,
                                        "title_content2" : title_content2,
                                        "status": '<div class="alert alert-success" role="alert">Successfully Added Document!</div>',
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

                return render(request, "document/add.html", context)
        else:
                return render(request, "document/unauthorized.html", {})

def CatList(request):
	if request.user.is_authenticated():

		form = ListDocumentForm(request.POST or None)

		title = "Documents"
                title_content1 = "This area allows you to view and download your documents."
                title_content2 = "Please select a catalogue from the list to display the revelant documents."
		button = "Select Catalogue"

		#Context Data for catalogue selection
                context = {
                	"title": title,
                        "title_content1": title_content1,
                        "title_content2": title_content2,
			"button": button,
                        "form": form,
                }

		return render(request, "document/cat_list.html", context)
	else:
                return render(request, "unauthorized.html", {})

def DocList(request):
	if request.user.is_authenticated():

		#We store the catalogue ID into the session if the request was POSTed, if not, we read from the session
		if request.POST:
			catalogueID = request.POST['Catalogue']
			request.session['catalogueID'] = catalogueID
		else:
			catalogueID = request.session['catalogueID']	

		#Get List of Documents using the session catalogue ID
		relatedDocs = Document.objects.filter(catalogue = catalogueID)

		#Setup Pagination
		paginator = Paginator(relatedDocs, 10)

		#Check if a page number exists, if not set to page 1
		try:
			page = int(request.GET.get('page', '1'))
		except:
			page = 1			

		#If page is empty or invalid, return to last page
		try:
               		docList = paginator.page(page)
               	except(EmptyPage, InvalidPage):
			docList = paginator.page(paginator.num_pages)

		title = "Documents"
               	title_content1 = "This area allows you to view and download your documents."
               	title_content2 = "You may also modify or delete documents."

		#Context Data
               	context = {
               		"title": title,
                       	"title_content1": title_content1,
                       	"title_content2": title_content2,
                       	"documents": docList,
               	}

		return render(request, "document/doc_list.html", context)
        else:
                return render(request, "unauthorized.html", {})
