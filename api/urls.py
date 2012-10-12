from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from api import handlers

script_handler = Resource(handlers.ScriptHandler)
event_handler = Resource(handlers.EventHandler)
param_handler = Resource(handlers.ParameterHandler)

urlpatterns = patterns('',
   url(r'^script/(?P<script_id>[^/]+)/', script_handler),
   url(r'^script/', script_handler),
   url(r'^event/(?P<event_id>[^/]+)/', event_handler),
   url(r'^script_events/(?P<script_id>[^/]+)/', event_handler),
   url(r'^event/', event_handler),
   url(r'^event_parameters/(?P<event_id>[^/]+)/', param_handler),
   url(r'^parameter/', param_handler),
)
