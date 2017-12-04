from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', views.partners, name='partners'),
]
