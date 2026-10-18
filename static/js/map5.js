require([
    "esri/map",
    "esri/layers/ArcGISDynamicMapServiceLayer",
    "esri/layers/ArcGISTiledMapServiceLayer",
    "esri/toolbars/navigation",
    "esri/dijit/BasemapGallery",
    "esri/dijit/Legend",
    "esri/layers/FeatureLayer",
    "dojo/dom",
    "dojo/_base/lang",
    "dojo/json",
    "esri/config",
    "esri/graphic",
    "esri/geometry/Geometry",
    "esri/geometry/Extent",
    "esri/SpatialReference",
    "esri/tasks/GeometryService",
    "esri/tasks/AreasAndLengthsParameters",
    "esri/toolbars/draw",
    "esri/symbols/SimpleFillSymbol",
    "esri/symbols/SimpleMarkerSymbol",
    "esri/symbols/SimpleLineSymbol",
    "esri/symbols/PictureFillSymbol",
    "esri/symbols/CartographicLineSymbol",
    "esri/graphic",
    "esri/Color",
    "dojo/dom",
    "dojo/on",
    "esri/arcgis/utils",
    "dojo/parser","esri/dijit/Bookmarks",

//    "dojo/domReady!"
], function(
    Map,
    ArcGISdymicMapServiceLayer,
    ArcGISTiledMapServiceLayer,
    Navigation,
    BasemapGallery,
    Legend,
    FeatureLayer,
    dom,
    lang,
    json,
    esriConfig,
    Graphic,
    Geometry,
    Extent,
    SpatialReference,
    GeometryService,
    AreasAndLengthsParameters,
    Draw,
    SimpleFillSymbol,
    SimpleMarkerSymbol,
    SimpleLineSymbol,
    PictureFillSymbol,
    CartographicLineSymbol,
    Graphic,
    Color,
    dom,
    on, arcgisUtils,parser,Bookmarks
    ) {
        parser.parse();
        var map = new Map("map", {
            basemap:"hybrid",
//            hybrid
            logo:false,
            center:[85.8,41.75],
            zoom:10
        });

        let dynamicLayer=new ArcGISdymicMapServiceLayer
        ("http://localhost:6080/arcgis/rest/services/Kerle/三大系数反演/MapServer")

        map.addLayer(dynamicLayer)
        map.on("load", initToolbar);


        // Create the bookmark widget
          // specify "editable" as true to enable editing
          var bookmarks = new Bookmarks({
            map: map,
            bookmarks: [],
            editable: true
          }, "bookmarks");

          // Bookmark data objects
          var bookmarkJSON = {
            first: {
              "extent": {
                "xmin": -12975100,
                "ymin": 3993900,
                "xmax": -12964100,
                "ymax": 4019500,
                "spatialReference": {
                  "wkid": 102100,
                  "latestWkid": 3857
                }
              },
              "name": "Palm Springs, CA"
            },
            second: {
              "extent": {
                "xmin": -13052100,
                "ymin": 4024900,
                "xmax": -13041100,
                "ymax": 4050500,
                "spatialReference": {
                  "wkid": 102100,
                  "latestWkid": 3857
                }
              },
              "name": "Redlands, California"
            },
            third: {
              "extent": {
                "xmin": -13048800,
                "ymin": 3844800,
                "xmax": -13037800,
                "ymax": 3870400,
                "spatialReference": {
                  "wkid": 102100,
                  "latestWkid": 3857
                }
              },
              "name": "San Diego, CA"
            },
          };

          // Add bookmarks to the widget
          Object.keys(bookmarkJSON).forEach(function (bookmark){
            bookmarks.addBookmark(bookmarkJSON[bookmark]);
          });



        function openLayers1()
         {
            visible=[];
            visible.push(2);
            dynamicLayer.setVisibleLayers(visible);
         }
       document.getElementById("S1").addEventListener('click',openLayers1)

        function openLayers5()
         {
            visible=[];
            visible.push(0);
            dynamicLayer.setVisibleLayers(visible);
         }
       document.getElementById("S5").addEventListener('click',openLayers5)

        function openLayers3()
         {
            visible=[];
            visible.push(1);
            dynamicLayer.setVisibleLayers(visible);
         }
       document.getElementById("SI_T").addEventListener('click',openLayers3)

        function closeAllLayers()
       {
          visible=[-1];
          dynamicLayer.setVisibleLayers(visible);
       }
       document.getElementById("close").addEventListener('click',closeAllLayers)

       var navToolbar = new Navigation(map);
       function quantu() {
         navToolbar.zoomToFullExtent();
       }
       document.getElementById("quantu").addEventListener('click',quantu)

       function qian() {
         navToolbar.zoomToPrevExtent();
       }
       document.getElementById("qian").addEventListener('click',qian)

       function hou() {
         navToolbar.zoomToNextExtent();
       }
       document.getElementById("hou").addEventListener('click',hou)

       function da() {
         navToolbar.activate(Navigation.ZOOM_IN);
       }
       document.getElementById("da").addEventListener('click',da)

       function xiao() {
         navToolbar.activate(Navigation.ZOOM_OUT);
       }
       document.getElementById("xiao").addEventListener('click',xiao)

       function manyou() {
         navToolbar.activate(Navigation.PAN);
       }
       document.getElementById("manyou").addEventListener('click',manyou)

       var basemapGallery = new BasemapGallery({
        showArcGISBasemaps: true,
        map: map
      }, "basemapGallery");
      basemapGallery.startup();

      function mianji() {
        var tb = new Draw(map);
        tb.on("draw-end", lang.hitch(map, getAreaAndLength));
        tb.activate(Draw.FREEHAND_POLYGON);
      }
      document.getElementById("mianji").addEventListener('click',mianji)
      var geometryService = new GeometryService("https://sampleserver6.arcgisonline.com/arcgis/rest/services/Utilities/Geometry/GeometryServer");
      geometryService.on("areas-and-lengths-complete", outputAreaAndLength);
      function getAreaAndLength(evtObj) {
      var map = this,
          geometry = evtObj.geometry;
      map.graphics.clear();

      var graphic = map.graphics.add(new Graphic(geometry, new SimpleFillSymbol()));

      //setup the parameters for the areas and lengths operation
      var areasAndLengthParams = new AreasAndLengthsParameters();
      areasAndLengthParams.lengthUnit = GeometryService.UNIT_FOOT;
      areasAndLengthParams.areaUnit = GeometryService.UNIT_ACRES;
      areasAndLengthParams.calculationType = "geodesic";
      geometryService.simplify([geometry], function(simplifiedGeometries) {
        areasAndLengthParams.polygons = simplifiedGeometries;
        geometryService.areasAndLengths(areasAndLengthParams);
      });
    }
    function outputAreaAndLength(evtObj) {
      var result = evtObj.result;
      console.log(json.stringify(result));
      dom.byId("area").innerHTML = result.areas[0].toFixed(3) + " 英亩";
      dom.byId("length").innerHTML = result.lengths[0].toFixed(3) + " 英尺";
    }
    function clear(){
        map.graphics.clear();
    }
    document.getElementById("clear").addEventListener('click',clear)

    // markerSymbol is used for point and multipoint, see http://raphaeljs.com/icons/#talkq for more examples
        var markerSymbol = new SimpleMarkerSymbol();
        markerSymbol.setPath("M16,4.938c-7.732,0-14,4.701-14,10.5c0,1.981,0.741,3.833,2.016,5.414L2,25.272l5.613-1.44c2.339,1.316,5.237,2.106,8.387,2.106c7.732,0,14-4.701,14-10.5S23.732,4.938,16,4.938zM16.868,21.375h-1.969v-1.889h1.969V21.375zM16.772,18.094h-1.777l-0.176-8.083h2.113L16.772,18.094z");
        markerSymbol.setColor(new Color("#00FFFF"));

        // lineSymbol used for freehand polyline, polyline and line.
        var lineSymbol = new CartographicLineSymbol(
          CartographicLineSymbol.STYLE_SOLID,
          new Color([255,0,0]), 10,
          CartographicLineSymbol.CAP_ROUND,
          CartographicLineSymbol.JOIN_MITER, 5
        );

        // fill symbol used for extent, polygon and freehand polygon, use a picture fill symbol
        // the images folder contains additional fill images, other options: sand.png, swamp.png or stiple.png
        var fillSymbol = new PictureFillSymbol(
          "/static/images/盐碱地1.jpg",
          new SimpleLineSymbol(
            SimpleLineSymbol.STYLE_SOLID,
            new Color('#000'),
            1
          ),
          42,
          42
        );

        function initToolbar() {
          tb = new Draw(map);
          tb.on("draw-end", addGraphic);

          // event delegation so a click handler is not
          // needed for each individual button
          on(dom.byId("info1"), "click", function(evt) {
            if ( evt.target.id === "info1" ) {
              return;
            }
            var tool = evt.target.id.toLowerCase();
            map.disableMapNavigation();
            tb.activate(tool);
          });
        }

        function addGraphic(evt) {
          //deactivate the toolbar and clear existing graphics
          tb.deactivate();
          map.enableMapNavigation();

          // figure out which symbol to use
          var symbol;
          if ( evt.geometry.type === "point" || evt.geometry.type === "multipoint") {
            symbol = markerSymbol;
          } else if ( evt.geometry.type === "line" || evt.geometry.type === "polyline") {
            symbol = lineSymbol;
          }
          else {
            symbol = fillSymbol;
          }

          map.graphics.add(new Graphic(evt.geometry, symbol));
        }
        var legend = new Legend({
        map:map,
        layerInfos:[{
          layer:dynamicLayer,
          title:"土壤盐渍化分级"
      }]
    },"legendDiv");
    legend.startup();

        var basemapGallery = new BasemapGallery({
        showArcGISBasemaps: true,
        map: map
        }, "basemapGallery");
        basemapGallery.startup();

        basemapGallery.on("error", function(msg) {
        console.log("basemap gallery error:  ", msg);
      });



    });
