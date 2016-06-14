
      var raster = new ol.layer.Tile({
        source: new ol.source.OSM()
      });


      var map = new ol.Map({
        layers: [raster],
        target: 'map',
        view: new ol.View({
          center: [0, 0],
          zoom: 2
        })
      });

