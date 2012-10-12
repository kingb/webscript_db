from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from api import handlers

script_handler = Resource(handlers.ScriptHandler)
event_handler = Resource(handlers.EventHandler)

urlpatterns = patterns('',
   url(r'^script/(?P<script_id>[^/]+)/', script_handler),
   url(r'^script/', script_handler),
   url(r'^event/(?P<event_id>[^/]+)/', event_handler),
   url(r'^script/events/(?P<script_id>[^/]+)/', event_handler),
   url(r'^event/', event_handler),
)
