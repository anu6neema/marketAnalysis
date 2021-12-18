import tkinter as tk
from tkinter import ttk
import time
import csv
import matplotlib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import dates, ticker
from matplotlib.dates import DateFormatter
from datetime import datetime , timedelta
from mpl_finance import candlestick_ohlc
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
style.use('ggplot')
import urllib
import json
import threading
import os, glob
from random import randint

f = plt.figure()
##ax = f.add_subplot(111)
LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)
##resampleSize = "15Min"
##DataPace = "1d"
##candleWidth = 0.008
chartLoad = False
loadStockData = False
liveDataTrade = False
nextBar = False
main_df = pd.DataFrame()
db_bkp = pd.DataFrame()

ltp_price = 0.00
sell_p = 0.00
buy_p = 0.00
profit_loss = 0.00
quantity = 0
timeCount = 0
date_traded = "20210101"
##df_nifty = pd.read_csv('DATA/STOCK_{}_5_MIN.csv'.format("NIFTY"), dtype=str)
df_nifty = pd.read_csv('STOCK_{}_5_MIN.csv'.format("NIFTY"), dtype=str)
df_test1  = df_nifty[df_nifty['DATE'] == date_traded]
timelist = pd.unique(df_test1['TIME'].values).tolist()
DateList = pd.unique(df_nifty['DATE'].values).tolist()

df_nifty_daily = pd.read_csv('nifty_ohlc_pivots.csv')
df_nifty_daily['DATE_1'] = pd.to_datetime(df_nifty_daily['Date'], format='%d-%b-%Y')
df_nifty_daily['DATE_1'] = df_nifty_daily['DATE_1'].dt.strftime('%Y%m%d')

dfForDate = df_nifty_daily[df_nifty_daily['DATE_1'] == df_test1['DATE'].values[0]]

def deleteIntradayFile():    
    if os.path.exists('intraday5min.csv'):
        os.remove('intraday5min.csv')
        
""" 
def getRandomStock():
    global chartLoad, loadStockData, liveDataTrade, stockSelected, main_df, db_bkp, ltp_price, sell_p, buy_p, profit_loss, quantity
    main_df = pd.DataFrame()
    db_bkp = pd.DataFrame()
    chartLoad = False
    loadStockData = False
    liveDataTrade = False
    files = glob.glob('data/*')
    for f in files:
        os.remove(f)

    with open('INDEX_FO.csv') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')
        companies = []      
        for row in readcsv:
            comp = row[0]
            companies.append(comp)
    listindex = randint(0, len(companies))
    print(listindex)


    
    chartLoad = True
    # get list of stocks.
    # select a random number
    # assign it to stockSelected
    # stop global loadStockData
    # global liveDataTrade
    # clear directory
    # turn on flag  """

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title('!')
    label = ttk.Label(popup, text = msg, font = NORM_FONT)
    label.pack(side ='top', fill = 'x', pady = 10)
    B1 = ttk.Button(popup, text = 'OK',command = popup.destroy)
    B1.pack()
    popup.mainloop()

