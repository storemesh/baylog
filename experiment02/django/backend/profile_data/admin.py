from django.contrib import admin
from profile_data.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Profile._meta.fields]