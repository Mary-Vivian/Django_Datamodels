from django.contrib import admin
from .models import ClassPeriod

class ClassPeriodAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'start_time', 'end_time', 'capacity', 'attendance_count')
    search_fields = ('title', 'date', 'start_time', 'end_time')
    list_filter = ('date', 'start_time', 'end_time')
    filter_horizontal = ('students',) 

admin.site.register(ClassPeriod, ClassPeriodAdmin)
