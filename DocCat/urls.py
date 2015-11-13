from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.static import serve

#We use this decorator and custom serve function to prevent the download of files by unuathorised users
@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)

urlpatterns = [
    # Examples:
    # url(r'^$', 'DocCat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #home page
    url(r'^$', 'home.views.home', name='home'),

    #Registration and Login
    url(r'^accounts/', include('registration.backends.default.urls')),

    #Catalogue URL's
    url(r'^add_cat/', 'catalogue.views.add', name='add_cat'),
    url(r'^list_cat/', 'catalogue.views.CatList', name='list_cat'),
    url(r'^del_cat/', 'catalogue.views.delete', name='del_cat'),

    #Document URLS's
    url(r'^add_doc/', 'document.views.add', name='add_doc'),
    url(r'^list_doc/', 'document.views.DocList', name='list_doc'),
    url(r'^list_cat_doc', 'document.views.CatList', name='list_cat_doc'),
    url(r'^del_doc/', 'document.views.delete', name='del_doc'),
    url(r'^get_doc/', 'document.views.download', name='get_doc'),
    url(r'^uploads/(?P<path>.*)$', protected_serve, {'document_root': settings.MEDIA_ROOT}),
]
