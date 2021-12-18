import csv
import os
import pandas as pd
import numpy as np
##import indicatorsData
##import Doji
##import getPrice
##import longBody
##import getTrend
import logging
from datetime import datetime, timedelta
import matplotlib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib import dates, ticker
from datetime import datetime , timedelta
from mpl_finance import candlestick_ohlc
matplotlib.use('TkAgg')
##from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
style.use('ggplot')
'''
Too High/Low RSI on 5 min candle and
last candle: Very long and more than double average volume for that day.
Basically I need to find out GREED BUYING...
last 5 min body twice that of wicks

'''


try:
    stocksAll = []
####    logging.basicConfig(level=logging.ERROR)
##    time_log = datetime.now().strftime('MILLION_%H_%M_%d_%m_%Y.log')
##    logging.basicConfig(filename = time_log ,level=logging.INFO)
    def save_fig(df_stock_5min_temp, filename):
        df_stock_5min_temp['TIMESTR'] = [str(i).replace('9', '09') for i in df_stock_5min_temp['TIME'].values]  
        df_stock_5min_temp['TIME_'] = [str(i)[:2] + ':' + str(i)[2:] for i in df_stock_5min_temp['TIMESTR'].values]
        df_stock_5min_temp['DATETIME'] = df_stock_5min_temp['DATE'].map(str) + ' '+df_stock_5min_temp['TIME_']
        df_stock_5min_temp['DATETIME'] = pd.to_datetime(df_stock_5min_temp['DATETIME'])

        df_stock_5min_temp["dateCopy"] = df_stock_5min_temp['DATETIME']
        df_stock_5min_temp["MPLDates"] = df_stock_5min_temp["dateCopy"].apply(lambda date: mdates.date2num(date.to_pydatetime()))
        del df_stock_5min_temp["dateCopy"]
        ##                        print(df_stock_5min_temp)
        allDates = df_stock_5min_temp["MPLDates"].tolist()
        dates1 = np.asarray(allDates)
        ##        print(dates)
        ##        quotes = quotes.astype(float)

        Volume = df_stock_5min_temp['TIME'].apply(float).tolist()

        volume = np.asarray(Volume)
        ##    ax = plt.subplots()
        ax = plt.subplot2grid((6,4), (0,0), rowspan = 5, colspan = 4)
        av = plt.subplot2grid((6,4), (5,0), rowspan = 1, colspan = 4, sharex = ax)
        av.fill_between(allDates, 0, volume,facecolor='green', alpha=0.5)
        ##        av.bar(allDates,volume,align='center')
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y %H:%M'))
        ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
        candlestick_ohlc(ax, df_stock_5min_temp[["MPLDates","OPEN","HIGH","LOW","CLOSE"]].values, width = 0.5 , colorup = 'g', colordown = 'r', alpha = 0.8)
        ax.xaxis_date()
        ax.autoscale_view()
        ##        plt.setp(av.get_xticklabels(), rotation=45, horizontalalignment='right')
        plt.setp(ax.get_xticklabels(), visible = False) ## this removes x - axis
        plt.setp(av.get_xticklabels(), visible = False)

        ##        plt.subplots_adjust(hspace=.0)
        plt.tight_layout()                                                
##        plt.show()
        plt.savefig('figure/{}'.format(filename), bbox_inches='tight')

    def record_winLoss(nrdf,check_df,symbol):
        global NRfound, win, loss
        nro = float(nrdf['OPEN'].values)
        nrc = float(nrdf['CLOSE'].values)
        nrh = float(nrdf['HIGH'].values)
        nrl = float(nrdf['LOW'].values)

        chko = float(check_df['OPEN'].values)
        chkc = float(check_df['CLOSE'].values)
        chkh = float(check_df['HIGH'].values)
        chkl = float(check_df['LOW'].values)

        if (chkl > nrl and chkh > nrh) or (chkh < nrh and chkl < nrl):
            print('Win on',check_df['DATE'].values, 'for', symbol )
            win += 1
        else:
            print('Loss on',check_df['DATE'].values,  'for', symbol )        
            loss += 1
    

    def calculate_rsi_df(df_stock,rsi_period):
        delta = df_stock['CLOSE'].diff()
        dUp, dDown = delta.copy(), delta.copy()
        dUp[dUp < 0] = 0
        dDown[dDown > 0] = 0
        RolUp = pd.rolling_mean(dUp, rsi_period)
        RolDown = pd.rolling_mean(dDown,rsi_period).abs()
        RS = RolUp / RolDown
        rsi= 100.0 - (100.0 / (1.0 + RS))
        df_stock['RSI'] = rsi
