from django.contrib import admin
from webscript_backend import models

class ScriptAdmin(admin.ModelAdmin):
    pass

class EventAdmin(admin.ModelAdmin):
    list_display = ('execution_order', 'event_type', 'display_parameters', 'script',)
    list_filter = ('script__name',
                   'script__user__username',
                   'event_type')

    search_fields = ('event_type',
                     'dom_pre_event_state',
                     'dom_post_event_state',
                     'script__name',
                     'parameter__name',
                     'parameter__value',
                     )


    ordering = ('execution_order',)

class ParameterAdmin(admin.ModelAdmin):
    pass

class ReplayAdmin(admin.ModelAdmin):
    pass

class ReplayEventAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Script, ScriptAdmin)
admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Parameter, ParameterAdmin)
admin.site.register(models.Replay, ReplayAdmin)
admin.site.register(models.ReplayEvent, ReplayEventAdmin)
