from django.contrib import admin

from movies.account.models import CustomUser


admin.site.register(CustomUser)