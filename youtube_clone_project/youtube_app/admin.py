from django.contrib import admin
from .models import BackendData
from .models import Comments

# Register your models here.
admin.site.register(BackendData)
admin.site.register(Comments)