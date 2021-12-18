import { Component, OnInit, Input, OnChanges,SimpleChanges,SimpleChange } from '@angular/core';
import {ModelLog} from '../../trading-log/modelTrade';
/* import { DomSanitizer } from '@angular/platform-browser'; */
/* import {MatDialog} from '@angular/material';
import { TradingLogComponent } from '../../trading-log/trading-log.component';
 */

@Component({
  selector: 'app-trade-detail',
  templateUrl: './trade-detail.component.html',
  styleUrls: ['./trade-detail.component.css']
})
export class TradeDetailComponent implements OnInit, OnChanges {
  @Input() data: ModelLog;

  papar_Flag :boolean = false;
  _url: any = '/assets/Trades_snap/'; 
  //_url_swing: any = '/assets/Trades_snap/'; 
  entrysnapurl:any = '';
  exitsnapurl:any = '';
  entryflag :boolean = true;
  exitflag:boolean  =  true;
  constructor() {
   /*  console.log('hwew '+this.data.efilename); */
   /*  console.log(this.data.efilename); */
   }

   ngOnChanges(changes: SimpleChanges) {
    /* const tradenew: SimpleChange = changes.data;
     console.log('tradenew:'+tradenew); */
      for (let propName in changes) {
      /* console.log(changes[propName].currentValue.efilename); */
        this.papar_Flag = changes[propName].currentValue.papertrade;

        if (changes[propName].currentValue.efilename !='NONE' && changes[propName].currentValue.efilename !=null){
          this.entryflag = false;
          this.entrysnapurl = this._url + changes[propName].currentValue.efilename; 
        }else{
          this.entryflag = true;
        }
        if (changes[propName].currentValue.exfilename !='NONE' && changes[propName].currentValue.exfilename !=null){
          this.exitflag = false;
          this.exitsnapurl = this._url + changes[propName].currentValue.exfilename; 
        }else{
          this.exitflag = true;
        }

     } 
  }

  

  ngOnInit() {
       
    //URL_ENTRY : String = 'D:\\Project\\Angular\\python\\FileUploads\\'+this.data.efilename; 
  }

}
