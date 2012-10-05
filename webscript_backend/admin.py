from django.contrib import admin
from webscript_backend import models

class ScriptAdmin(admin.ModelAdmin):
    pass

class EventAdmin(admin.ModelAdmin):
    pass

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
