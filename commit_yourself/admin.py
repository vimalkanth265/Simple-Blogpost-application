from django.contrib import admin
from .models import BlogPost, profile
# Register your models here.
admin.site.register(BlogPost)

admin.site.register(profile)