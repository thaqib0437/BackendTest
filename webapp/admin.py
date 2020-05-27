from django.contrib import admin
from .models import User, activity_periods

# Register your models here.

admin.site.register(User)

admin.site.register(activity_periods)