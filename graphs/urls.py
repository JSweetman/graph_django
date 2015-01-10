from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import create_graph, get_graph

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'graph_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', create_graph),
    url(r'^(?P<graph_id>\d+)/$', get_graph),
)
