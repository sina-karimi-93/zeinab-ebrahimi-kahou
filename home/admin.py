from django.contrib import admin
from .models import Banner, Skill, MyExperience, MyEducation, ContactMe, Language, Research, Activity
from django.contrib.auth.models import Group

admin.site.site_header = 'Admin Panel'
admin.site.unregister(Group)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill', 'level')
    list_editable = ('level',)


@admin.register(Language)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('language', 'level')
    list_editable = ('level',)


@admin.register(MyExperience)
class MyExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc', 'date')
    list_display_links = ('id', 'title', 'desc', 'date')


@admin.register(MyEducation)
class MyEducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc', 'date')
    list_display_links = ('id', 'title', 'desc', 'date')


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'link', 'file', 'references', 'image')
    list_display_links = ('id', 'title')


@admin.register(ContactMe)
class ContactMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_read', 'subject', 'message')
    list_editable = ('is_read',)
