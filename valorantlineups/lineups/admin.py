from django.contrib import admin

from .models import Agent, Lineup, ChildLineup, Map

# Register your models here.

admin.site.register(Agent)
admin.site.register(Lineup)
admin.site.register(ChildLineup)
admin.site.register(Map)