##        return df_stock['RSI'].tail(1).values   
        return df_stock
        
    def NR_BACKTST(companies, days):
        global NRfound, win, loss
        for symbol in companies:
            df_stock = pd.read_csv('../SYMBOL/STOCK_{}.csv'.format(symbol))
##            df_stock = calculate_rsi_df(df_stock,14)
##            for i in [50,20,9]:
##               df_stock['MA{}'.format(i)] =  df_stock['CLOSE'].rolling(window=i).mean()

##            print(df_stock.tail(5))   
            df_stock['RANGE'] = df_stock['HIGH'] - df_stock['LOW']
            for i in range(0,days):
                check_df = df_stock.tail(1)
##                print(check_df)
                df_stock.drop(df_stock.tail(1).index,inplace=True)
                stockdf = df_stock.tail(21) ##NR21 NR7

                NRdf = df_stock.tail(1)
                stockdf.drop(stockdf.tail(1).index,inplace=True)

##                print(NRdf)
                            
##                stockdf.drop(stockdf.tail(1).index,inplace=True)
                sixRange = stockdf['RANGE'].values
    ##            print(sixRange)
                if all(i > NRdf['RANGE'].values for i in sixRange) and stockdf['HIGH'].tail(1).values > NRdf['HIGH'].values and\
                   stockdf['LOW'].tail(1).values < NRdf['LOW'].values:
                    
##                    print('NR candle found on',NRdf['DATE'].values,' for', symbol )
                    print(symbol,NRdf['DATE'].values)
##                    NRfound += 1
##                    record_winLoss(NRdf, check_df,symbol)

##                print('---------------------------------------')
                


    def get_ob_os_stocks(companies, flg = True):
        if flg == True:            
            ob = []
            os = []
            for symbol in companies:
                df_stock = pd.read_csv('../SYMBOL/STOCK_{}.csv'.format(symbol))
                df_stock = calculate_rsi_df(df_stock,9)
                if df_stock.tail(1)['RSI'].values > 80:
                    ob.append(symbol)
                elif df_stock.tail(1)['RSI'].values < 20:
                    os.append(symbol)
            print('OVERBOUGHT LIST = ', ob)                
            print('OVERSOLD LIST = ', os)
        else:
            ob = []
            os = []
            for symbol in companies:
                df_stock = pd.read_csv('../SYMBOL/STOCK_{}.csv'.format(symbol))
                df_stock = calculate_rsi_df(df_stock,9)
                if df_stock.tail(1)['RSI'].values > 75:
                    ob.append(symbol)
                elif df_stock.tail(1)['RSI'].values <= 25:
                    os.append(symbol)
            print('UP LIST = ', len(ob))
            print('DOWN LIST = ', len(os))
            

    def get_3IIIB_stocks(companies, flg = True):
        global stocksAll
        _IIIB = []
        for symbol in companies:
            df_stock = pd.read_csv('../SYMBOL/STOCK_{}.csv'.format(symbol))
            df_lastThree = df_stock.tail(3)
