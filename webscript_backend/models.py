from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Script(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(help_text="Please describe what the script does.",
                                   blank=True, null=True)
    notes = models.TextField(help_text="Comments, questions, problems, etc.",
                             blank=True, null=True)
    user = models.ForeignKey(User,
                             help_text="The user who submitted the script.")

    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True, auto_now_add=True)


class Event(models.Model):
    event_type = models.CharField(max_length=128,
                                  help_text="The type of event to be replayed.")
    dom_pre_event_state = models.TextField(help_text="State of DOM prior to Event firing",
                                     blank=True, null=True)
    dom_post_event_state = models.TextField(help_text="State of DOM after Event finished",
                                     blank=True, null=True)
    version = models.CharField(max_length=32,
                               help_text="Event Format version for Event. " \
                                     "Intended to allow backwards incompatible changes.",
                               default="1.0")

    script = models.ForeignKey('Script',
                               help_text="The script this event belongs to.")
    execution_order = models.FloatField(help_text="Floating point number of execution." \
                                "This allows for reconstructing the proper order of events.")

    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True, auto_now_add=True)


class Parameter(models.Model):
    name = models.CharField(max_length=64)
    value = models.TextField()
    #FIXME: We may not need to provide the datatype, but it may be useful. Need to decide.
    data_type = models.CharField(max_length=32, choices=[('Int', 'Int'),
                                                         ('Float', 'Float'),
                                                         ('Bool', 'Bool'),
                                                         ('String', 'String')])

    event = models.ForeignKey('Event')

    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True, auto_now_add=True)


#FIXME: Need to define what the replay will store and where it should store it?
#  In duplicated Events/Parameters, or similar objects with more details?
class Replay(models.Model):
    script = models.ForeignKey('Script',
                               help_text="The script that was replayed")

    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True, auto_now_add=True)
