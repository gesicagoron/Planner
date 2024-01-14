from django.contrib import admin
from .models import Profile
from .models import Task, Itinerary

admin.site.register(Profile)
admin.site.register(Task)
admin.site.register(Itinerary)
# Register your models here.
