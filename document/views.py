from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse
from django.conf import settings
from catalogue.models import Catalogue
from .forms import ListDocumentForm
from .forms import AddDocumentForm
from .models import Document

# Create your views here.

def add(request):
        if request.user.is_authenticated():

		if request.GET and 'documentID' in request.GET:
                        documentID = request.GET.get('documentID')
                        document = Document.objects.get(id = documentID)

                        #We load the instance of the catalogue into the form to edit the fields
                        form = AddDocumentForm(request.POST or None, initial={'name': document.name, 'catalogue': document.catalogue, 'description': document.description, 'document': document.document}, instance=document)
                        title = "Edit Document"
                        button = "Edit"
                        status = "Modified"
                else:
                        form = AddDocumentForm(request.POST or None)
                        title = "Add Document"
                        button = "Add"
                        status = "Added"

                #context variables
                title_content1 = "This area allows you to " + button + " documents to a catalogue."
                title_content2 = "There is no limit to the number of Documents one can upload."

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
                                title_content2 = "You can continue to " + button + " more Documents."

                                context = {
                                        "title": title,
                                        "title_content2" : title_content2,
                                        "status": '<div class="alert alert-success" role="alert">Successfully ' + status + ' Document!</div>',
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

                return render(request, "document/add.html", context)
        else:
                return render(request, "unauthorized.html", {})

def delete(request):
        if request.user.is_authenticated():

                if request.GET and 'documentID' in request.GET:
                        documentID = request.GET.get('documentID')

                        #We delete the related documents but need to get the Catalogue ID first, we instanciate a seperate object for this
			catalogue = Document.objects.filter(id = documentID)[0]
			catalogueID = catalogue.catalogue

                        Document.objects.filter(id = documentID).delete()

                        #We just go back to the Document list from here passing the cat ID in GET.
                        return redirect('document.views.DocList')
        else:
                return render(request, "unauthorized.html", {})

def download(request):
	if request.user.is_authenticated():

		if request.GET and 'fileName' in request.GET:

			fileName = request.GET.get('fileName')

			path = settings.MEDIA_ROOT +'/'+ fileName

			response = HttpResponse(path, content_type= None)
			response['Content-Disposition'] = 'attachment; filename='+fileName

                	return response
        else:
                return render(request, "unauthorized.html", {})

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
		elif request.GET and 'catalogueID' in request.GET:
			catalogueID = request.GET.get('catalogueID')
			request.session['catalogueID'] = catalogueID
		else:
			catalogueID = request.session['catalogueID']

		#Get List of Documents using the session catalogue ID
		relatedDocs = Document.objects.filter(catalogue = catalogueID).order_by('name')

		#Setup Pagination
		paginator = Paginator(relatedDocs, 6)

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
               	title_content2 = "You may also modify or delete documents from this listing. "

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
