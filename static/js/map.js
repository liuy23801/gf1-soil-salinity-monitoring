require([
    "esri/map",
    "esri/layers/ArcGISDynamicMapServiceLayer",
    "esri/layers/ArcGISTiledMapServiceLayer",
    "esri/dijit/InfoWindowLite",
    "esri/InfoTemplate",
    "esri/layers/FeatureLayer",
    "dojo/dom-construct",
    "dojo/domReady!"
], function(
    Map,
    ArcGISdymicMapServiceLayer,
    ArcGISTiledMapServiceLayer,
    InfoWindowLite,
    InfoTemplate,
    FeatureLayer,
    domConstruct
    ) {
        var map = new Map("map1", {
            basemap:"streets-night-vector",
            logo:false,
            center:[85.8,41.55],
            zoom:11
        });

        let dynamicLayer=new ArcGISdymicMapServiceLayer
        ("http://localhost:6080/arcgis/rest/services/1/库尔勒研究区1/MapServer")

        map.addLayer(dynamicLayer)
        var infoWindow = new InfoWindowLite(null, domConstruct.create("div", null, null, map.root));
        infoWindow.startup();
        map.setInfoWindow(infoWindow);

        var template = new InfoTemplate();
        template.setTitle("<b>库尔勒市土壤采样数据</b>");
        // template.setContent("${STATE_NAME} is in the ${SUB_REGION} sub region.");
        template.setContent("采样点名称：${采样点}<br>X轴(经度)：${X}<br>Y轴(纬度)：${Y}<br>水溶性盐量(g/Kg)：${水溶性盐量}");
        //add a layer to the map
        var featureLayer = new FeatureLayer("http://localhost:6080/arcgis/rest/services/1/库尔勒研究区1/MapServer/0", {
            mode: FeatureLayer.MODE_ONDEMAND,
            infoTemplate:template,
            outFields: ["采样点" , "X", "Y","水溶性盐量"]
        });
        map.addLayer(featureLayer);

        map.infoWindow.resize(200, 150);
    });