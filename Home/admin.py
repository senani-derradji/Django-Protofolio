from django.contrib import admin
from .models import Contact

class ContactShow(admin.ModelAdmin):
    list_display = ['name','email']


admin.site.register(Contact,ContactShow)