""" def unix_to_datetime(date_index):
        return datetime.fromtimestamp(
            int(date_index)
        ).strftime('%Y-%m-%d %H:%M:%S')
    
def get_all_prices_combined(interval,stocks, tf):        
        main_close = pd.DataFrame()
        main_open = pd.DataFrame()
        main_high = pd.DataFrame()
        main_low = pd.DataFrame()
        main_vol = pd.DataFrame()
        for eachsymbol in stocks:
##            print(eachsymbol)
            df2 = pd.read_csv('{}/STOCK_{}.csv'.format(interval,eachsymbol),skiprows = 7, header=None)
##            print(2)
            df2.columns = ['DATE','CLOSE','HIGH','LOW','OPEN','VOLUME']
##            print(3)
            indexList = df2['DATE']
##            print(4)
            start_unix_index = indexList[0].replace('a', '')
            new_index_main = [unix_to_datetime(start_unix_index)]
            new_index_1 = [unix_to_datetime( int(start_unix_index)  + tf * int(i.replace('a', '')))  for i in indexList if i!= 'a'+start_unix_index]
            new_index_main.extend(new_index_1)
##            print(5)
            se = pd.Series(new_index_main)
##            print(6)
            df2['DATE'] = se.values
##            print(7)
            df2.set_index('DATE', inplace  = True)
            
            df_close = df2.copy()
            df_open = df2.copy()
            df_high = df2.copy()
            df_low = df2.copy()
            df_vol = df2.copy()
            
            df_close.rename(columns={'CLOSE': eachsymbol}, inplace=True)
            df_close.drop(['OPEN', 'HIGH', 'LOW', 'VOLUME'], 1, inplace=True)

            df_open.rename(columns={'OPEN': eachsymbol}, inplace=True)
            df_open.drop(['CLOSE', 'HIGH', 'LOW', 'VOLUME'], 1, inplace=True)

            df_high.rename(columns={'HIGH': eachsymbol}, inplace=True)
            df_high.drop(['OPEN', 'CLOSE', 'LOW', 'VOLUME'], 1, inplace=True)
            
            df_low.rename(columns={'LOW': eachsymbol}, inplace=True)
            df_low.drop(['OPEN', 'HIGH', 'CLOSE', 'VOLUME'], 1, inplace=True)
            
            df_vol.rename(columns={'VOLUME': eachsymbol}, inplace=True)
            df_vol.drop(['OPEN', 'HIGH', 'CLOSE', 'LOW'], 1, inplace=True)
                 
            if main_close.empty:
                main_close = df_close
            else:
                main_close = main_close.join(df_close, how='outer')

            if main_open.empty:
                main_open = df_open
            else:
                main_open = main_open.join(df_open, how='outer')

            if main_high.empty:
                main_high = df_high
            else:
                main_high = main_high.join(df_high, how='outer')

            if main_low.empty:
                main_low = df_low
            else:
                main_low = main_low.join(df_low, how='outer')

            if main_low.empty:
                main_vol = df_vol
            else:
                main_vol = main_vol.join(df_vol, how='outer')                
        return main_close, main_open, main_high, main_low, main_vol

def FetchPrices(companies, timef, day):        
        for eachsymbol in companies:
            print(eachsymbol)
            #SavePrice.save_price_details(eachsymbol,str(timef),str(day))

def FETCHnGETprices (companies , tf, days, Apiflag = 'FALSE'):
        if tf == 86400:
            folder = '1_DAY'
        elif tf == 60:
            folder = '60_SEC'
        elif tf == 300:
            folder = '5_MIN'            
        if Apiflag == 'TRUE':
            FetchPrices(companies,tf,days)
        return get_all_prices_combined(folder,companies, tf)    

def saveDf(companies, closedf, opendf, highdf, lowdf, voldf):
    global ltp_price, profit_loss, sell_p, buy_p, quantity
    OverB_today = []
    OverS_today = []
    OverB_yes = []
    OverS_yes = []
    for symbol in companies:
        stockdf = pd.DataFrame()
        stockdf['CLOSE'] = closedf[symbol]
        stockdf['OPEN'] = opendf[symbol]
        stockdf['HIGH'] = highdf[symbol]
        stockdf['LOW'] = lowdf[symbol]
        stockdf['VOLUME'] = voldf[symbol]

        stockdf['DATE_ONLY'] = pd.to_datetime(stockdf.index.values)
        stockdf['ONLY_DATES'] = stockdf['DATE_ONLY'].dt.date
        stockdf.drop(['DATE_ONLY'], 1, inplace=True)                        
        stockdf.to_csv('data/STOCK_{}.csv'.format(symbol)) ## save csv 
        tail1 = stockdf.tail(1)
        ltp_pricelst = (tail1['OPEN'].values + tail1['CLOSE'].values) / 2
        ltp_price = str(round(ltp_pricelst[0], 2)) 
        if buy_p != 0.00 and sell_p !=0.00:
            profit_loss = (float(sell_p) - float(buy_p)) * float(quantity) 
        elif buy_p != 0.00 and sell_p == 0.00: # long
            profit_loss = (float(ltp_price) - float(buy_p)) * float(quantity)
        elif sell_p != 0.00 and buy_p == 0.00: # short
            profit_loss = ( float(sell_p) - float(ltp_price)) * float(quantity)  

def UpdateLiveCsv():
##here just send stock symbol and save/rewrite csv directly to data folder.
    companies = []
    companies.append(stockSelected)
    df_close, df_open, df_high, df_low, df_vol = FETCHnGETprices(companies,300,1,'TRUE')
    saveDf(companies,df_close,df_open,df_high,df_low,df_vol)

def UpdateMainCsv():
    global ltp_price, profit_loss, sell_p, buy_p, quantity
    global main_df, db_bkp
    if main_df.empty:
        db_quote = pd.read_csv('DATABASE/STOCK_{}.csv'.format(stockSelected),
                               index_col=0,
                               parse_dates=True,
                               infer_datetime_format=True)
        main_df  = db_quote[db_quote['ONLY_DATES'] == dateToRun]        
##        main_df['Avg_CO'] = (main_df['OPEN'] + main_df['CLOSE']) / 2
##        print(main_df)
    if db_bkp.empty:
##        main_df.drop(main_df.head(1).index,inplace=True) ## delete blank 9 15 time
        db_bkp = main_df.copy()
        
    head1 = main_df.head(1)
    ltp_pricelst = (head1['OPEN'].values + head1['CLOSE'].values) / 2
    ltp_price = str(round(ltp_pricelst[0], 2)) 
##    print('qty: ', quantity)
##    print('sell_p ', sell_p)
##    print('buy_p ', buy_p)
##    print('ltp_price ', ltp_price)
    if buy_p != 0.00 and sell_p !=0.00:
        profit_loss = (float(sell_p) - float(buy_p)) * float(quantity) 
    elif buy_p != 0.00 and sell_p == 0.00: # long
        profit_loss = (float(ltp_price) - float(buy_p)) * float(quantity)
    elif sell_p != 0.00 and buy_p == 0.00: # short
        profit_loss = ( float(sell_p) - float(ltp_price)) * float(quantity)             
              
    main_df.drop(main_df.head(1).index,inplace=True)
    if os.path.exists('data/STOCK_{}.csv'.format(stockSelected)):
        with open('data/STOCK_{}.csv'.format(stockSelected), 'a') as f:
            head1.to_csv(f, header=False)        
    else:
        head1.to_csv('data/STOCK_{}.csv'.format(stockSelected)) ## save csv for future use 
         """
    
