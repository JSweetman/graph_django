from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import make_graph

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'graph_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', make_graph),
)
