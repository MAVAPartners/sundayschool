from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from exam.models import School, Student, User

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(School)
admin.site.register(Student)
