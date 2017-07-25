from django.contrib import admin

from .models import Member, Event, Committee, SubCommittee, Division

admin.site.register(Member)
admin.site.register(Event)
admin.site.register(Committee)
admin.site.register(SubCommittee)
admin.site.register(Division)
