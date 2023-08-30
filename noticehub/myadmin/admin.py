from django.contrib import admin
from myadmin.models import Notice

admin.site.site_header = 'Notice Hub Web App'
class NoticeAdmin(admin.ModelAdmin):
	list_display = ['id' , 'subject', 'description', 'created_at' ,'updated_at']

admin.site.register(Notice, NoticeAdmin)
# Register your models here.
