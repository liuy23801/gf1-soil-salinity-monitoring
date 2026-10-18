require([
    "esri/map",
    "esri/layers/ArcGISDynamicMapServiceLayer",
    "esri/layers/ArcGISTiledMapServiceLayer",


    "dojo/domReady!"
], function(
    Map,
    ArcGISdymicMapServiceLayer,
    ArcGISTiledMapServiceLayer,


    ) {
        var map = new Map("map", {
            basemap:"satellite",
            logo:false,
            center:[85.8,41.75],
            zoom:10
        });

        let dynamicLayer=new ArcGISdymicMapServiceLayer
        ("http://localhost:6080/arcgis/rest/services/1/库尔勒研究区1/MapServer")

        map.addLayer(dynamicLayer)



    });
