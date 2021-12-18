import { Component, Input, OnInit } from '@angular/core';


@Component({
  selector: '.app-bar-chart',
  templateUrl: './bar-chart.component.html',
  styleUrls: ['./bar-chart.component.css']
})
export class BarChartComponent implements OnInit {

  chartReady: boolean = false;

  @Input ('dataSets') dataSet: any;
  /* @Input ('widgetLabel') widgetLabel: any; */
  csi_data:Array<any> = [];
  yearWithQuarterForBar:any = [];
  _data_1 : string; 
  labelData: any= [];


  public lineChartData:any =[];
  public lineChartLabels:any =[];
  public lineChartOptions:any;
  public lineChartColors :any =[];
  public lineChartLegend: boolean 
  public lineChartType:string = 'bar';


/* countData:Array<any> = [97.2, 96.9, 94.47, 88, 87.2, 89.6];
 */
ngOnInit(){
  
      /* console.log("ngOnInit");
      console.log("dataSet"); */
    /*  console.log(this.dataSet);  */
    if (this.dataSet.length != 0) {
      for(var i = this.dataSet.length - 1;i>=this.dataSet.length-6;i--)
      {//Math.round( ($scope.ChartData[i].csi)) * 10) / 10
        this.csi_data.push(this.round(this.dataSet[i].csi,1));
        this.yearWithQuarterForBar.push(this.dataSet[i].year+"-Q"+this.dataSet[i].quarter);
      }
      this.draw_chart(this.csi_data, this.yearWithQuarterForBar); 
    }
 
  }
  /* function declare */
round(value, precision) {
    var multiplier = Math.pow(100, precision || 0);
    return Math.round(value * multiplier) / multiplier;
}

public draw_chart(_data:any[], _label:any[]) {
 /*  console.log("_data");
  console.log(_data); */

  this.lineChartData =[{data: _data}];
  this.lineChartLabels = this.yearWithQuarterForBar;
  
     /* public lineChartLabels:Array<any> = this.yearWithQuarterForBar;   */
     /* this.lineChartLabels= ["2010-Q1", "2010-Q2", "2010-Q3", "2009-Q1", "2009-Q2", "2009-Q3"]; */
     this.lineChartOptions = {
      scales: {
        yAxes: [{
           gridLines : {
              display : false
            },
          id: 'A',
          type: 'linear',
          position: 'left',
          /* scaleLabel: {
            display: true,
            labelString: 'Customer Satisfaction Index'
          } */
        }],
        xAxes: [{
          gridLines : {
            display : false
          }
        }]
      },
      legend: {
        position: 'bottom',
        labels: {
          usePointStyle: true
        }
      }
    };
    
    this.lineChartColors = [
      /* { // grey
        backgroundColor: 'blue',
        borderColor: 'blue',
        pointBackgroundColor: 'blue'
      }, */
      { // dark grey
        backgroundColor: '#ab7aef',
        borderColor: 'pink',
        pointBackgroundColor: 'pink'
      }
    ];
   this.lineChartLegend = false;
   this.lineChartType = 'bar';
   this.chartReady = true;
}
/* 
public barChartData:any[] = [
  {data: [this.csi_data], label: 'Series A'},
  {data: [28, 48, 40, 19, 86, 27, 90], label: 'Series B'}
];

public barChartData1:any[] = [
  {data:  this.csi_data, label: 'Series A'},
  //{data: [28, 48, 40, 19, 86, 27, 90], label: 'Series B'}
];

  public lineChartData:any[] = this.barChartData;
   //public lineChartLabels:Array<any> = this.yearWithQuarterForBar;  
   public lineChartLabels:Array<any> = ["2010-Q1", "2010-Q2", "2010-Q3", "2009-Q1", "2009-Q2", "2009-Q3"];
  public lineChartOptions:any = {
    scales: {
      yAxes: [{
         gridLines : {
            display : false
          },
        id: 'A',
        type: 'linear',
        position: 'left',
        scaleLabel: {
          display: true,
          labelString: 'Customer Satisfaction Index'
        }
      }],
      xAxes: [{
        gridLines : {
          display : false
        }
      }]
    },
    legend: {
      position: 'bottom',
      labels: {
        usePointStyle: true
      }
    }
  };
  public lineChartColors:Array<any> = [
   
    { // dark grey
      backgroundColor: 'pink',
      borderColor: 'pink',
      pointBackgroundColor: 'pink'
    }
  ];
  public lineChartLegend:boolean = true;
  public lineChartType:string = 'bar';
 

 
  // events
  public chartClicked(e:any):void {
    console.log(e);
  }
 
  public chartHovered(e:any):void {
    console.log(e);
  } */

}
