import { Injectable } from '@angular/core';
import 'rxjs/add/operator/map';
import { HttpClient } from '@angular/common/http'; 


@Injectable()
export class PythonDataService {
  
  constructor(private _http:HttpClient) { }

  url : string = ''
  getDataObservable(paper_trade: boolean,ToggleValue: string) {  
    if (ToggleValue=='INTRADAY'){
      if (paper_trade) {
        this.url = 'http://127.0.0.1:5002/tradespaper';
      }else {
        this.url = 'http://127.0.0.1:5002/trades';
      }
    }
    else if (ToggleValue == 'POSITIONAL-CASH') {
      if (paper_trade) {
        this.url = 'http://127.0.0.1:5002/tradespaperpositional';
      }else {
        this.url = 'http://127.0.0.1:5002/trades_positional';
      }
    }
    else if (ToggleValue == 'SWING-FNO'){
      if (paper_trade) {
        this.url = 'http://127.0.0.1:5002/tradespaperswing';
      }else {
        this.url = 'http://127.0.0.1:5002/trades_swing';
      }
    }
    return this._http.get(this.url)
    .map(data => {    
        return JSON.parse(data.toString());
    }); 
  }


  saveTrade(url:string, data:any) {
    return this._http.post(url, data, {observe: 'response'})
  };

  getDataAnalysis(paper_trade: boolean, startdate:string, enddate:string) {
    if (paper_trade) {
      this.url = 'http://127.0.0.1:5002/getTradesData'+ '?startdate='+startdate+'&enddate='+enddate;
    }else {
      this.url = 'http://127.0.0.1:5002/getTradesData'+'?startdate='+startdate+'&enddate='+enddate;// change here for actual trades
    }
    return this._http.get(this.url)
    .map(data => {    
        return JSON.parse(data.toString());
    }); 
  }

  TradeDataforDates(paper_trade: boolean, startdate:string, enddate:string) {
    if (paper_trade) {
      this.url = 'http://127.0.0.1:5002/getChartingData'+ '?startdate='+startdate+'&enddate='+enddate;
    }else {
      this.url = 'http://127.0.0.1:5002/getChartingData'+'?startdate='+startdate+'&enddate='+enddate;// change here for actual trades
    }
    return this._http.get(this.url)
    .map(data => {    
        return JSON.parse(data.toString());
    }); 
  } 
}
  

