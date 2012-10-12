from piston.handler import BaseHandler
from piston.utils import rc, throttle

from webscript_backend import models

class ScriptHandler(BaseHandler):
    allowed_methods = ('GET',)  # 'PUT')
    fields = ('name',
              'notes',
              'description',
              'modification_date',
              'creation_date',
              'id',
              ('user', ('username', 'firstname', 'lastname', 'id')),
              ('events', ('event_type', 'modification_date')),
               )
    model = models.Script

    def read(self, request, script_id=None):
        base = models.Script.objects

        if script_id:
            return base.get(pk=script_id)
        else:
            return base.all()  # Or base.filter(...)

    def create(self, request):
        if request.content_type:
            data = request.data

            em = self.model(title=data['title'], content=data['content'])
            em.save()

            # for comment in data['comments']:
            #    Comment(parent=em, content=comment['content']).save()

            return rc.CREATED
        else:
            super(ScriptHandler, self).create(request)


class EventHandler(BaseHandler):
    allowed_methods = ('GET',)  # 'PUT')
    fields = ('event_type',
               'execution_order',
               'version',
               'modification_date',
               'creation_date',
               'id',
               'dom_pre_event_state',
               'dom_post_event_state',
               ('parameters', ('name',)),
               )
    exclude = ('script',)
    model = models.Event

    def read(self, request, script_id=None, event_id=None):
        base = models.Event.objects

        if script_id:
            return base.filter(script=int(script_id))
        elif event_id:
            return base.get(pk=event_id)
        else:
            return base.all()


class ParameterHandler(BaseHandler):
    allowed_methods = ('GET',)  # 'PUT')
    exclude = ('event',)
    model = models.Parameter

    def read(self, request, event_id=None):
        base = models.Parameter.objects

        if event_id:
            return base.filter(event=int(event_id))
        else:
            return base.all()
