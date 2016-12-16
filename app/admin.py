from django.contrib import admin
from app.models import About, Staff, AboutFeed, Consultancyservice, Service


# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    list_display = ('history', 'mission', 'vision')
    search_fields = ('whoweare', 'history')


class AboutFeedAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_position', 'client_company', 'client_url')
    search_fields = ('client_company', 'client_name')


class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'email', 'fb_username', 'image_url')
    search_fields = ('first_name', 'last_name', 'position', 'email', 'bio')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'service_desc')
    search_fields = ('service_name', 'service_desc')


class ConsultancyserviceAdmin(admin.ModelAdmin):
    list_display = ('cservice_name', 'cservice_desc')
    search_fields = ('cservice_name', 'cservice_desc')


# Register your models here.
admin.site.register(About, AboutAdmin)
admin.site.register(AboutFeed, AboutFeedAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Consultancyservice, ConsultancyserviceAdmin)