##UpdateLiveCsv()
##UpdateMainCsv()

""" def getPosition():
##    if BUY_PRICE > 0 and SELL_PRICE > 0:
    popupmsg('Functionality to be added soon')
        """ 
    
""" def placeOrder(what):    
    rsiQ = tk.Tk()
    if  what =='BUY':        
        rsiQ.wm_title(what)        
        label = ttk.Label(rsiQ, text = "Enter buy quantity:")
        label.pack(side="top", fill="x", pady=20, padx = 30)
        q = ttk.Entry(rsiQ)
        q.insert(0,100)
        q.pack()
        q.focus_set()
        label = ttk.Label(rsiQ, text = "Enter buy price:")
        label.pack(side="top", fill="y", pady=20, padx = 30)
        p = ttk.Entry(rsiQ)
        p.insert(0,0.00)
        p.pack()
        p.focus_set()
        
    if  what =='SELL':        
        rsiQ.wm_title(what)        
        label = ttk.Label(rsiQ, text = "Enter sell quantity:")
        label.pack(side="top", fill="x", pady=20, padx = 30)
        q = ttk.Entry(rsiQ)
        q.insert(0,100)
        q.pack()
        q.focus_set()
        label = ttk.Label(rsiQ, text = "Enter sell price:")
        label.pack(side="top", fill="y", pady=20, padx = 30)
        p = ttk.Entry(rsiQ)
        p.insert(0,0.00)
        p.pack()
        p.focus_set()    

    def callback():
        global buy_p 
        global sell_p
        global quantity
##        global whichFirst
##        global topIndicator
##        global DatCounter
        qty = (q.get())
        price = (p.get())
##        print(qty)
##        print('price', price)
        group = []
        group.append("rsi")
        group.append(qty)
        if what == 'BUY':
            buy_p = price
        else:
            sell_p = price

        if int(qty) > 0 and float(price) > 0:
            print("Stock {} at price of {}. Quantity: {}".format(what, price, qty))
            quantity = qty
        else:
            popupmsg("Enter Valid details!")
        
        rsiQ.destroy()
        

    b = ttk.Button(rsiQ, text="Submit", width=10, command=callback)
    b.pack()
    tk.mainloop() """
    
