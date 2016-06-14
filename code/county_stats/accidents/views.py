from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.core.serializers import serialize
from .models import County, Accident
from django.http.response import HttpResponse

class IndexView(TemplateView):
    template_name = 'accidents/index.html'
    
    def get_context_data(self, **kwargs):
        return kwargs


class countyGeoJSON(View):
    def get(self, request):
    	geojson = serialize('geojson', County.objects.all(),
          geometry_field='geom',
          fields=('name',))
    	return HttpResponse(geojson)


class AccidentsGeojson(View):
    def get(self, request):
    	#get county from county name in request
    	county = County.objects.filter(name=request.GET.get('county')).first()
    	#if no geom fields exist, create them for accident
    	#migrations would be better, but are more complex
    	no_accident_exists = Accident.objects.filter(geom__isnull=False).exists()
    	if no_accident_exists:
    		Accident.objects.raw('UPDATE accidents_accident SET geom=ST_SIMPLIFY(ST_GeomFromText(\'POINT(\' || %s || \' \' || %s || \')\',27700);',[location_easting_osgr, location_northing_osgr])
    	#use within query to filter all points within the geometry
    	geojson = {}
    	if county:
	    	geojson = serialize('geojson', Accident.objects.filter(geom__within=county.geom),
	          geometry_field='geom',
	          fields=('accident_index', 'accident_severity'))
    	return HttpResponse(geojson)
