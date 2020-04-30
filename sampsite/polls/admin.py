# L3 this import was already here
from django.contrib import admin

# L3 Register your models that will sho up here.
from .models import Question

# L3 register Question to show up in the admin portion of the site
admin.site.register(Question)