""" def loadData(run):
    global loadStockData
    global liveDataTrade
    if run == "start":
        loadStockData = True ## start from local db
        liveDataTrade = False ## stop live feeding
    elif run == "stop":
        loadStockData = False """

""" def loadLiveData(what):
    global liveDataTrade
    global loadStockData
    currtime = int(datetime.now().strftime ("%H%M"))
##    print(datetime.now().strftime ("%Y-%m-%d") ) #2018-06-12
    print('Live data start during trading timings.') 
    if what == "start" and currtime >=920 and currtime <=1430:
        liveDataTrade = True
        loadStockData = False
    elif what =="stop":
        liveDataTrade = False
    else:
        popupmsg("Time for Live data is between 9:20 to 14:30") """
    
def loadChart(run):
    global chartLoad
    if run == "start":
        chartLoad = True
        nextBar = False
    elif run == "stop":
        chartLoad = False

def loadNextBar():
    global nextBar, timeCount
    #stop loadChart
    #call animate and load only once. 
    loadChart("stop")
    timeCount += 1
    nextBar = True

def loadNextDate():
    global df_test1, dfForDate, timelist, timeCount, date_traded, DateList
    loadChart("stop")
    deleteIntradayFile()
    timeCount = 0
    date_traded = DateList[int(DateList.index(date_traded)) + 1]
    print('NEXT DATE: {}'.format(date_traded))
    df_test1  = df_nifty[df_nifty['DATE'] == date_traded]
    timelist = pd.unique(df_test1['TIME'].values).tolist()
    dfForDate = df_nifty_daily[df_nifty_daily['DATE_1'] == df_test1['DATE'].values[0]]
    nextBar = False
    #loadChart("start")

def submitDateForIntradayTicks(inputTxt):
    global df_test1, dfForDate, timelist, timeCount, date_traded
    inputDate = inputTxt.get("1.0","end-1c")
    print('Entered date is {}'.format(inputDate))

    loadChart("stop")
    deleteIntradayFile()
    timeCount = 0
    nextBar = False
    date_traded = inputDate
    df_test1  = df_nifty[df_nifty['DATE'] == date_traded]
    timelist = pd.unique(df_test1['TIME'].values).tolist()
    dfForDate = df_nifty_daily[df_nifty_daily['DATE_1'] == df_test1['DATE'].values[0]]
    #loadChart("start")
    ## stop chart rendering
    ## delete intraday file
    ## 

