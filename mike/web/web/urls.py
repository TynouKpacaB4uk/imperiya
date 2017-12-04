from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('main.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^competition/', include('competition.urls')),
    url(r'^team/', include('team.urls')),
    url(r'^question/', include('question.urls')),
    url(r'^partners/', include('partners.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^games/', include('games.urls')),
    url(r'^table/', include('table.urls')),
    url(r'^photogallery/', include('photogallery.urls')),

]
