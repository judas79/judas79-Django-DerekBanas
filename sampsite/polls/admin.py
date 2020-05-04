# L3 this import was already here
from django.contrib import admin

# L3 Register your models that will sho up here.
# L4 add choice option to admin panel
from .models import Question, Choice

# L3 register Question to show up in the admin portion of the site
admin.site.register(Question)

# L4 register Choice to show up in admin panel
admin.site.register(Choice)
