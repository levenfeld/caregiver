# Boilerplate import
from django.contrib import admin

# Importing needed models for the application
from .models import City, SpokenLanguage, Certificate, CareGiver

# Register your models here.
admin.site.register(City)
admin.site.register(SpokenLanguage)
admin.site.register(Certificate)
admin.site.register(CareGiver)
