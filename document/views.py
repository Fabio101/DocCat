from django.shortcuts import render
from .forms import AddDocumentForm
from .models import Document

# Create your views here.

def add(request):
        if request.user.is_authenticated():

                #context variables
                form = AddDocumentForm(request.POST or None, request.FILES or None)
                title = "Add Document"
                title_content1 = "This area allows you to add new documents to a catalogue."
                title_content2 = "There is no limit to the number of Documents one can upload, however, charges apply*"

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

def list(request):
	if request.user.is_authenticated():
		try: 
			#Get List of Documents
			documents = Document.objects.all()

			#Context Data
			context = {
				"documents": documents,
			}

		except Exception, e:
			context = {
                        	"status": '<div class="alert alert-danger" role="alert">Failure: ' + str(e) + '</div>',
                        }

		return render(request, "document/list.html", context)
        else:
                return render(request, "document/unauthorized.html", {})
