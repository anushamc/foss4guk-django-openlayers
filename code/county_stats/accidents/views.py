from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.core.serializers import serialize
from .models import County
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
