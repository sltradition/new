from django.contrib import admin

# Register your models here.
from functions.models import Courses, Teachers

admin.site.register(Courses)
admin.site.register(Teachers)