from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import datetime
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.action_chains import ActionChains
import logging
from datetime import datetime as dt
from BUY_SELL import buy_sell_BO_MIS
from LOGIN_KITE import zerodha_login
from INTRADAY_PATTERN import patterns
import csv
try:
    time_log = dt.now().strftime('NIFTY_STOCKS/TRADE_LOG_%H_%M_%d_%m_%Y.log')
    logging.basicConfig(filename = time_log ,level=logging.INFO)

    logging.info('PROCESS STARTED')
##    breaktime = '2235'
    try:
        capital = pd.read_csv('main/{}'.format('Capital.csv'))['HEADER'].values
    except Exception as e:
        print('ERROR READING Capital file..')
        logging.info('ERROR READING Capital file.. {}'.format(e))  
        capital = int(10000)
        
##    risk                = int(((capital * 1)/100))
    risk                = int(300)
    target              = float(20) ##3R, 4R, 5R
    target_lmt          = float(1.5)
    target_profit       = target * risk
    target_profit_lmt   = target_lmt * risk
    buySell             = buy_sell_BO_MIS()
    login_              = zerodha_login()
    patterns_           = patterns()    
    TradedScripts = []
    def round_num(x, prec=2, base=.05): ##.05
        return round(base * round(float(x)/base),prec)

## START FROM HERE.
    print('****OM GAN GANPATAYE NAMAH****')
    logging.info('****OM GAN GANPATAYE NAMAH****')
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    #options.binary_location = "/usr/bin/chromium"
    #driver = webdriver.Chrome()
    driver = webdriver.Chrome('C:/Users/ACER/Desktop/python/_NSE_ARCHIVED/Automation work/chromedriver.exe', chrome_options=options)

    ##########
    login_.loginChrome(driver, logging, 'IR5523', 'dashingmayank@15', '151195')
    ##########

    ohlc_columns_5_min = ['STOCK','TIME','OPEN','HIGH','LOW','CLOSE','INT_TIME']
    df_ohlc_main_5_min = pd.DataFrame(columns = ohlc_columns_5_min)

    df_range_cols  = ['STOCK', 'HIGH', 'LOW'] 
    df_range_identified = pd.DataFrame(columns = df_range_cols)
    highlowbreak = []
    TRADE_LOG = []
    scriptTraded = []
    BUYS = 0
    SELL = 0
    trade_log = pd.DataFrame(columns = ['STOCK','TYPE','QTY','ENTRY','STOP'])        

    def record_ohlc(df_temp, time):
        ohlc_5_min = []        
        for stock in list(df_temp.columns.values):
            list_price = df_temp[stock].values
            list_floats = [float(i) for i in list_price]
    ##        print(list_floats)
            OPEN  = float(list_floats[0])
            CLOSE = float(list_floats[-1])
            HIGH  = float(max(list_floats))
            LOW  =  float(min(list_floats))
            time_int = int(time)
            ohlc_5_min.append([stock, time ,OPEN, HIGH, LOW, CLOSE, time_int])        
        
        for ohlc in ohlc_5_min:
            df_ohlc_main_5_min.loc[len(df_ohlc_main_5_min)] = ohlc
        print('Save and replace existing df to be read from another job.')
        df_ohlc_main_5_min.to_csv('OHLC_TICKS/OHLC.csv', mode='w')
            
            
    all_stocks = driver.find_elements_by_xpath("//span[@class='nice-name']")
    stocks = []
    stocks_to_sell = []
    stocks_all = []
    stocks_to_buy = []

##    companies = []
##    with open('EQUITY STOCKS.csv') as csvfile:
##        readcsv = csv.reader(csvfile, delimiter=',')     
##        for row in readcsv:
##            comp = row[0]
##            companies.append(comp)
    tradeLogCols = ['STOCK','TRADE','ENTRY','SL','QTY','ABS_SL','ABS_TGT']
    tradeLog = pd.DataFrame(columns = tradeLogCols)
##    df_ohlc_main_5_min.loc[len(df_ohlc_main_5_min)] = ohlc    
    
    for span in all_stocks:        
        stocks.append(span.text)
        stock = span.text
        print(span.text)        



    list_ohlc = []
    last_5_min_check = 'NONE'
    LOSS_PERDAY = float(-500)
##    buySell.BUY_SELL_SLM(logging, driver,'button-orange',1, 265, 264, 1, 10, 1, 'JSWSTEEL')
##    time.sleep(20)
    for ii in range(0,900000000):
        concatetime = str(time.strftime('%H%M'))
        prices = driver.find_elements_by_xpath("//div[@class='info']//span[@class='last-price']") 
        listprice = []
        for price in prices:
            listprice.append(price.text)            
        
        list_ohlc.append(listprice)
        if last_5_min_check != concatetime and int(concatetime) > 915 and ( int(concatetime) == 930 or int(concatetime) == 945 or int(concatetime) == 1000 or int(concatetime) == 1015 or int(concatetime) == 1030  or int(concatetime) == 1045 or int(concatetime) == 1100):
            logging.info('Calculate ohlc {}'.format(concatetime))
            df_temp = pd.DataFrame(list_ohlc,columns=stocks)
            record_ohlc(df_temp, concatetime )
            list_ohlc = []
            if int(concatetime) == 1100:
                logging.info('Script Execution completed.')
                print('Script Execution completed.')                
                break          
            last_5_min_check =  concatetime

        time.sleep(0.1)

    ## again loop through range
    ## let LTP.
    ## for i_ in range(0, len(stocks)): stk = stocks[i_] use prices to get 
            
            
    print('JSK')
    logging.info('JSK')


except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
