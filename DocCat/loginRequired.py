from django.contrib.auth.decorators import login_required
from django.views.static import serve

#We use this decorator and custom serve function to prevent the download of files by unuathorised users
@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)
