from django.contrib import admin
from .models import Note, Workout, Exercise

# Register your models here.

admin.site.register(Note)
admin.site.register(Workout)
admin.site.register(Exercise)