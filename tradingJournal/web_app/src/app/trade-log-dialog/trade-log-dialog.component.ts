import {Component,Inject,OnInit} from '@angular/core';
import {MatDialog} from '@angular/material';
import {ModelLog} from '../trading-log/modelTrade';
import { TradingLogComponent } from '../trading-log/trading-log.component';
import {PythonDataService} from '../services/python-data.service';

@Component({
  selector: 'app-trade-log-dialog',
  templateUrl: './trade-log-dialog.component.html',
  styleUrls: ['./trade-log-dialog.component.css']
})
export class TradeLogDialogComponent implements OnInit {
  
  selectedVal : string='INTRADAY'; 
  paperFlag: boolean = false;
  data_l: any= 0;
  selectedRow : Number;
  public TradeLogs:Array<ModelLog> = [];
  model_trade : ModelLog;
  model_trade_edit : ModelLog;
  constructor(public dialog: MatDialog,private _pyservice:PythonDataService) { }

  Toggle_change(val: string) {
    //alert(this.selectedVal);// CALL SERVICES.
    this.selectedVal = val;
    this.TradeLogs = [];
    this._pyservice.getDataObservable(this.paperFlag,this.selectedVal).subscribe(
      data => {
        /* console.log(data); */
         for (let key in data) {
          this.TradeLogs.push(data[key]);
        } 
         this.data_l = this.TradeLogs.length; 
         this.model_trade = this.TradeLogs[0]; 
         /* console.log('this.TradeLogs:'+  this.TradeLogs.length);  */       
      }
    ); 
    
  }
  getTradeDetails(_index) {
    this.model_trade = this.TradeLogs[_index];
    this.selectedRow = _index;
  }

  EditTradeDetails(_index): void {
    this.model_trade_edit = this.TradeLogs[_index];
    this.model_trade_edit.papertrade = this.paperFlag;
    const dialogRef = this.dialog.open(TradingLogComponent, { 
      width: '100%',  
      position:{top:'6%' },
      data: { datalength: this.data_l, paperflag : this.paperFlag, editModel: this.model_trade_edit, toggleValue: this.selectedVal }
    });

    dialogRef.afterClosed().subscribe(result => {
      this.TradeLogs = [];
      console.log('The dialog was closed');
      this._pyservice.getDataObservable(this.paperFlag, this.selectedVal).subscribe(
      data => {
        /* console.log(data); */
         for (let key in data) {
          this.TradeLogs.push(data[key]);
        } 
         this.data_l = this.TradeLogs.length;
         this.model_trade = this.TradeLogs[0];
      }
    );
    });
  }

  GetPaperTrdes(_paperflag) {
    this.paperFlag = _paperflag;
    this.TradeLogs = [];
    this._pyservice.getDataObservable(_paperflag,this.selectedVal).subscribe(
      data => {
        /* console.log(data); */
         for (let key in data) {
          this.TradeLogs.push(data[key]);
        } 
         this.data_l = this.TradeLogs.length; 
         this.model_trade = this.TradeLogs[0];         
      }
    );
  }

  ngOnInit() {
    /* var k = '{"0":{"entryprice":100,"entryreason":32434,"entrytime":324,"exitprice":110,"exitreason":324,"exittime":34,"mistakeslearning":null,"nifty":"RED","profitloss":6230,"quantity":623,"riskreward":"2R","scriptname":"TCS","sector":"UP","slprice":95,"tradedate":"2018-11-10"},"1":{"entryprice":100,"entryreason":32434,"entrytime":324,"exitprice":110,"exitreason":324,"exittime":34,"mistakeslearning":null,"nifty":"RED","profitloss":6230,"quantity":623,"riskreward":"2R","scriptname":"TCS","sector":"UP","slprice":95,"tradedate":"2018-11-10"},"2":{"entryprice":100,"entryreason":32434,"entrytime":324,"exitprice":110,"exitreason":324,"exittime":34,"mistakeslearning":null,"nifty":"RED","profitloss":6230,"quantity":623,"riskreward":"2R","scriptname":"ICICIB","sector":"UP","slprice":95,"tradedate":"2018-11-11"},"3":{"entryprice":100,"entryreason":32434,"entrytime":324,"exitprice":110,"exitreason":324,"exittime":34,"mistakeslearning":null,"nifty":"RED","profitloss":6230,"quantity":623,"riskreward":"2R","scriptname":"ICICIB","sector":"UP","slprice":95,"tradedate":"2018-11-11"}}';
    console.log(JSON.parse(k)); */

    this._pyservice.getDataObservable(this.paperFlag,this.selectedVal).subscribe(
      data => {
        /* console.log(data); */
         for (let key in data) {
          this.TradeLogs.push(data[key]);
        } 
         this.data_l = this.TradeLogs.length; 
         this.model_trade = this.TradeLogs[0];         
      }
    ); 

  
  }
  openDialog(): void {
    const dialogRef = this.dialog.open(TradingLogComponent, { 
      width: '100%', 
      position:{top:'6%' },
      data: { datalength: this.data_l, paperflag : this.paperFlag, toggleValue: this.selectedVal  }
    });

    dialogRef.afterClosed().subscribe(result => {
      this.TradeLogs = [];
      console.log('The dialog was closed');
      this._pyservice.getDataObservable(this.paperFlag, this.selectedVal).subscribe(
      data => {
        /* console.log(data); */
         for (let key in data) {
          this.TradeLogs.push(data[key]);
        } 
         this.data_l = this.TradeLogs.length;
         this.model_trade = this.TradeLogs[0];
      }
    );
    });
  }



}