##            print(df_lastThree.iloc[0]['HIGH'])
            if df_lastThree.iloc[0]['HIGH'] > df_lastThree.iloc[1]['HIGH']\
               and df_lastThree.iloc[0]['LOW'] < df_lastThree.iloc[1]['LOW']\
               and df_lastThree.iloc[1]['HIGH'] > df_lastThree.iloc[2]['HIGH']\
               and df_lastThree.iloc[1]['LOW'] < df_lastThree.iloc[2]['LOW']:
                _IIIB.append(symbol)
        print('3 INSIDE BARS,', _IIIB)            

    def get_DMA_stocks(companies, flg = True):
        global stocksAll
        if flg == True:            
            _DMA50 = []
            _DMA100 = []
            for symbol in companies:
                df_stock = pd.read_csv('../SYMBOL/STOCK_{}.csv'.format(symbol))
                for i in [100,50]:
                    df_stock['MA{}'.format(i)] =  df_stock['CLOSE'].rolling(window=i).mean()

                closep = df_stock.tail(1)['CLOSE'].values
                ma100 = df_stock.tail(1)['MA100'].values
                ma50 = df_stock.tail(1)['MA50'].values

                UL = closep + ((closep * (1))/100)
                LL = closep - ((closep * (1))/100)
                if ma100 > LL and ma100 < UL:
                    _DMA100.append(symbol)
                if ma50 > LL and ma50 < UL:
                    _DMA50.append(symbol)
            print('STOCK NEAR 5ODMA', _DMA50)                
            print('STOCK NEAR 100DMA', _DMA100)
        else:           
            bullish = []
            bearish = []
            _j = 5
            for symbol in companies:
                df_stock = pd.read_csv('../SYMBOL/STOCK_{}.csv'.format(symbol))
                for i in [_j]:
                    df_stock['MA'] =  df_stock['CLOSE'].rolling(window=i).mean()
                closep = df_stock.tail(1)['CLOSE'].values
                ma = df_stock.tail(1)['MA'].values               
                if closep > ma:
                    bullish.append(symbol)
                elif closep < ma:
                    bearish.append(symbol)
            print('MA UP list', len(bullish))                
            print('MA DOWN list',len(bearish))            
        
    def get_NR_list(companies, day):
        global stocksAll        
        NR = []        
        for symbol in companies:
            stockdf = pd.DataFrame()
            df_stock = pd.read_csv('../SYMBOL/STOCK_{}.csv'.format(symbol))
            stockdf = df_stock.tail(day)
            ## get aVERAGE Volume for todays
            stockdf['RANGE'] = stockdf['HIGH'] - stockdf['LOW']
            lastdaydf = stockdf.tail(1)            
            stockdf.drop(stockdf.tail(1).index,inplace=True)
            sixRange = stockdf['RANGE'].values
