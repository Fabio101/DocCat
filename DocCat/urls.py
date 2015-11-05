from django.conf.urls import include, url
from django.contrib import admin

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

    #Document URLS's
    url(r'^add_doc/', 'document.views.add', name='add_doc'),
    url(r'^list_doc/', 'document.views.list', name='list_doc'),
]
