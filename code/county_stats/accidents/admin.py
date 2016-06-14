from django.contrib.gis import admin
from .models import County

admin.site.register(County, admin.GeoModelAdmin)