from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
##import datetime
from datetime import datetime
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.action_chains import ActionChains

try:       
    
    def round_num(x, prec=2, base=.05): ##.05
        return round(base * round(float(x)/base),prec)


## START FROM HERE.    
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    #options.binary_location = "/usr/bin/chromium"
    #driver = webdriver.Chrome()
    driver = webdriver.Chrome('path/chromedriver.exe', chrome_options=options)        
    driver.get('https://kite.zerodha.com/')
    ##html = driver.page_source
    ##print(html)
    time.sleep(5)    

    driver.find_element_by_tag_name("body").click();

    elemuser = WebDriverWait(driver, 120, 1).until(
            expect.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='User ID']")))
    elemuser.send_keys('USER ID')


    elempswd = WebDriverWait(driver, 120, 1).until(
            expect.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Password']")))
    elempswd.send_keys('PASSWORD')

    ##click submit
    time.sleep(1)
    driver.find_element_by_class_name('actions').submit()

    time.sleep(2)
    driver.find_element_by_tag_name("body").click();
    
    elempin = WebDriverWait(driver, 120, 1).until(
            expect.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='PIN']")))
    elempin.send_keys('PIN')


    time.sleep(1)
    driver.find_element_by_class_name('actions').submit()
    time.sleep(15)
    driver.find_element_by_tag_name("body").click();





    ohlc_columns_5_min = ['STOCK','TIME','OPEN','HIGH','LOW','CLOSE','INT_TIME']
    df_ohlc_main_5_min = pd.DataFrame(columns = ohlc_columns_5_min)
    today_date = str(time.strftime('%d%m%y'))
    def record_and_save_ohlc(df_temp, time):
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
##            print(stock,time,'OPEN:',OPEN,'CLOSE:',CLOSE,'HIGH:',HIGH,'LOW:',LOW)
            ## calculate both short and long positions. qty, entry, exit, target, abs sl, abs entry.
            ohlc_5_min.append([stock, time ,OPEN, HIGH, LOW, CLOSE, time_int])        
        
        for ohlc in ohlc_5_min:
##            print(ohlc)
            df_ohlc_main_5_min.loc[len(df_ohlc_main_5_min)] = ohlc
##        df_ohlc_main_5_min["INT_TIME"] = pd.to_numeric(df["TIME"])

        filename_OHLC = 'OHLC_{}.csv'.format(today_date)                   
        df_ohlc_main_5_min.to_csv('OHLC/{}'.format(filename_OHLC), index = False)

  
    all_stocks = driver.find_elements_by_xpath("//span[@class='nice-name']")
    stocks = []
    for span in all_stocks:        
        stocks.append(span.text)
        
##here
    print(stocks)
    df_watchlist = pd.DataFrame(stocks, columns = ['SYMBOL'])
##    print(df_stock)
    filename = 'LIST_{}.csv'.format(today_date)
##    df_watchlist.to_csv('stocks_traded/{}'.format(filename),index= False)
    
##    list_master = []
    list_ohlc = []
    last_5_min_check = 'NONE'
    for i in range(0,3000000):
##        currentDT = datetime.datetime.now()
##        ##print ("Current Second is: %d" % currentDT.second)
##        concatetime = str(('{}{}').format(currentDT.hour,currentDT.minute))
##        prices = driver.find_elements_by_xpath("//span[@class='last-price']")
        concatetime = str(time.strftime('%H%M'))
        prices = driver.find_elements_by_xpath("//div[@class='info']//span[@class='last-price']") 
        listprice = []

        for price in prices:
            listprice.append(price.text)            
##        list_master.append(listprice)
        list_ohlc.append(listprice)
##        print(listprice)
        if int(concatetime) % 5 == 0 and last_5_min_check != concatetime and int(concatetime) > 855:
            print('Calculate ohlc ', concatetime)
            df_temp = pd.DataFrame(list_ohlc,columns=stocks)
            record_and_save_ohlc(df_temp, concatetime )
            list_ohlc = []
            if concatetime == '1400':
                ## exit after 5 min for 5 min range
                break;            
            last_5_min_check =  concatetime
        time.sleep(.3)


    print('Completed')    
    
except Exception as e:
    print(e)
finally:
    driver.close()
##    driver.quit()