##            print(sixRange)
            if all(i > lastdaydf['RANGE'].values for i in sixRange) and stockdf['HIGH'].tail(1).values > lastdaydf['HIGH'].values and stockdf['LOW'].tail(1).values < lastdaydf['LOW'].values:
                NR.append(symbol) 
        
        return NR          

    def getUPDOWNTrendingStock(companies):
        global stocksAll
        stocks_to_buy=[]
        stocks_to_sell=[]
        for stock in companies:             
            try:
                df_Trendstock = pd.read_csv('../SYMBOL/STOCK_{}.csv'.format(stock))
                df_Trendstock = calculate_rsi_df(df_Trendstock,14)
                for i_ma in [50,20,9,5,3]:
                    df_Trendstock['MA{}'.format(i_ma)] =  df_Trendstock['CLOSE'].rolling(window=i_ma).mean()
                PPDH         = df_Trendstock.tail(3)['HIGH'].values[0]
                PPDL         = df_Trendstock.tail(3)['LOW'].values[0]
                PDH         = df_Trendstock.tail(2)['HIGH'].values[0]
                PDL         = df_Trendstock.tail(2)['LOW'].values[0]
                VOL_PD      = df_Trendstock.tail(2)['VOLUME'].values[0]
                VOL         = df_Trendstock.tail(1)['VOLUME'].values[0]
                MA50        = df_Trendstock.tail(1)['MA50'].values[0]
                MA20        = df_Trendstock.tail(1)['MA20'].values[0]
                MA9         = df_Trendstock.tail(1)['MA9'].values[0]
                MA5         = df_Trendstock.tail(1)['MA5'].values[0]
                MA3         = df_Trendstock.tail(1)['MA5'].values[0]
                close_    = df_Trendstock.tail(1)['CLOSE'].values[0]
                RSI         = df_Trendstock.tail(1)['RSI'].values[0]
                ## PDClose_ > float(MA50) and PDClose_ < float(MA50)and
                if close_ > float(MA9) and  close_ > float(MA5) and close_ > PDH and VOL > VOL_PD: 
                    stocks_to_buy.append(stock)
                elif close_ < float(MA9) and  close_ < float(MA5) and close_ < PDL and VOL > VOL_PD:
                    stocks_to_sell.append(stock)
            except Exception as e:
                print('error ', e)
        print('BUY', stocks_to_buy)
        print('SELL', stocks_to_sell)   

    def getUPDOWNTrendingStockBacktest(companies):
        stocks_to_buy=[]
        stocks_to_sell=[]
        win = 0
        lost = 0
        
        for stock in companies:             
            try:                
                winstk = 0
                loststk = 0
                df_Trendstock = pd.read_csv('../SYMBOL/STOCK_{}.csv'.format(stock))
                #df_Trendstock = calculate_rsi_df(df_Trendstock,14)
                
                for i_ma in [50,20,9,5]:
                    df_Trendstock['MA{}'.format(i_ma)] =  df_Trendstock['CLOSE'].rolling(window=i_ma).mean()
                df_Trendstock = df_Trendstock.dropna()
                for i in range(0,  len(df_Trendstock.index)-3):
                    df_ = df_Trendstock.iloc[i:i+3]
                    #df_['TIME'] = ['915','920','925']
                    PDH         = float(df_.iloc[0]['HIGH'])
                    PDL         = float(df_.iloc[0]['LOW'])
                    PDCLOSE     = float(df_.iloc[0]['CLOSE'])
                    MA50PD      = float(df_.iloc[0]['MA50'])
                    MA5PD      = float(df_.iloc[0]['MA5'])
                    MA9PD      = float(df_.iloc[0]['MA9'])
                    MA20PD      = float(df_.iloc[0]['MA20'])
                    VOL_PD      = float(df_.iloc[0]['VOLUME'])
                    VOL         = float(df_.iloc[1]['VOLUME'])
                    MA50        = float(df_.iloc[1]['MA50'])
                    MA5        = float(df_.iloc[1]['MA5'])
                    MA20        = float(df_.iloc[1]['MA20'])
                    MA9         = float(df_.iloc[1]['MA9'])
                    close_      = float(df_.iloc[1]['CLOSE'])
                    low_      = float(df_.iloc[1]['LOW'])
                    high_      = float(df_.iloc[1]['HIGH'])
                    #RSI         = float(df_.iloc[1]['RSI'])
                    open_chk    = float(df_.iloc[2]['OPEN'])
                    close_chk    = float(df_.iloc[2]['CLOSE'])
                    high_chk    = float(df_.iloc[2]['HIGH'])
                    low_chk    = float(df_.iloc[2]['LOW'])
                    ## PDClose_ > float(MA50) and PDClose_ < float(MA50)and
                    if close_ > MA5 and close_ > MA9 and close_ > PDH:
                        if low_chk > low_ and close_chk > close_:
                            winstk +=1
                        elif low_chk < low_:
                            loststk += 1
                        #save_fig(df_,'long_{}_{}.png'.format(stock,df_.iloc[1]['DATE']))
                        
                        #stocks_to_buy.append(stock)
                    elif close_ < MA5 and close_ < MA9 and close_ < PDL:
                        if high_chk < high_ and close_chk > close_:
                            winstk += 1
                        elif high_chk > high_:
                            loststk +=1
                        #save_fig(df_,'short{}_{}.png'.format(stock,df_.iloc[1]['DATE']))
                        #stocks_to_sell.append(stock)
                win = win + winstk
                lost = lost + loststk
                print('{} win:{} lost:{} totalTrades {}'.format(stock, winstk, loststk, int(winstk+ loststk)))
            except Exception as e:
                print('error ', e)
        print('total trades:{}, win:{}, lost:{}'.format(int(win+lost), win, lost))                
##        print('BUY', stocks_to_buy)
##        print('SELL', stocks_to_sell)         

            
##--------------------------------------------------------------##    
    with open('EQUITY STOCKS.csv') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')
        companies = []      
        for row in readcsv:
            comp = row[0]
            companies.append(comp)

##    print('GETTING NR STOCKS')   
##    print('NR7',get_NR_list(companies,7))
##    print('NR21',get_NR_list(companies,21))
##    get_ob_os_stocks(companies)
##    get_3IIIB_stocks(companies)
##    get_DMA_stocks(companies)
##        
##    
##    print('')
##    print('')
##    print('Getting Bullish/bearish List for probable next day move.')
##    get_ob_os_stocks(companies, False)
##    get_DMA_stocks(companies, False)

    print('----------------------')
    print('-----------GETTING DAILY UP DOWN TRENDING-----------')
    getUPDOWNTrendingStock(companies)
    
    
except Exception as e:
        print(e)    

    

    


        
        
