from django.contrib import admin
from .models import Bin, Teacher, Booked_Bin
# Register your models here.

admin.site.register(Bin)
admin.site.register(Teacher)
admin.site.register(Booked_Bin)