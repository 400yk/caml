from django.contrib import admin
from ca.models import *

class ProgramAdmin(admin.ModelAdmin):
    fieldsets = [
            #(None, {'fields': ['name', 'university']}),
            ]
    list_display = ('degree', 'name', 'university')

# Register your models here.
admin.site.register(Question)
admin.site.register(Package)
admin.site.register(University)
admin.site.register(Program, ProgramAdmin)
admin.site.register(UserProfile)
admin.site.register(Resume)
admin.site.register(PS)
admin.site.register(LOR)
admin.site.register(BS)
admin.site.register(Tracking)

