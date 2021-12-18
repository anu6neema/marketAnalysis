import {Directive,ElementRef,Input,OnInit} from '@angular/core';
declare var google:any;

@Directive({
  selector: '[appMapsView]'
})
export class MapsViewDirective implements OnInit {

  public _element:any;
/*   @Input('chartType') public chartType:string;
  @Input('chartOptions') public chartOptions: Object; */
  @Input('mapData') public mapData: any; 

 constructor(public element: ElementRef) {
    this._element = this.element.nativeElement;
  }

  ngOnInit() {
    /* var mapOptions = {
      zoom: 2,
      center: new google.maps.LatLng(30.0000, 0.0000),
      mapTypeId: google.maps.MapTypeId.TERRAIN
    };
   var map = new google.maps.Map(document.getElementById('map'), this.mapOptions);
   
    var infoWindow = new google.maps.InfoWindow();
    for (var i=0; i < this.mapData.length; i++) {    
      this.createMarker(this.mapData[i]);
    }
 */

let mapProp = {
  center: new google.maps.LatLng(30.0000, 0.0000),
  zoom: 2,
  mapTypeId: google.maps.MapTypeId.ROADMAP
};
let map = new google.maps.Map(document.getElementById("map"), mapProp);


    
  }

  markers:any = [];
  markersFullView:any = [];

 public mapOptions = {
    zoom: 2,
    center: new google.maps.LatLng(30.0000, 0.0000),
    mapTypeId: google.maps.MapTypeId.TERRAIN
  };



/*  createMarker(info){
  var marker = new google.maps.Marker({
      map:this.map,
      position: new google.maps.LatLng(info.latitudedata, info.longitudedata),
      title: info.city,
      icon: info.pin
  });
  var address = (info.address2 != undefined ? (info.address1 + " , " + info.address2) : info.address1);
  var contentString = '<div class="layout" style="padding-left:20px;height:210px;width:260px;overflow-y:hidden;overflow-x:hidden" ><div id="storelayout" class="storelayout" style="padding-top:5px;box-shadow: 3px 3px  3px 3px #888888;margin-top:10px;" ><p style="color:#fff;font-size:12px;margin-left: 13px;"> '+info.plantname+'</p><p style="border-bottom: 1px solid grey;margin-top: -11px; margin-bottom:5px;"></p><p style="color:#404040;font-weight:bold;font-size:10px; margin-left: 13px;">Plant Type :<span style="font-weight:bold;color:black"> '+ info.planttype +' </span></p><p style="border-bottom: 1px solid grey;margin-top: -11px; margin-bottom: 5px;"></p><p style="color:#404040;font-weight:bold;font-size:10px; margin-left: 13px;">Address :<span style="font-weight:bold;color:black"> '+ address +' </span></p><p style="border-bottom: 1px solid grey;margin-top: -11px; margin-bottom: 5px;"></p><p style="color:#404040;font-weight:bold;font-size:10px; margin-left: 13px;">City :<span style="font-weight:bold;color:black"> '+ info.city +' </span></p><p style="border-bottom: 1px solid grey;margin-top: -11px; margin-bottom: 5px;"></p><p style="color:#404040;font-weight:bold;font-size:10px; margin-left: 13px;">Country :<span style="font-weight:bold;color:black"> '+ info.country +' </span></p><p style="border-bottom: 1px solid grey;margin-top: -11px; margin-bottom: 0px;"></p><p><img src="images/Plantlayout.png" style="cursor: pointer;width:100%;height:80px;" ng-click="showPlantLayout(\''+info.plantid+'\',\''+address+'\',\''+info.city+'\',\''+info.latitudedata+'\',\''+info.longitudedata+'\',\''+info.plantname+'\',\''+info.country+'\',\''+info.state+'\',\''+info.zipcode+'\')"></img></p></div></div>';
   */
/*   google.maps.event.addListener(marker, 'click', function(){
var compiled = $compile(contentString)($scope);
var infoWindow = new google.maps.InfoWindow({ content: compiled[0]});
      infoWindow.open($scope.map, marker);
  }); */
/* }; */

}


