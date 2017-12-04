from django.conf.urls import include, url
from django.contrib import admin
from competition import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', views.competition, name='competition'),
]