require([
    "esri/map",
    "esri/geometry/Extent",
    "esri/SpatialReference",
    "esri/layers/ArcGISDynamicMapServiceLayer",
    "esri/layers/ArcGISTiledMapServiceLayer",
    "esri/dijit/Scalebar",
    "esri/dijit/BasemapToggle",
    "esri/dijit/OverviewMap",
    "esri/dijit/InfoWindowLite",
    "esri/InfoTemplate",
    "esri/layers/FeatureLayer",
    "dojo/dom-construct",
    "esri/dijit/Search",
    "esri/dijit/HomeButton",
    "dojo/domReady!",
    "dojo/query"
//
], function(
    Map,
    Extent,
    SpatialReference ,
    ArcGISdymicMapServiceLayer,
    ArcGISTiledMapServiceLayer,
    Scalebar,
    BasemapToggle,
    OverviewMap,
    InfoWindowLite,
    InfoTemplate,
    FeatureLayer,
    domConstruct,
    Search,
    HomeButton

    ) {
        var map = new Map("map", {
            basemap:"satellite",
            logo:false,
            center:[85.8,41.75],
            extent: new Extent(94.51737150255514,50.471071551840855,96.52155038419323,51.938662494916795, new SpatialReference({ wkid:4326 })),
            zoom:10
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




        var search = new Search({
            map: map
         }, "search");
         search.startup();

//        geoLocate = new LocateButton({
//        map: map
//      }, "LocateButton");
//      geoLocate.startup();



         var home = new HomeButton({
             map: map
         }, "HomeButton");
         home.startup();

         //鹰眼图
         let overviewMap = new OverviewMap({
            map: map,
            attachTo: "bottom-left",
            visible:true,
            color:" #D84E13",
            opacity: 0.40
         })
         overviewMap.startup()

         //2-2显示地图范围
       function showExtent(){
          var s = "";
           s = "XMin: "+map.extent.xmin+'<br/>'
           +"YMin: "+map.extent.ymin+'<br/>'
           +"XMax: "+map.extent.xmax+'<br/>'
           +"YMax: "+map.extent.ymax;
           document.getElementById('lable').innerHTML=s;
       }
       map.on('extent-change',showExtent)


      query("select").on("change",function(event){
      //获得下拉框的文本信息
      var value=this.value;
      let kuli1 = new Extent(94.51737150255514,50.471071551840855,96.52155038419323,51.938662494916795, new SpatialReference({ wkid:4326 }))
      let baoding = new Extent(95.4329293972433, 50.68172023440176, 95.55819057734545, 50.77344466834384, new SpatialReference({ wkid:4326 }))
      let langfang = new Extent(114.5, 38.10, 116, 39.90, new SpatialReference({ wkid:4326 }))
        switch(value)
        {
          case '库梨1':
                map.setExtent(langfang);
                break;
          case '库梨2':
                map.setExtent(kuli2);
                break;
          case '库梨3':
                map.setExtent(baoding);
                break;
          case '鸡空':
                map.setExtent(baoding);
                break;
          case '地膜5':
                map.setExtent(baoding);
                break;
          case '保定':
                map.setExtent(baoding);
                break;
          case '张家口':
                map.setExtent(baoding);
                break;
          case '承德':
                map.setExtent(baoding);
                break;
          case '沧州':
				        map.setExtent(baoding);
				        break;
          case '廊坊':
          map.setExtent(langfang);
          break;
          case '衡水':
                map.setExtent(baoding);
                break;

        }
      })

      var scalebar = new Scalebar({
         map: map,
         scalebarUnit: "metric"
//         attachTo: "top-left",
      });

      var toggle = new BasemapToggle({
        map: map,
        basemap: "satellite"
      }, "BasemapToggle");
      toggle.startup();

});
