from django.contrib import admin
from .models import room, message,signup

# Register your models here.
admin.site.register(room)
admin.site.register(message)
admin.site.register(signup)