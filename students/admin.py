from django.contrib import admin
from .models import Course, Cohort, Student

# Register your models here.

class ContactStudent(admin.ModelAdmin):
    list_display = ['name', 'cohort', 'course']
    list_filter = ['cohort', 'course']
    


admin.site.register([Course, Cohort])
admin.site.register(Student, ContactStudent)
