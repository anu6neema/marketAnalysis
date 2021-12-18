import { Component, OnInit ,Inject, ViewChild } from '@angular/core';
import {ModelLog} from './modelTrade';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material';
import { TradeLogDialogComponent } from '../trade-log-dialog/trade-log-dialog.component';
import {PythonDataService} from '../services/python-data.service';
/* import {MatSnackBar} from '@angular/material'; */
/* import { DatePipe } from '@angular/common'; */

@Component({
  selector: 'app-trading-log',
  templateUrl: './trading-log.component.html',
  styleUrls: ['./trading-log.component.css']
})
export class TradingLogComponent implements OnInit {

  constructor(public dialogRef: MatDialogRef<TradeLogDialogComponent>, private _pyservice:PythonDataService,
    @Inject(MAT_DIALOG_DATA) public data: any) { }
  model: ModelLog = new ModelLog ();
  data_len: number = 0;
  isSubmitted:boolean = true;
  paperTrade:boolean = this.data.paperflag;
  ToggleValue : string= this.data.toggleValue;
  
  modelEdit : ModelLog= this.data.editModel;
  abs_tgt: number = 0;
  abs_sl: number = 0;
  risk_per_trade: number = 1;  
  risk_tgt: number = 3;  

  ngOnInit() {
    if (this.modelEdit) {     
      this.model = this.modelEdit;
      console.log('this.model.efilename :'+this.model.efilename);
      this.isSubmitted = true;
    }
    else {
      this.data_len = this.data.datalength + 1;
      if (this.data_len > 1) {
        this.model.papertrade = this.paperTrade;
        this.model.trade_num  = this.data_len;
        this.isSubmitted = true;
      } 
    }       
  }
  entryFile: File = null;
  exitFile: File = null;
  
  @ViewChild("logForm") form: any;
  riskp :any = 0;

  Get_absolute_values(){
    var slprice = +this.model.slprice;
    var entry = +this.model.entryprice;
    var exit = +this.model.exitprice;

    if(slprice > 0 && ((entry > 0) || (exit > 0))){
        var riskamount  = (+this.model.capital * this.risk_per_trade)/100;
        if (entry > 0 && exit === 0){
          this.model.quantity = Math.round(riskamount/Math.abs(entry-slprice));
          this.abs_tgt = Math.round((Math.abs(entry - (entry - (riskamount*this.risk_tgt)/this.model.quantity))) * 100) / 100;
          this.abs_sl = Math.round((entry - slprice) * 100) / 100;

        }else if (exit > 0 && entry === 0) {
          this.model.quantity = Math.round(riskamount/Math.abs(exit-slprice));
          this.abs_tgt = Math.round((Math.abs(exit - (exit - (riskamount*this.risk_tgt)/this.model.quantity))) * 100) / 100;
          this.abs_sl = Math.round((slprice - exit) * 100) / 100;
        }        
    }

  }
  
  onSelectEntryFile(event) {
    if (event.target.files && event.target.files[0]) {
      this.entryFile = event.target.files[0]; // read file as data url
      console.log(this.entryFile);
    }
  }

  onSelectExitFile(event) {    
    if (event.target.files && event.target.files[0]) {
      this.exitFile = event.target.files[0]; // read file as data url
      console.log(this.exitFile);
    }
  }

  CalculateRisk() {
    /* console.log('car risk called'); */
    if((+this.model.slprice) !=0){
      if ((+this.model.slprice) > (+this.model.exitprice) && (+this.model.exitprice)!=0) {// short
        this.riskp = +this.model.quantity * Math.abs((+this.model.slprice) - (+this.model.exitprice));
        this.model.tradetype= "SHORT";
      }else if ((+this.model.entryprice) > (+this.model.slprice) && (+this.model.entryprice)!= 0) { // long
        this.riskp = +this.model.quantity * Math.abs((+this.model.entryprice) - (+this.model.slprice));
        this.model.tradetype= "LONG";
      }
    } 
   
  }
  
  CalculateRR(){
    this.CalculateRisk();
   /*  console.log('rr called'); */
/*     console.log((+this.model.exitprice));
    console.log((+this.model.entryprice));
    console.log((+this.model.quantity));
 */
    if ((+this.model.exitprice) != 0 && (+this.model.entryprice)!=0
      && (+this.model.quantity) !=0) {        
        var profitnloss = ((+this.model.exitprice) - (+this.model.entryprice)) * (+this.model.quantity);
        this.model.profitloss =  Math.round(((profitnloss)) * 100) / 100;
        this.model.riskreward = Math.round(((this.model.profitloss/this.riskp)) * 100) / 100 +'R';

        /* if (+this.model.entryprice < +this.model.exitprice){ // in case of profits
         //var reward = Math.abs((+this.model.exitprice) - (+this.model.entryprice)) * +this.model.quantity;
          this.model.riskreward = Math.round(((profitnloss/this.riskp)) * 100) / 100 +'R';
          console.log('this.model.riskreward '+ this.model.riskreward);
        }else {
          this.model.riskreward = Math.round(((this.model.profitloss/this.riskp)) * 100) / 100 +'R';
        } */
    }
    
  }  

  resetform(){
    this.form.reset();
  }

  onSubmit() {
    if (this.form.valid) {
      
      const formData = new FormData();
     /*  var tmp_files :File[] = [] ; */
      if (this.entryFile !=  null){
       /*  tmp_files.push(this.entryFile); */
         var filenamee = 'entry'+'_'+this.model.scriptname+'_'+this.model.tradedate+'_'+this.model.entrytime+'.jpg';
        formData.append('entryfile', this.entryFile,filenamee); 
      }
      if (this.exitFile !=  null){
       /*  tmp_files.push(this.entryFile); */
         var filenameex = 'exit'+'_'+this.model.scriptname+'_'+this.model.tradedate+'_'+this.model.exittime+'.jpg';
        formData.append('exitfile', this.exitFile,filenameex); 
      }

      /* console.log(tmp_files); */
      Object.keys(this.model).forEach(key => {
        console.log(key+ '::'+this.model[key]);
        formData.append(key, this.model[key]); 
      });   
      //alert(this.ToggleValue);
      if (this.ToggleValue == "INTRADAY") {
        this._pyservice.saveTrade('http://127.0.0.1:5002/savefile',formData).subscribe((res) => {
          if (res.status === 201){
            console.log('ADDED');
            this.isSubmitted = false;       
          }
        }); 
      }else if (this.ToggleValue == "SWING-FNO") {
        this._pyservice.saveTrade('http://127.0.0.1:5002/savefile_swing',formData).subscribe((res) => {
          if (res.status === 201){
            console.log('ADDED');
            this.isSubmitted = false;       
          }
        }); 
      }
      else if (this.ToggleValue == "POSITIONAL-CASH") {

      }
      
      /*  this.form.reset(); */
    }
  }
}
