
      var raster = new ol.layer.Tile({
        source: new ol.source.OSM()
      });

      var county = new ol.layer.Vector({
        source: new ol.source.Vector({
          url: '/accidents/countyGeoJSON/',
          format: new ol.format.GeoJSON()
        })
      });

      var accident_source = new ol.source.Vector({
          url: '/accidents/accidentsGeojson/?county=null',
          format: new ol.format.GeoJSON()
        });

      var accident = new ol.layer.Vector({
        source: accident_source
      });

      var map = new ol.Map({
        layers: [raster, county],
        target: 'map',
        view: new ol.View({
          center: [0, 0],
          zoom: 2
        })
      });

      var select = new ol.interaction.Select({
        layers:[county]
      });

      map.addInteraction(select);
      select.on('select', function(e) {
        accident.setSource({
          url: '/accidents/accidentsGeojson/?county='+e.target.getFeatures().getArray()[0].get('name').replace(' ','%20'),
          format: new ol.format.GeoJSON()
        });
      });
