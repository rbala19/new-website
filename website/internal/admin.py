from django.contrib import admin

from .models import Member, Event, Committee, SubCommittee, Division

class MemberAdmin(admin.ModelAdmin):
    actions = ['delete_selected']
    ordering = ['username']
    list_filter = ('status', 'semester_joined')
    filter_horizontal = ('committees', 'subcommittees', 'divisions')
    list_display = ('username', 'full_name', 'email', 'status', 'title')
    search_fields = ('username', 'first_name', 'last_name', 'email')

    def full_name(self, o):
        return o.get_full_name()

class EventAdmin(admin.ModelAdmin):
    actions = ['delete_selected']
    ordering = ['name']
    # list_filter = ('created_by', 'point_person', 'confirmed', 'complete')
    list_filter = ('created_by', 'point_person', 'confirmed')
    # list_display = ('name','title', 'speaker_full_name', 'time', 'venue', 'point_person',
    #                 'confirmed', 'complete')
    list_display = ('name', 'title', 'speaker_full_name', 'time', 'venue', 'point_person',
                    'confirmed')
    search_fields = ('name', 'title', 'speaker_first_name', 'speaker_last_name', 'point_person')

class CommitteeAdmin(admin.ModelAdmin):
    ordering = ['name']
    filter_horizontal = ('members',)
    list_display = ('name', 'friendly_name', 'vp')

class SubCommitteeAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_filter = ('members',)
    filter_horizontal = ('members',)
    list_display = ('name', 'friendly_name', 'parent_committee', 'project_manager')

class DivisionAdmin(admin.ModelAdmin):
    ordering = ['name']
    filter_horizontal = ('members',)
    list_display = ('name', 'friendly_name', 'director')

admin.site.register(Member, MemberAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Committee, CommitteeAdmin)
admin.site.register(SubCommittee, SubCommitteeAdmin)
admin.site.register(Division, DivisionAdmin)
