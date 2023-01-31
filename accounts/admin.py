from django.contrib import admin
from . import models


admin.site.register(models.Account)
admin.site.register(models.Wallet)
admin.site.register(models.Place)
admin.site.register(models.Restaurant)