##count = 0 
def animate(i):  
    global timeCount , nextBar
    if chartLoad or nextBar :        
        pivot = dfForDate['Pivot'].values[0]
        R1 = dfForDate['R1'].values[0]
        S1 = dfForDate['S1'].values[0]
        R2 = dfForDate['R2'].values[0]
        S2 = dfForDate['S2'].values[0]
        high = dfForDate['High'].values[0]
        low =  dfForDate['Low'].values[0]
        bcp = float((high+low)/2)
        tcp = (pivot - bcp) + pivot
        
        if timeCount < 75:
            if os.path.exists('intraday5min.csv'):
                with open('intraday5min.csv', 'a') as f:                
                    df_test1[df_test1['TIME'] == timelist[timeCount]].to_csv(f, header=False, index =False)        
            else:
                df_test1[df_test1['TIME'] == timelist[timeCount]].to_csv('main/intraday5min.csv', index =False) ## save csv
            if not nextBar:
                timeCount += 1
            else:
                nextBar = False
        

        df_stock_5min_temp = pd.read_csv('intraday5min.csv')
        df_stock_5min_temp['TIMESTR'] = [str(i).replace('9', '09') for i in df_stock_5min_temp['TIME'].values]  
        df_stock_5min_temp['TIME_'] = [str(i)[:2] + ':' + str(i)[2:] for i in df_stock_5min_temp['TIMESTR'].values]
        df_stock_5min_temp['DATETIME'] = df_stock_5min_temp['DATE'].map(str) + ' '+df_stock_5min_temp['TIME_']
        df_stock_5min_temp['DATETIME'] = pd.to_datetime(df_stock_5min_temp['DATETIME'])

        df_stock_5min_temp["dateCopy"] = df_stock_5min_temp['DATETIME']
        df_stock_5min_temp["MPLDates"] = df_stock_5min_temp["dateCopy"].apply(lambda date: mdates.date2num(date.to_pydatetime()))
        del df_stock_5min_temp["dateCopy"]
        allDates = df_stock_5min_temp["MPLDates"].tolist()
        dates1 = np.asarray(allDates)
    
        ax = plt.subplot2grid((1,2), (0,0), rowspan = 4, colspan = 6)
        ax.axhline(y = bcp, color='r', linestyle='-')
        ax.axhline(y = tcp, color='g', linestyle='-')
        ax.axhline(y = pivot, color='b', linestyle='-')
##        ax.axhline(y = R1, color='r', linestyle='-')
##        ax.axhline(y = S1, color='g', linestyle='-')
##        ax.axhline(y = R2, color='r', linestyle='-')
##        ax.axhline(y = S2, color='g', linestyle='-')
        
##        ax.axhline(y = 15771, color='r', linestyle='-')
##        ax.axhline(y = 15817.40, color='g', linestyle='-')
        
##        ax.set_xticks(timelist)
##        av = plt.subplot2grid((6,4), (5,0), rowspan = 1, colspan = 4, sharex = ax)
##        av.fill_between(allDates, 0, volume,facecolor='green', alpha=0.5)
        ##        av.bar(allDates,volume,align='center')
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M')) #%d/%m/%Y 
        ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
        candlestick_ohlc(ax, df_stock_5min_temp[["MPLDates","OPEN","HIGH","LOW","CLOSE"]].values, width = 0.6/(24*60)*5 , colorup = 'g', colordown = 'r', alpha = 0.8)
        ax.xaxis_date()
        ax.autoscale_view()
        ax.set_xlabel('DATE: {}'.format(date_traded), fontsize=10)
##        plt.subplots_adjust(hspace=.0)
        plt.tight_layout()
        
        """ f.suptitle('DATE: {}'.format(date_traded), fontsize=10, fontweight='bold') """
    ##    ax.clear()
    ##    plt.show()           

class SeafBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('{}x{}'.format(850, 650))
        container = tk.Frame(self)        
        container.pack(side='top',fill= 'both', expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        for F in ([StartPage]):           
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column =0, sticky='nsew')
        deleteIntradayFile()
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
            
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text = 'Systematic trading BAR by BAR replay.', font= LARGE_FONT)
        label.pack(pady=5, padx=5)

        """ label = ttk.Label(self, text = 'Test price action and backtest bar by bar reply with pivots points', font= SMALL_FONT)
        label.pack(pady=5, padx=5) """

        button = ttk.Button(self, text ='Stop',
                           command = lambda: loadChart('stop'))
        button.pack(pady=5, padx=5 , side=tk.TOP, anchor=tk.NW)

        button2 = ttk.Button(self, text = 'Start',
                            command = lambda: loadChart('start'))
        button2.pack(pady=5, padx=5,side=tk.TOP,anchor=tk.NW)

        btnSubmitDate = ttk.Button(self, text = 'Submit',
                            command = lambda: submitDateForIntradayTicks(inputtxt))
        btnSubmitDate.pack(pady=5, padx=5,side=tk.RIGHT, anchor=tk.NE)

        buttonNextDate= ttk.Button(self, text = 'Next Date',
                            command = lambda: loadNextDate())
        buttonNextDate.pack(pady=5, padx=5,side=tk.RIGHT, anchor=tk.NE)

        buttonNextBar = ttk.Button(self, text = 'Next Bar',
                            command = lambda: loadNextBar())
        buttonNextBar.pack(pady=5, padx=5,side=tk.TOP, anchor=tk.NW)

        """ btnSubmitDate = ttk.Button(self, text = 'EXIT',
                            command =  parent.destroy)
        btnSubmitDate.pack(pady=10, padx=10,side= tk.BOTTOM, anchor=tk.SE )  """       

        inputtxt = tk.Text(self,height = 1,width = 10)
        inputtxt.insert(tk.END, date_traded)
        inputtxt.pack(pady=5, padx=5,side=tk.TOP, anchor=tk.NE) 

        label1 = ttk.Label(self, text = 'Date (YYYYMMDD)', font= LARGE_FONT)
        label1.pack(pady=5, padx=5, side=tk.TOP, anchor=tk.NE)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()

        canvas.get_tk_widget().pack(side = tk.BOTTOM, fill = tk.BOTH, expand = True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side= tk.TOP, fill= tk.BOTH, expand = True)

""" class PageOne(tk.Frame):    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label  = ttk.Label(self, text= 'Page 1', font = LARGE_FONT)
        label.pack(pady= 10, padx = 10)

        button1 =ttk.Button(self, text ='Back to home',
                           command= lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 =ttk.Button(self, text  = 'Goto Page 2',
                           command =lambda: controller.show_frame(PageTwo))
        button2.pack() """

""" class PageTwo(tk.Frame):    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label  = ttk.Label(self, text= 'Page 2', font = LARGE_FONT)
        label.pack(pady= 10, padx = 10)

        button1 =ttk.Button(self, text ='Back to home',
                           command= lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 =ttk.Button(self, text  = 'Goto Page 1',
                           command =lambda: controller.show_frame(PageOne))
        button2.pack()  """       

class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)       
        
##        label = tk.Label(self, text="Profit/Loss =", font=LARGE_FONT)
##        label.pack(pady=10,padx=10)
##
##        label_ltp = tk.Label(self, text="Last Traded Price:{}".format(ltp_price), font=NORM_FONT)
##        label_ltp.pack(side="bottom")
##
##        label_buy = tk.Label(self, text="Buy Price:{}".format(buy_p), font=NORM_FONT)
##        label_buy.pack(side="bottom")
##
##        label_sell = tk.Label(self, text="Sell Price:{}".format(sell_p), font=NORM_FONT)
##        label_sell.pack(side="bottom")


        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

##        f = Figure (figsize= (5,5), dpi = 100)
##        a = f.add_subplot(111)
##        a.plot([1,2,3,4,5,6,7,8],[7,6,5,4,8,3,2,1])



"""         canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()

        canvas.get_tk_widget().pack(side = tk.BOTTOM, fill = tk.BOTH, expand = True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side= tk.TOP, fill= tk.BOTH, expand = True) """
        

    
def qf(quickPrint):
    print(quickPrint)            

app = SeafBTCapp()
ani = animation.FuncAnimation(f, animate, interval=2000)
app.mainloop()
