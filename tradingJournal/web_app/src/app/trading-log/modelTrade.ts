/* import { DatePipe } from '@angular/common'; */
export class ModelLog{
    public now: Date = new Date();
    
    constructor(             
              public trade_num: number = 0.00,
              public tradedate:  String = new Date().toISOString().split('T')[0],
              public scriptname: string = '',
              public efilename: string ='',
              public exfilename: string = '',
              public papertrade: boolean= false,
              public nifty: string = 'None',
              public sector: string = 'None',
              public quantity: number = 0,
              public entryprice: number = 0.00,
              public slprice:number = 0.00,
              public entrytime: string = (new Date().toLocaleTimeString()).replace(/:/g,"_")
                                            .replace(/\s+/g, '_'),
              public entryreason: string = '',
              public exitprice : number = 0.00,
              public exittime: string = (new Date().toLocaleTimeString()).replace(/:/g,"_")
                                        .replace(/\s+/g, '_'),
              public exitreason: string = 'NONE',
              public tradetype:string= '',
              public riskreward: string = '0R',
              public profitloss: number = 0.00,
              public mistakeslearning: string = 'My learnings from this trade.',
              public capital: number = 10000.00
    ){}


}