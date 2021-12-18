import urllib.request
import urllib.parse
import re
import csv


def save_price_details(symbol, timeframe, day_1):    
    req_url = 'https://www.google.com/finance/getprices?q='+symbol+'&x=NSE&i='+timeframe+'&p='+day_1+'d&f=d,c,h,l,o,v'
    #req_url = 'https://www.google.com/finance/getprices?q='+symbol+'&x=NSE&i='+timeframe+'&p='+day_1+'Y&f=d,c,h,l,o,v'
    #print(req_url)

    try:
        req = urllib.request.urlopen(req_url)
        resp_data=req.read()
        #print("resp_data  "+ resp_data)
        check = resp_data.decode('UTF-8')
        if int(timeframe) == 86400:
            savefile = open('1_DAY/STOCK_'+symbol+'.csv', 'w')
        elif int(timeframe) == 60:
            savefile = open('60_SEC/STOCK_'+symbol+'.csv', 'w')
        elif int(timeframe) == 300:
            savefile = open('5_MIN/STOCK_'+symbol+'.csv', 'w')
            
        savefile.write(str(check))
        savefile.close() 
    except Exception as e:
        print(str(e))


