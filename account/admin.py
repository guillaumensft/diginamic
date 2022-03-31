from django.contrib import admin

# Register your models here.
from .models import Profile, User

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'slug']


admin.site.register(Profile, ProfileAdmin)

