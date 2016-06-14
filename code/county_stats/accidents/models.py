from django.contrib.gis.db import models

class County(models.Model):

    # Django fields corresponding to attributes in shapefile.
    name = models.CharField(max_length=60)
    area_code = models.CharField(max_length=3)
    descriptio = models.CharField(max_length=50)
    file_name = models.CharField(max_length=50)
    number = models.FloatField()
    number0 = models.FloatField()
    polygon_id = models.IntegerField()
    unit_id = models.IntegerField()
    code = models.CharField(max_length=9)
    hectares = models.FloatField()
    area = models.FloatField()
    type_code = models.CharField(max_length=2)
    descript0 = models.CharField(max_length=25)
    type_cod0 = models.CharField(max_length=3, null=True)
    descript1 = models.CharField(max_length=25, null=True)

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    geom = models.MultiPolygonField(srid=27700)
