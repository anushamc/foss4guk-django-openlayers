from django.conf.urls import patterns, url
from .views import IndexView, countyGeoJSON, AccidentsGeojson

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name="index"),    
    url(r'^countyGeoJSON/', countyGeoJSON.as_view(), name="countyGeoJSON"),
    url(r'^accidentsGeojson/', AccidentsGeojson.as_view(), name="accidentsGeojson"),
)