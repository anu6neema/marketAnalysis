export class TradeData{
    //public now: Date = new Date();    
    constructor(             
              public TOTALPNL: number = 0,
              public TOTALTRADES:  number = 0,
              public WINS: number = 0,
              public LOST: number = 0,
              public ACCURACY: number = 0,
              public AVERAGE_WIN_RR: number = 0              
    ){}


}

export class Trade_pnl_by_date{
    //public now: Date = new Date();    
    constructor(             
              public profitloss: number = 0,
              public tradedate_str:  string = ''
                      
    ){}


}