
      var raster = new ol.layer.Tile({
        source: new ol.source.OSM()
      });

      var vector = new ol.layer.Vector({
        source: new ol.source.Vector({
          url: '/accidents/accidentsGeojson/',
          format: new ol.format.GeoJSON()
        })
      });

      var map = new ol.Map({
        layers: [raster, vector],
        target: 'map',
        view: new ol.View({
          center: [0, 0],
          zoom: 2
        })
      });

      var select = new ol.interaction.Select();

      map.addInteraction(select);
      select.on('select', function(e) {
        document.getElementById('comments').innerHTML = '&nbsp;' +
            e.target.getFeatures().getLength() +
            ' selected features (last operation selected ' + e.selected.length +
            ' and deselected ' + e.deselected.length + ' features)';
      });
