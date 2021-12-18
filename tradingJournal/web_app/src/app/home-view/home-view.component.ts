import { Component, OnInit, ViewChild } from '@angular/core';
import {PythonDataService} from '../services/python-data.service';
import {TradeData} from './TradeData';
import {Trade_pnl_by_date} from './TradeData'
/* import { ChartsModule } from 'ng2-charts'; */

@Component({
  selector: 'app-home-view',
  templateUrl: './home-view.component.html',
  styleUrls: ['./home-view.component.css']
})
export class HomeViewComponent implements OnInit {
     
     objectKeys = Object.keys;
     plantCountResponse: any;    
     Oee_avg: any;
     Oee_value: any;
     plantOeeAvgResponse: any =[];
     csi_dataResponse: any = null;
     mapdashBoardResponse: any = null;
     Trade_data  = new TradeData() ;
     //TradePnLByDates = new Trade_pnl_by_date();
     TradePnLByDates:Array<Trade_pnl_by_date> = [];
     paperTrade : boolean = true;
     /* startdate: string = new Date().toISOString().split('T')[0];
     enddate : string = new Date().toISOString().split('T')[0]; */
    startdate: string = '2018-01-01';
    enddate : string = '2019-12-31';
    _barChartKey = [];
    clone = [{ data: [],label:"Daily Profits/losses"}]; 

    public pieChartLabels:string[] = ['Losses', 'Wins'];
    public pieChartData:number[] = [0,0];
    public pieChartColors: Array<any> = [{ // grey
      backgroundColor: ['red','green']
        },
    ];
    public pieChartType:string = 'pie';

    public barChartOptions:any = {
      scaleShowVerticalLines: false,
      responsive: true
    };
    public barChartColors  = [{backgroundColor:[]}];
    public barChartLabels:string[] = [];
    public barChartType:string = 'bar';
    public barChartLegend:boolean = false;
    public barChartData:any[] = [
      {data: [], label:"Daily Profits/losses"}
    ];

/*   private plantCounturl = "https://globalplantoperations-backend-service.run.azr-usw01-pr.ice.predix.io/performance/numPlants/";
  private plantOEEurl = "https://globalplantoperations-backend-service.run.azr-usw01-pr.ice.predix.io/performance/plantOeeAvg/";
  private csi_dataResponseurl = "https://globalplantoperations-backend-service.run.azr-usw01-pr.ice.predix.io/drillView/getDetailedCSIForAll/";
  private mapdashBoardurl = "https://globalplantoperations-backend-service.run.azr-usw01-pr.ice.predix.io/pinDetail/";
 */
  constructor(private _pyservice:PythonDataService) { }
  
  ngOnInit() {
    
    this._pyservice.getDataAnalysis(this.paperTrade, this.startdate, this.enddate).subscribe(
      data => {
        this.Trade_data = data[0]; 
        /* console.log(this.Trade_data['LOST']+ '   ' + this.Trade_data['WINS']); */
        this.pieChartData = [this.Trade_data['LOST'], this.Trade_data['WINS']];           
      }
    ); 

    this._pyservice.TradeDataforDates(this.paperTrade, this.startdate, this.enddate).subscribe(
      data => {
        for (let key in data) {
          this.TradePnLByDates.push(data[key]);
        } 
        Object.keys( this.TradePnLByDates).map((key)=> {          
          this.barChartLabels.push(this.TradePnLByDates[key]['tradedate_str']); 
          this.clone[0].data.push(this.TradePnLByDates[key]['profitloss']); 
            if (this.TradePnLByDates[key]['profitloss'] <0) {
              this.barChartColors[0].backgroundColor.push('red');
            }else{
              this.barChartColors[0].backgroundColor.push('green');
            }
         
        });
          this.barChartData = this.clone;  
      }
    );
      
}

@ViewChild("DataForm") form: any;

SubmitDates() {
  if (this.form.valid) {
    this.clone = [{ data: [] ,label:"Daily Profits/losses"}]; 
    this.barChartLabels = [];
    this.TradePnLByDates = [];
    this.barChartColors  = [{backgroundColor:[]}];     
    this._pyservice.getDataAnalysis(this.paperTrade, this.startdate, this.enddate).subscribe(
      data => {
        this.Trade_data = data[0];  
        /* console.log(this.Trade_data);  */
        this.pieChartData = [this.Trade_data['LOST'], this.Trade_data['WINS']];          
      }
    );  
    this._pyservice.TradeDataforDates(this.paperTrade, this.startdate, this.enddate).subscribe(
      data => {
        for (let key in data) {
          this.TradePnLByDates.push(data[key]);
        } 
        Object.keys( this.TradePnLByDates).map((key)=> {
         /*  console.log(this.TradePnLByDates[key]['tradedate_str']);          
          console.log(this.TradePnLByDates[key]['profitloss']); */
          this.barChartLabels.push(this.TradePnLByDates[key]['tradedate_str']); 
          this.clone[0].data.push(this.TradePnLByDates[key]['profitloss']);
          if (this.TradePnLByDates[key]['profitloss'] <0) {
            this.barChartColors[0].backgroundColor.push('red');
          }else{
            this.barChartColors[0].backgroundColor.push('green');
          }
        });
          this.barChartData = this.clone;  
      }

      
    );
      /* alert(this.barChartData[0].data);
      alert(this.barChartLabels); */

  }

}

}
