from django.conf.urls.defaults import patterns, include, url
from tastypie.api import Api
from webscript_backend import api

v1_api = Api(api_name='v1')
v1_api.register(api.UserResource())
v1_api.register(api.ScriptResource())
v1_api.register(api.EventResource())
v1_api.register(api.ParameterResource())
v1_api.register(api.ReplayResource())
v1_api.register(api.ReplayEventResource())


urlpatterns = patterns('webscript_backend',
    url(r'^api_old/', include(v1_api.urls)),
)

