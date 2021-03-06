from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from . import settings
from django.views.generic import RedirectView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'graph_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='/graph/')),
    url(r'^graph/', include('graphs.urls')),
)
