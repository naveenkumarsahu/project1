from django.contrib import admin

# Register your models here.
from login.models import UserGroup,UserData
admin.site.register(UserGroup)
admin.site.register(UserData)
