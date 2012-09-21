from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie import fields

from django.contrib.auth.models import User

from webscript_backend import models


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']


class ParameterResource(ModelResource):
    event = fields.ToOneField('webscript_backend.api.EventResource', 'event')

    class Meta:
        queryset = models.Parameter.objects.all()
        resource_name = 'parameter'


class EventResource(ModelResource):
    script = fields.ToOneField('webscript_backend.api.ScriptResource', 'script')
    parameters = fields.ToManyField('webscript_backend.api.ParameterResource', 'parameter_set')

    class Meta:
        queryset = models.Event.objects.all()
        resource_name = 'event'


class ScriptResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    events = fields.ToManyField(EventResource, 'event_set')

    class Meta:
        queryset = models.Script.objects.all()
        resource_name = 'script'

        authorization = Authorization()
        #authentication = ApiKeyAuthentication()

