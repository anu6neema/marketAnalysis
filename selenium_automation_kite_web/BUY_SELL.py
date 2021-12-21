##import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.action_chains import ActionChains
class buy_sell_BO_MIS:

    def absSL(self, driver, logging, ABS_SL):
        try:
            logging.info('BO {}'.format(28))
            elemABS_SL = WebDriverWait(driver,2).until(
                    expect.visibility_of_element_located(
                    (By.XPATH,"//input[@label='Stoploss']")))
            elemABS_SL.send_keys(Keys.CONTROL + "a");
            logging.info('BO {}'.format(28))
            time.sleep(.2)
            elemABS_SL.send_keys(Keys.DELETE);
            logging.info('BO {}'.format(29))
            elemABS_SL.send_keys(str(ABS_SL))
            logging.info('BO {}'.format(30))
        except Exception as e: ## "//input[@value='bo' and @type='radio']"
            noError = False
            print('error SL input', e)
            logging.info('error SL input {}'.format(e))

    def absTgt(self, driver, logging, ABS_TGT):        
        try:
            logging.info('BO {}'.format(31))
            elemABS_TGT = WebDriverWait(driver, 2).until(
                    expect.visibility_of_element_located(
                    (By.XPATH,"//input[@label='Target']")))
            logging.info('BO {}'.format(32))
            elemABS_TGT.send_keys(Keys.CONTROL + "a");
            logging.info('BO {}'.format(33))
            elemABS_TGT.send_keys(Keys.DELETE);
            time.sleep(.3)
            logging.info('BO {}'.format(34))
            elemABS_TGT.send_keys(str(ABS_TGT))
            logging.info('BO {}'.format(35))
        except Exception as e: ## "//input[@value='bo' and @type='radio']"
            noError = False
            print('error Tgt input', e)
            logging.info('error Tgt input {}'.format(e))
        

    def boRadio(self, driver, logging):
        try:
            elemBO = WebDriverWait(driver, 2).until(
                    expect.element_to_be_clickable(
                    (By.XPATH,"//label[contains(text(),'Bracket')]")))
            logging.info('BO {}'.format(12))
            driver.execute_script("arguments[0].click();", elemBO) 
            time.sleep(.1)
            result_bo = driver.execute_script("return document.querySelector('input[type=\"radio\"][value=\"bo\"]').checked")
            if result_bo == True:
                print('BO radio selected.', result_bo)
                logging.info('BO radio selected.')
            logging.info('BO {}'.format(13))
        except Exception as e: ## "//input[@value='bo' and @type='radio']"
            noError = False
            print('error finding BO radio button', e)
            logging.info('error finding BO radio button..')

    def boPrice(self, driver, logging, ENTRYPRICE):
        noError = True
        try:
            
            logging.info('BO {}'.format(24))
            CLEAR_TRIGGER = WebDriverWait (driver, 2).until(expect.element_to_be_clickable((By.XPATH,"//input[@label='Price']")))
            CLEAR_TRIGGER.click()
            time.sleep(.3)
            CLEAR_TRIGGER.clear()
##                    print(11)
            #driver.find_element_by_tag_name("body").click()
            self.doBodyClick(driver, logging)
            logging.info('BO {}'.format(25))
            elemtrigger = WebDriverWait(driver,2).until(
                    expect.visibility_of_element_located(
                    (By.XPATH,"//input[@label='Price']")))
            logging.info('BO {}'.format(26))
            time.sleep(.2)
            elemtrigger.send_keys(str(ENTRYPRICE))
            logging.info('BO {}'.format(27))
        except Exception as e: ## "//input[@value='bo' and @type='radio']"
            noError = False
            print('error trigger price input', e) 
            logging.info('error trigger price input'.format(e))
        return noError                       
        
    def SLRadio(self, driver, logging):
        noError = True
        try:            
            elem_ = WebDriverWait(driver, 2).until(
                    expect.element_to_be_clickable(
                    (By.XPATH,"//label[contains(text(),'SL')]")))
            driver.execute_script("arguments[0].click();", elem_)
            result_ = driver.execute_script("return document.querySelector('input[type=\"radio\"][value=\"SL\"]').checked")
            if result_ == True:
                print('MIS radio selected.', result_)
                logging.info('MIS radio selected.')
            logging.info('BO {}'.format(12))                        
        except Exception as e: 
            noError = False
            print('error finding regularRadio radio button', e)
            
        return noError
        
    def regularRadio(self, driver, logging):
        noError = True
        try:            
            elem_ = WebDriverWait(driver, 2).until(
                    expect.element_to_be_clickable(
                    (By.XPATH,"//label[contains(text(),'Regular')]")))
            driver.execute_script("arguments[0].click();", elem_)
            result_ = driver.execute_script("return document.querySelector('input[type=\"radio\"][value=\"regular\"]').checked")
            if result_ == True:
                print('MIS radio selected.', result_)
                logging.info('MIS radio selected.')
            logging.info('BO {}'.format(12))                        
        except Exception as e: 
            noError = False
            print('error finding regularRadio radio button', e)
            
        return noError         

    def coverOrderRadio(self, driver, logging):
        noError = True
        try:            
            elem_ = WebDriverWait(driver, 2).until(
                    expect.element_to_be_clickable(
                    (By.XPATH,"//label[contains(text(),'Cover')]")))
            driver.execute_script("arguments[0].click();", elem_)
            result_ = driver.execute_script("return document.querySelector('input[type=\"radio\"][value=\"co\"]').checked")
            if result_ == True:
                print('co radio selected.', result_)
                logging.info('co radio selected.')
            logging.info('BO {}'.format(12))                        
        except Exception as e: 
            noError = False
            print('error finding co radio button', e)
            
        return noError

    def ClickLimitRadio(self, driver, logging):
        noError = True
        try:
            elemLMT = WebDriverWait(driver,2).until(
                    expect.element_to_be_clickable(
                    (By.XPATH,"//label[contains(text(),'Limit')]")))                                      
            logging.info('BO {}'.format(16.2))
            driver.execute_script("arguments[0].click();", elemLMT)                    
            time.sleep(.2)
            result_lmt = driver.execute_script("return document.querySelector('input[type=\"radio\"][value=\"LIMIT\"]').checked")                    
            if result_lmt == True:
                print('Limit radio selected.', result_lmt)
                logging.info('Limit radio selected.')                   
            logging.info('BO {}'.format(16.3))
        except Exception as e:
            noError = False
            print('error finding LIMIT radio button', e)
            logging.info('error finding LIMIT radio button {}'.format(e))        
        return noError 

    def MISRadio(self, driver, logging):
        noError = True
        try:            
            elem_ = WebDriverWait(driver, 2).until(
                    expect.element_to_be_clickable(
                    (By.XPATH,"//label[contains(text(),'Intraday ')]")))
            driver.execute_script("arguments[0].click();", elem_)
            result_ = driver.execute_script("return document.querySelector('input[type=\"radio\"][value=\"MIS\"]').checked")
            if result_ == True:
                print('MIS radio selected.', result_)
                logging.info('MIS radio selected.')
            logging.info('BO {}'.format(12))
            logging.info('BO {}'.format(13))                        
        except Exception as e: 
            noError = False
            print('error finding MISRadio radio button', e)
        return noError             
        

    def slmRadio(self, driver, logging):
        noError = True
        try:
            
            elemSL = WebDriverWait(driver,2).until(
                    expect.element_to_be_clickable(
                    (By.XPATH,"//label[contains(text(),'SL-M')]")))
    ##                    elemSL = WebDriverWait(driver, 2).until(
    ##                            expect.element_to_be_clickable(
    ##                            (By.CSS_SELECTOR,"input[type='radio'][value='SL']")))                                         
            logging.info('BO {}'.format(15))
    ##                    elemSL.click()
            driver.execute_script("arguments[0].click();", elemSL)                     
            time.sleep(.2)
            result_sl = driver.execute_script("return document.querySelector('input[type=\"radio\"][value=\"SL-M\"]').checked")
            if result_sl == True:
                print('sl-m radio selected.', result_sl)
                logging.info('sl-m radio selected.')                    
            logging.info('BO {}'.format(16))
        except Exception as e: ## "//input[@value='bo' and @type='radio']"
            noError = False
            print('error finding SL-m radio button', e)
            logging.info('error finding SL-m radio button {}'.format(e))

        return noError     

    def enterQty(self, driver, logging, QTY):
        noError = True
        try:
            logging.info('BO {}'.format(17))
            print('qty form')
            logging.info('qty form')
            CLEAR_QTY = WebDriverWait (driver,2).until(expect.element_to_be_clickable((By.XPATH,"//input[@label='Qty.']")))
            CLEAR_QTY.click()
            time.sleep(.2)
            CLEAR_QTY.clear()
            logging.info('BO {}'.format(18))
            #driver.find_element_by_tag_name("body").click()
            self.doBodyClick(driver, logging)
            print('qty form clear. enter values now')
            logging.info('qty form clear. enter values now')
            elemQTY = WebDriverWait(driver,2).until(
                    expect.visibility_of_element_located(
                    (By.XPATH,"//input[@label='Qty.']")))
##            time.sleep(.2)
            logging.info('BO {}'.format(19))
            elemQTY.send_keys(str(QTY))
            logging.info('BO {}'.format(20))
        except Exception as e: ## "//input[@value='bo' and @type='radio']" SLPrice   LimitEntryPrice
            print('error QTY input', e)
            noError = False
            logging.info('error QTY input {}'.format(e))
            
        return noError

    def LimitEntryPrice(self, driver, logging, ENTRYPRICE):
        noError = True
        try:            
            logging.info('BO {}'.format(24))
            CLEAR_TRIGGER = WebDriverWait (driver, 2).until(expect.element_to_be_clickable((By.XPATH,"//input[@label='Price']")))
            CLEAR_TRIGGER.click()
            time.sleep(.3)
            CLEAR_TRIGGER.clear()
            self.doBodyClick(driver, logging)
            logging.info('BO {}'.format(25))
            elemtrigger = WebDriverWait(driver,2).until(
                    expect.visibility_of_element_located(
                    (By.XPATH,"//input[@label='Price']")))
            logging.info('BO {}'.format(26))
            time.sleep(.2)
            elemtrigger.send_keys(str(ENTRYPRICE))
            logging.info('BO {}'.format(27))
        except Exception as e: ## "//input[@value='bo' and @type='radio']"
            noError = False
            print('error trigger price input', e) 
            logging.info('error trigger price input'.format(e))
        return noError

    def SLPrice(self, driver, logging, SLPrice):
        noError = True
        try:            
            logging.info('BO {}'.format(24))
            CLEAR_TRIGGER = WebDriverWait (driver, 2).until(expect.element_to_be_clickable((By.XPATH,"//input[@label='Stoploss trigger Price']")))
            CLEAR_TRIGGER.click()
            time.sleep(.3)
            CLEAR_TRIGGER.clear()
            self.doBodyClick(driver, logging)
            logging.info('BO {}'.format(25))
            elemtrigger = WebDriverWait(driver,2).until(
                    expect.visibility_of_element_located(
                    (By.XPATH,"//input[@label='Stoploss trigger Price']")))
            logging.info('BO {}'.format(26))
            time.sleep(.2)
            elemtrigger.send_keys(str(SLPrice))
            logging.info('BO {}'.format(27))
        except Exception as e: ## "//input[@value='bo' and @type='radio']"
            noError = False
            print('error trigger price input', e) 
            logging.info('error trigger price input'.format(e))
        return noError

    def triggerPrice(self, driver, logging, ENTRYPRICE):
        noError = True
        try:
            
            logging.info('BO {}'.format(24))
            CLEAR_TRIGGER = WebDriverWait (driver, 2).until(expect.element_to_be_clickable((By.XPATH,"//input[@label='Trigger price']")))
            CLEAR_TRIGGER.click()
            time.sleep(.3)
            CLEAR_TRIGGER.clear()
##                    print(11)
            #driver.find_element_by_tag_name("body").click()
            self.doBodyClick(driver, logging)
            logging.info('BO {}'.format(25))
            elemtrigger = WebDriverWait(driver,2).until(
                    expect.visibility_of_element_located(
                    (By.XPATH,"//input[@label='Trigger price']")))
            logging.info('BO {}'.format(26))
            time.sleep(.2)
            elemtrigger.send_keys(str(ENTRYPRICE))
            logging.info('BO {}'.format(27))
        except Exception as e: ## "//input[@value='bo' and @type='radio']"
            noError = False
            print('error trigger price input', e) 
            logging.info('error trigger price input'.format(e))
        return noError       

    def BuySellOrderPlace(self, driver, logging, TRADE):
        noError = True
        try:
            
            logging.info('BO {}'.format(36))
            elemPlaceOrder = WebDriverWait(driver,2).until(
                    expect.visibility_of_element_located(
                    (By.XPATH,"//button[@type='submit' and contains(@class,'"+TRADE+"')]")))
            ##'" + state + "'
            logging.info('BO {}'.format(37))
            elemPlaceOrder.click()
            logging.info('BO {}'.format(38))
        except Exception as e: ## "//input[@value='bo' and @type='radio']"
            noError = False
            print('error placing order', e)
            logging.info('error placing order {}'.format(e))
        return noError
    
    def doBodyClick(self, driver, logging):
        try:
            driver.find_element_by_tag_name("body").click()
        except Exception as e:
            print('Error CLicking body ', e)            
        
    def switchToTab1(self, driver, logging):        
        print('Switch to 1 tab')
        logging.info('Switch to 1 tab')
        try:
            mktSelector = driver.find_element_by_xpath("//ul[contains(@class, 'marketwatch-selector')]")
            item = mktSelector.find_elements_by_xpath("//li[contains(@class, 'item')]")[0]
            item.click()
            time.sleep(1)            
        except Exception as e:
            print('Error Switch to 1 tab', e)

    def switchToTab2(self, driver, logging):        
        print('Switch to 2 tab')
        logging.info('Switch to 2 tab')
        try:
            mktSelector = driver.find_element_by_xpath("//ul[contains(@class, 'marketwatch-selector')]")
            item = mktSelector.find_elements_by_xpath("//li[contains(@class, 'item')]")[1]
            item.click()
            time.sleep(1)
        except Exception as e:
            print('Error Switch to 2 tab', e)

    def BUY_SELL_AMO(self, logging, driver, TRADE, QTY, ENTRYPRICE, STOP, ABS_SL, ABS_TGT, i_dex, STOCK_, SLORDER = False):
        try:
            noError = True
            logging.info('BO {}'.format(1)) 
            print('i_dex', i_dex)
            tab_chng = False
            if i_dex >  11:
                self.switchToTab2(driver, logging)
                tab_chng = True
                i_dex = i_dex - 12

            logging.info('i_dex {}'.format(i_dex))
            ele = driver.find_elements_by_xpath("//div[contains(@class, 'vddl-draggable') and contains(@class, 'instrument')]")[i_dex]
            logging.info('BO {}'.format(2))
            items1 = ele.find_element_by_xpath(".//div[contains(@class, 'info')]")
            logging.info('BO {}'.format(3))
            script = items1.find_element_by_xpath(".//span[contains(@class, 'nice-name')]").text
            print('SCRIPT found',script,'to be checked with', STOCK_)
            logging.info('BO {}'.format(4))
            logging.info('SCRIPT found {} to be checked with {}'.format(script, STOCK_))
        except Exception as e:
            noError = False
            print('Element not found in BUY_SELL ',e)
            logging.info('Element not found in BUY_SELL {}'.format(e))

        if script == STOCK_:
            logging.info('BO {}'.format(5))
            print('Script match = SUCCESS')
            logging.info('Script match = SUCCESS')
            print('hover and buy/sell')
            logging.info('hover and buy/sell')
            try:
                logging.info('BO {}'.format(6))
                Hover = ActionChains(driver).move_to_element(items1)
                Hover.perform()
                logging.info('BO {}'.format(7))
                time.sleep(.3)
                elebuy = WebDriverWait(driver,1, 1).until(            
                        expect.element_to_be_clickable(
                        (By.XPATH,"//button[contains(@class,'"+TRADE+"')]")))
                logging.info('BO {}'.format(8))
                elebuy.click()              
            except Exception as e:
                noError = False
                print('Error performing hover and buy/sell', e)
                logging.info('Error performing hover and buy/sell {}'.format(e))

                
            print('Buy Button Clicked')
            logging.info('Buy Button Clicked')
            
          
            time.sleep(2)            
        

        if script == STOCK_:
            logging.info('BO {}'.format(5))
            print('Script match = SUCCESS')
            logging.info('Script match = SUCCESS')
            print('hover and buy/sell')
            logging.info('hover and buy/sell')
            try:
                logging.info('BO {}'.format(6))
                Hover = ActionChains(driver).move_to_element(items1)
                Hover.perform()
                logging.info('BO {}'.format(7))
                time.sleep(.3)
                elebuy = WebDriverWait(driver,1, 1).until(            
                        expect.element_to_be_clickable(
                        (By.XPATH,"//button[contains(@class,'"+TRADE+"')]")))
                logging.info('BO {}'.format(8))
                elebuy.click()              
            except Exception as e:
                noError = False
                print('Error performing hover and buy/sell', e)
                logging.info('Error performing hover and buy/sell {}'.format(e))

                
            print('Buy Button Clicked')
            logging.info('Buy Button Clicked')
            
          
            time.sleep(2)
            

            
            print('cliking MIS')
            logging.info('cliking MIS')
            self.doBodyClick(driver, logging)
            try:
                elemMIS = WebDriverWait(driver, 2).until(
                        expect.element_to_be_clickable(
                        (By.XPATH,"//label[contains(text(),'MIS')]")))
                driver.execute_script("arguments[0].click();", elemMIS)
                result_mis = driver.execute_script("return document.querySelector('input[type=\"radio\"][value=\"MIS\"]').checked")
                if result_mis == True:
                    print('MIS radio selected.', result_mis)
                    logging.info('MIS radio selected.')
                logging.info('BO {}'.format(12))
##                    elemMIS.click()
                time.sleep(.2)
                logging.info('BO {}'.format(13))
##                    if elemMIS.is_selected() == True:
##                        logging.info('MIS radio is selected.')
##                        
            except Exception as e: ## "//input[@value='bo' and @type='radio']"
                noError = False
                print('error finding MIS radio button', e)
                logging.info('error finding MIS radio button. trying again.')
                time.sleep(.5)    

            time.sleep(1)                
                            
            print('cliking more options')
            logging.info('cliking more options')
            self.doBodyClick(driver, logging)
            try:
                logging.info('BO {}'.format(9))
                eleMoreoptions = WebDriverWait(driver,2).until(            
                        expect.element_to_be_clickable(
                        (By.XPATH,"//a[@class='advanced-options-open']")))
                logging.info('BO {}'.format(10))
                eleMoreoptions.click()
                logging.info('BO {}'.format(11))
##                print(6)
                time.sleep(.5)
            except Exception as e:
##                noError = False
                print('more options tag not found')      
                logging.info('more options tag not found')         

        ## REGULAR RADIO
            print('AMO radio')
            logging.info('AMO radio')
            self.doBodyClick(driver, logging)
            try:
                elemRg = WebDriverWait(driver, 2).until(
                        expect.element_to_be_clickable(
                        (By.XPATH,"//label[contains(text(),'amo')]")))
##                    elemRg = WebDriverWait(driver, 2).until(
##                            expect.element_to_be_clickable(
##                            (By.CSS_SELECTOR,"input[type='radio'][value='regular']")))                     
##                print(7)
                logging.info('BO {}'.format(11.1))
##                    elemRg.click()
                driver.execute_script("arguments[0].click();", elemRg)                    
                time.sleep(.2)
                result_rg = driver.execute_script("return document.querySelector('input[type=\"radio\"][value=\"amo\"]').checked")
                if result_rg == True:
                    print('AMO radio selected.', result_rg)
                    logging.info('AMO radio selected.')                  
                logging.info('BO {}'.format(11.2))
            except Exception as e: ## "//input[@value='bo' and @type='radio']"                
                print('error finding amo radio button', e)
                logging.info('error finding amo radio button. trying again.')
                
            time.sleep(.5)

    ## click SL order
            if SLORDER == True:            
                try:
                    self.doBodyClick(driver, logging)
                    logging.info('BO {}'.format(14))
                    print('sl radio button')
                    logging.info('sl radio button')
                    elemSL = WebDriverWait(driver,2).until(
                            expect.element_to_be_clickable(
                            (By.XPATH,"//label[contains(text(),'SL')]")))
##                    elemSL = WebDriverWait(driver, 2).until(
##                            expect.element_to_be_clickable(
##                            (By.CSS_SELECTOR,"input[type='radio'][value='SL']")))                                         
                    logging.info('BO {}'.format(15))
##                    elemSL.click()
                    driver.execute_script("arguments[0].click();", elemSL)                     
                    time.sleep(.2)
                    result_sl = driver.execute_script("return document.querySelector('input[type=\"radio\"][value=\"SL\"]').checked")
                    if result_sl == True:
                        print('sl radio selected.', result_sl)
                        logging.info('sl radio selected.')                    
                    logging.info('BO {}'.format(16))
                except Exception as e: ## "//input[@value='bo' and @type='radio']"
                    noError = False
                    print('error finding SL radio button', e)
                    logging.info('error finding SL radio button {}'.format(e))
                time.sleep(.5)
            else:
                try:
                    self.doBodyClick(driver, logging)
                    logging.info('BO {}'.format(16.1))
                    print('LIMIT radio button')
                    logging.info('LIMIT radio button')
                    elemLMT = WebDriverWait(driver,2).until(
                            expect.element_to_be_clickable(
                            (By.XPATH,"//label[contains(text(),'LIMIT')]")))
##                    elemLMT = WebDriverWait(driver, 2).until(
##                            expect.element_to_be_clickable(
##                            (By.CSS_SELECTOR,"input[type='radio'][value='LIMIT']")))                                        
                    logging.info('BO {}'.format(16.2))
##                    elemLMT.click()
                    driver.execute_script("arguments[0].click();", elemLMT)                    
                    time.sleep(.2)
                    result_lmt = driver.execute_script("return document.querySelector('input[type=\"radio\"][value=\"LIMIT\"]').checked")                    
                    if result_lmt == True:
                        print('Limit radio selected.', result_lmt)
                        logging.info('Limit radio selected.')                   
                    logging.info('BO {}'.format(16.3))
                except Exception as e: ## "//input[@value='bo' and @type='radio']"
                    noError = False
                    print('error finding LIMIT radio button', e)
                    logging.info('error finding LIMIT radio button {}'.format(e))
                time.sleep(.5)                

                            
    ##-------------------------------------------------------------------------------------------------------------        
    ##fill in form details.
            #driver.find_element_by_tag_name("body").click()
            self.doBodyClick(driver, logging)
            try:
                logging.info('BO {}'.format(17))
                print('qty form')
                logging.info('qty form')
                CLEAR_QTY = WebDriverWait (driver,2).until(expect.element_to_be_clickable((By.XPATH,"//input[@label='Qty.']")))
                CLEAR_QTY.click()
                time.sleep(.2)
                CLEAR_QTY.clear()
                logging.info('BO {}'.format(18))
                #driver.find_element_by_tag_name("body").click()
                self.doBodyClick(driver, logging)
                print('qty form clear. enter values now')
                logging.info('qty form clear. enter values now')
                elemQTY = WebDriverWait(driver,2).until(
                        expect.visibility_of_element_located(
                        (By.XPATH,"//input[@label='Qty.']")))
    ##            time.sleep(.2)
                logging.info('BO {}'.format(19))
                elemQTY.send_keys(str(QTY))
                logging.info('BO {}'.format(20))
            except Exception as e: ## "//input[@value='bo' and @type='radio']"
                print('error QTY input', e)
                noError = False
                logging.info('error QTY input {}'.format(e))     
            time.sleep(.5)
            
            try:
                CLEAR_ENTRY = WebDriverWait (driver,2).until(expect.element_to_be_clickable((By.XPATH,"//input[@label='Price']")))
                logging.info('BO {}'.format(20.1))
                CLEAR_ENTRY.click()
                logging.info('BO {}'.format(20.2))
                time.sleep(.3)
                CLEAR_ENTRY.clear()
                logging.info('BO {}'.format(21))
                #driver.find_element_by_tag_name("body").click()
                self.doBodyClick(driver, logging)
                elemEntry = WebDriverWait(driver,2).until(
                        expect.visibility_of_element_located(
                        (By.XPATH,"//input[@label='Price']")))
##                print(10)            
                time.sleep(.2)
                logging.info('BO {}'.format(22))
                elemEntry.send_keys(str(ENTRYPRICE))
                logging.info('BO {}'.format(23))
            except Exception as e:
                noError = False
                print('error Entry price input', e) 
                logging.info('error Entry price input {}'.format(e))
            time.sleep(.5)
            
            if SLORDER == True:            
                try:
                    logging.info('BO {}'.format(24))
                    CLEAR_TRIGGER = WebDriverWait (driver, 2).until(expect.element_to_be_clickable((By.XPATH,"//input[@label='Trigger price']")))
                    CLEAR_TRIGGER.click()
                    time.sleep(.3)
                    CLEAR_TRIGGER.clear()
##                    print(11)
                    #driver.find_element_by_tag_name("body").click()
                    self.doBodyClick(driver, logging)
                    logging.info('BO {}'.format(25))
                    elemtrigger = WebDriverWait(driver,2).until(
                            expect.visibility_of_element_located(
                            (By.XPATH,"//input[@label='Trigger price']")))
                    logging.info('BO {}'.format(26))
                    time.sleep(.2)
                    elemtrigger.send_keys(str(ENTRYPRICE))
                    logging.info('BO {}'.format(27))
                except Exception as e: ## "//input[@value='bo' and @type='radio']"
                    noError = False
                    print('error trigger price input', e) 
                    logging.info('error trigger price input'.format(e))
            time.sleep(.2)

            if noError == True:                
                try:
                    logging.info('BO {}'.format(36))
                    elemPlaceOrder = WebDriverWait(driver,2).until(
                            expect.visibility_of_element_located(
                            (By.XPATH,"//button[@type='submit' and contains(@class,'"+TRADE+"')]")))
                    ##'" + state + "'
                    logging.info('BO {}'.format(37))
                    elemPlaceOrder.click()
                    logging.info('BO {}'.format(38))
                except Exception as e: ## "//input[@value='bo' and @type='radio']"
                    noError = False
                    print('error placing order', e)
                    logging.info('error placing order {}'.format(e))
                time.sleep(2)
            else:
                print('noError == False, no order place.')
                logging.info('noError == False, no order place.')
                
            try:
                logging.info('BO {}'.format(39))
                ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                logging.info('BO {}'.format(40))
                if tab_chng:
                    self.switchToTab1(driver, logging)
            except Exception as e:                
                print('Error sending escape key.',e)
                logging.info('Error sending escape key. {}'.format(e))
            print('buy/sell completed successfully.')
            logging.info('buy/sell completed successfully.')

    
    def BUY_SELL(self, logging, driver, TRADE, QTY, ENTRYPRICE, STOP, ABS_SL, ABS_TGT, i_dex, STOCK_, ORDER_TYPE, SLORDER = False):
        try:
            noError = True
            logging.info('BO {}'.format(1)) 
            print('i_dex', i_dex)
            tab_chng = False
            if i_dex >  11:
                self.switchToTab2(driver, logging)
                tab_chng = True
                i_dex = i_dex - 12

            logging.info('i_dex {}'.format(i_dex))
            ele = driver.find_elements_by_xpath("//div[contains(@class, 'vddl-draggable') and contains(@class, 'instrument')]")[i_dex]
            logging.info('BO {}'.format(2))
            items1 = ele.find_element_by_xpath(".//div[contains(@class, 'info')]")
            logging.info('BO {}'.format(3))
            script = items1.find_element_by_xpath(".//span[contains(@class, 'nice-name')]").text
            print('SCRIPT found',script,'to be checked with', STOCK_)
            logging.info('BO {}'.format(4))
            logging.info('SCRIPT found {} to be checked with {}'.format(script, STOCK_))
        except Exception as e:
            noError = False
            print('Element not found in BUY_SELL ',e)
            logging.info('Element not found in BUY_SELL {}'.format(e))
        

        if script == STOCK_:
            logging.info('BO {}'.format(5))
            print('Script match = SUCCESS')
            logging.info('Script match = SUCCESS')
            print('hover and buy/sell')
            logging.info('hover and buy/sell')
            try:
                logging.info('BO {}'.format(6))
                Hover = ActionChains(driver).move_to_element(items1)
                Hover.perform()
                logging.info('BO {}'.format(7))
                time.sleep(.3)
                elebuy = WebDriverWait(driver,1, 1).until(            
                        expect.element_to_be_clickable(
                        (By.XPATH,"//button[contains(@class,'"+TRADE+"')]")))
                logging.info('BO {}'.format(8))
                elebuy.click()              
            except Exception as e:
                noError = False
                print('Error performing hover and buy/sell', e)
                logging.info('Error performing hover and buy/sell {}'.format(e))

                
            print('Buy Button Clicked')
            logging.info('Buy Button Clicked')
            
          
            time.sleep(2)
            
    ## MORE OPTIONS
            if ORDER_TYPE == 'MIS':
                print('cliking MIS')
                logging.info('cliking MIS')
                self.doBodyClick(driver, logging)
                try:
                    elemMIS = WebDriverWait(driver, 2).until(
                            expect.element_to_be_clickable(
                            (By.XPATH,"//label[contains(text(),'MIS')]")))
##                    elemMIS = WebDriverWait(driver,2).until(
##                            expect.visibility_of_element_located(
##                            (By.XPATH,"//label[contains(text(),'MIS')]")))                    
##                    elemMIS = WebDriverWait(driver, 2).until(
##                            expect.element_to_be_clickable(
##                            (By.CSS_SELECTOR,"input[type='radio'][value='MIS']")))
##                    elemMIS = driver.find_element_by_css_selector("input[type='radio'][value='MIS']")
                    driver.execute_script("arguments[0].click();", elemMIS)
                    result_mis = driver.execute_script("return document.querySelector('input[type=\"radio\"][value=\"MIS\"]').checked")
                    if result_mis == True:
                        print('MIS radio selected.', result_mis)
                        logging.info('MIS radio selected.')
                    logging.info('BO {}'.format(12))
##                    elemMIS.click()
                    time.sleep(.2)
                    logging.info('BO {}'.format(13))
##                    if elemMIS.is_selected() == True:
##                        logging.info('MIS radio is selected.')
##                        
                except Exception as e: ## "//input[@value='bo' and @type='radio']"
                    noError = False
                    print('error finding MIS radio button', e)
                    logging.info('error finding MIS radio button. trying again.')
                    time.sleep(.5)    

                time.sleep(1)                
            else:                
                print('cliking more options')
                logging.info('cliking more options')
                self.doBodyClick(driver, logging)
                try:
                    logging.info('BO {}'.format(9))
                    eleMoreoptions = WebDriverWait(driver,2).until(            
                            expect.element_to_be_clickable(
                            (By.XPATH,"//a[@class='advanced-options-open']")))
                    logging.info('BO {}'.format(10))
                    eleMoreoptions.click()
                    logging.info('BO {}'.format(11))
    ##                print(6)
                    time.sleep(.5)
                except Exception as e:
    ##                noError = False
                    print('more options tag not found')      
                    logging.info('more options tag not found')         

        ## REGULAR RADIO
                print('REGULAR radio')
                logging.info('REGULAR radio')
                self.doBodyClick(driver, logging)
                try:
                    elemRg = WebDriverWait(driver, 2).until(
                            expect.element_to_be_clickable(
                            (By.XPATH,"//label[contains(text(),'regular')]")))
##                    elemRg = WebDriverWait(driver, 2).until(
##                            expect.element_to_be_clickable(
##                            (By.CSS_SELECTOR,"input[type='radio'][value='regular']")))                     
    ##                print(7)
                    logging.info('BO {}'.format(11.1))
##                    elemRg.click()
                    driver.execute_script("arguments[0].click();", elemRg)                    
                    time.sleep(.2)
                    result_rg = driver.execute_script("return document.querySelector('input[type=\"radio\"][value=\"regular\"]').checked")
                    if result_rg == True:
                        print('Regular radio selected.', result_rg)
                        logging.info('Regular radio selected.')                  
                    logging.info('BO {}'.format(11.2))
                except Exception as e: ## "//input[@value='bo' and @type='radio']"                
                    print('error finding regular radio button', e)
                    logging.info('error finding regular radio button. trying again.')
                    
                time.sleep(.5)
                

    ## BO RADIO
            if ORDER_TYPE == 'BO':
                print('bo radio')
                logging.info('bo radio')
                self.doBodyClick(driver, logging)
                try:
                    elemBO = WebDriverWait(driver, 2).until(
                            expect.element_to_be_clickable(
                            (By.XPATH,"//label[contains(text(),'bo')]")))
##                    elemBO = WebDriverWait(driver, 2).until(
##                            expect.element_to_be_clickable(
##                            (By.CSS_SELECTOR,"input[type='radio'][value='bo']")))                     
    ##                print(7)
                    logging.info('BO {}'.format(12))
##                    elemBO.click()
                    driver.execute_script("arguments[0].click();", elemBO) 
                    time.sleep(.2)
                    result_bo = driver.execute_script("return document.querySelector('input[type=\"radio\"][value=\"bo\"]').checked")
                    if result_bo == True:
                        print('BO radio selected.', result_bo)
                        logging.info('BO radio selected.')
                    logging.info('BO {}'.format(13))
                except Exception as e: ## "//input[@value='bo' and @type='radio']"
                    noError = False
                    print('error finding BO radio button', e)
                    logging.info('error finding BO radio button. trying again.')
                    time.sleep(.5)
                time.sleep(1)

    ## click SL order
            if SLORDER == True:            
                try:
                    self.doBodyClick(driver, logging)
                    logging.info('BO {}'.format(14))
                    print('sl radio button')
                    logging.info('sl radio button')
                    elemSL = WebDriverWait(driver,2).until(
                            expect.element_to_be_clickable(
                            (By.XPATH,"//label[contains(text(),'SL')]")))
##                    elemSL = WebDriverWait(driver, 2).until(
##                            expect.element_to_be_clickable(
##                            (By.CSS_SELECTOR,"input[type='radio'][value='SL']")))                                         
                    logging.info('BO {}'.format(15))
##                    elemSL.click()
                    driver.execute_script("arguments[0].click();", elemSL)                     
                    time.sleep(.2)
                    result_sl = driver.execute_script("return document.querySelector('input[type=\"radio\"][value=\"SL\"]').checked")
                    if result_sl == True:
                        print('sl radio selected.', result_sl)
                        logging.info('sl radio selected.')                    
                    logging.info('BO {}'.format(16))
                except Exception as e: ## "//input[@value='bo' and @type='radio']"
                    noError = False
                    print('error finding SL radio button', e)
                    logging.info('error finding SL radio button {}'.format(e))
                time.sleep(.5)
            else:
                try:
                    self.doBodyClick(driver, logging)
                    logging.info('BO {}'.format(16.1))
                    print('LIMIT radio button')
                    logging.info('LIMIT radio button')
                    elemLMT = WebDriverWait(driver,2).until(
                            expect.element_to_be_clickable(
                            (By.XPATH,"//label[contains(text(),'LIMIT')]")))                                      
                    logging.info('BO {}'.format(16.2))
##                    elemLMT.click()
                    driver.execute_script("arguments[0].click();", elemLMT)                    
                    time.sleep(.2)
                    result_lmt = driver.execute_script("return document.querySelector('input[type=\"radio\"][value=\"LIMIT\"]').checked")                    
                    if result_lmt == True:
                        print('Limit radio selected.', result_lmt)
                        logging.info('Limit radio selected.')                   
                    logging.info('BO {}'.format(16.3))
                except Exception as e: ## "//input[@value='bo' and @type='radio']"
                    noError = False
                    print('error finding LIMIT radio button', e)
                    logging.info('error finding LIMIT radio button {}'.format(e))
                time.sleep(.5)                

                            
    ##-------------------------------------------------------------------------------------------------------------        
    ##fill in form details.
            #driver.find_element_by_tag_name("body").click()
            self.doBodyClick(driver, logging)
            try:
                logging.info('BO {}'.format(17))
                print('qty form')
                logging.info('qty form')
                CLEAR_QTY = WebDriverWait (driver,2).until(expect.element_to_be_clickable((By.XPATH,"//input[@label='Qty.']")))
                CLEAR_QTY.click()
                time.sleep(.2)
                CLEAR_QTY.clear()
                logging.info('BO {}'.format(18))
                #driver.find_element_by_tag_name("body").click()
                self.doBodyClick(driver, logging)
                print('qty form clear. enter values now')
                logging.info('qty form clear. enter values now')
                elemQTY = WebDriverWait(driver,2).until(
                        expect.visibility_of_element_located(
                        (By.XPATH,"//input[@label='Qty.']")))
    ##            time.sleep(.2)
                logging.info('BO {}'.format(19))
                elemQTY.send_keys(str(QTY))
                logging.info('BO {}'.format(20))
            except Exception as e: ## "//input[@value='bo' and @type='radio']"
                print('error QTY input', e)
                noError = False
                logging.info('error QTY input {}'.format(e))     
            time.sleep(.5)
            
            try:
                CLEAR_ENTRY = WebDriverWait (driver,2).until(expect.element_to_be_clickable((By.XPATH,"//input[@label='Price']")))
                logging.info('BO {}'.format(20.1))
                CLEAR_ENTRY.click()
                logging.info('BO {}'.format(20.2))
                time.sleep(.3)
                CLEAR_ENTRY.clear()
                logging.info('BO {}'.format(21))
                #driver.find_element_by_tag_name("body").click()
                self.doBodyClick(driver, logging)
                elemEntry = WebDriverWait(driver,2).until(
                        expect.visibility_of_element_located(
                        (By.XPATH,"//input[@label='Price']")))
##                print(10)            
                time.sleep(.2)
                logging.info('BO {}'.format(22))
                elemEntry.send_keys(str(ENTRYPRICE))
                logging.info('BO {}'.format(23))
            except Exception as e:
                noError = False
                print('error Entry price input', e) 
                logging.info('error Entry price input {}'.format(e))
            time.sleep(.5)
            
            if SLORDER == True:            
                try:
                    logging.info('BO {}'.format(24))
                    CLEAR_TRIGGER = WebDriverWait (driver, 2).until(expect.element_to_be_clickable((By.XPATH,"//input[@label='Trigger price']")))
                    CLEAR_TRIGGER.click()
                    time.sleep(.3)
                    CLEAR_TRIGGER.clear()
##                    print(11)
                    #driver.find_element_by_tag_name("body").click()
                    self.doBodyClick(driver, logging)
                    logging.info('BO {}'.format(25))
                    elemtrigger = WebDriverWait(driver,2).until(
                            expect.visibility_of_element_located(
                            (By.XPATH,"//input[@label='Trigger price']")))
                    logging.info('BO {}'.format(26))
                    time.sleep(.2)
                    elemtrigger.send_keys(str(ENTRYPRICE))
                    logging.info('BO {}'.format(27))
                except Exception as e: ## "//input[@value='bo' and @type='radio']"
                    noError = False
                    print('error trigger price input', e) 
                    logging.info('error trigger price input'.format(e))
            time.sleep(.2)
            if ORDER_TYPE == 'BO':                
                try:
                    logging.info('BO {}'.format(28))
                    elemABS_SL = WebDriverWait(driver,2).until(
                            expect.visibility_of_element_located(
                            (By.XPATH,"//input[@label='Stoploss']")))
                    elemABS_SL.send_keys(Keys.CONTROL + "a");
                    logging.info('BO {}'.format(28))
                    time.sleep(.5)
                    elemABS_SL.send_keys(Keys.DELETE);
                    logging.info('BO {}'.format(29))
                    elemABS_SL.send_keys(str(ABS_SL))
                    logging.info('BO {}'.format(30))
                except Exception as e: ## "//input[@value='bo' and @type='radio']"
                    noError = False
                    print('error SL input', e)
                    logging.info('error SL input {}'.format(e))
                time.sleep(.5)
                try:
                    logging.info('BO {}'.format(31))
                    elemABS_TGT = WebDriverWait(driver, 2).until(
                            expect.visibility_of_element_located(
                            (By.XPATH,"//input[@label='Target']")))
                    logging.info('BO {}'.format(32))
                    elemABS_TGT.send_keys(Keys.CONTROL + "a");
                    logging.info('BO {}'.format(33))
                    elemABS_TGT.send_keys(Keys.DELETE);
                    time.sleep(.3)
                    logging.info('BO {}'.format(34))
                    elemABS_TGT.send_keys(str(ABS_TGT))
                    logging.info('BO {}'.format(35))
                except Exception as e: ## "//input[@value='bo' and @type='radio']"
                    noError = False
                    print('error Tgt input', e)
                    logging.info('error Tgt input {}'.format(e))

                time.sleep(.5)## wait to verify
##            place button-blue
            if noError == True:                
                try:
                    logging.info('BO {}'.format(36))
                    elemPlaceOrder = WebDriverWait(driver,2).until(
                            expect.visibility_of_element_located(
                            (By.XPATH,"//button[@type='submit' and contains(@class,'"+TRADE+"')]")))
                    ##'" + state + "'
                    logging.info('BO {}'.format(37))
                    elemPlaceOrder.click()
                    logging.info('BO {}'.format(38))
                except Exception as e: ## "//input[@value='bo' and @type='radio']"
                    noError = False
                    print('error placing order', e)
                    logging.info('error placing order {}'.format(e))
                time.sleep(2)
            else:
                print('noError == False, no order place.')
                logging.info('noError == False, no order place.')
                
            try:
                logging.info('BO {}'.format(39))
                ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                logging.info('BO {}'.format(40))
                if tab_chng:
                    self.switchToTab1(driver, logging)
            except Exception as e:                
                print('Error sending escape key.',e)
                logging.info('Error sending escape key. {}'.format(e))
            print('buy/sell completed successfully.')
            logging.info('buy/sell completed successfully.')

    def BUY_SELL_CO(self, logging, driver, TRADE, QTY, ENTRYPRICE, STOP, i_dex, STOCK_):
        try:
            HoverClass = 'button-orange' if TRADE == 'Sell' else 'button-blue'
            noError = True
            logging.info('BO {}'.format(1)) 
            print('i_dex', i_dex)
            tab_chng = False
            if i_dex >  11:
                self.switchToTab2(driver, logging)
                tab_chng = True
                i_dex = i_dex - 12

            logging.info('i_dex {}'.format(i_dex))
            ele = driver.find_elements_by_xpath("//div[contains(@class, 'vddl-draggable') and contains(@class, 'instrument')]")[i_dex]
            logging.info('BO {}'.format(2))
            items1 = ele.find_element_by_xpath(".//div[contains(@class, 'info')]")
            logging.info('BO {}'.format(3))
            script = items1.find_element_by_xpath(".//span[contains(@class, 'nice-name')]").text
            print('SCRIPT found',script,'to be checked with', STOCK_)
            logging.info('BO {}'.format(4))
            logging.info('SCRIPT found {} to be checked with {}'.format(script, STOCK_))
        except Exception as e:
            noError = False
            print('Element not found in BUY_SELL ',e)
            logging.info('Element not found in BUY_SELL {}'.format(e))

        if script == STOCK_:
            logging.info('BO {}'.format(5))
            print('Script match = SUCCESS')
            logging.info('Script match = SUCCESS')
            print('hover and buy/sell')
            logging.info('hover and buy/sell')
            try:
                logging.info('BO {}'.format(6))
                Hover = ActionChains(driver).move_to_element(items1)
                Hover.perform()
                logging.info('BO {}'.format(7))
                time.sleep(.3)
                elebuy = WebDriverWait(driver,1, 1).until(            
                        expect.element_to_be_clickable(
                        (By.XPATH,"//button[contains(@class,'"+HoverClass+"')]")))
                logging.info('BO {}'.format(8))
                elebuy.click()              
            except Exception as e:
                noError = False
                print('Error performing hover and buy/sell', e)
                logging.info('Error performing hover and buy/sell {}'.format(e))

                
            print('Button Clicked')
            logging.info('Button Clicked')
            time.sleep(2)
            timer_ = 0.3
            try:             
                noError = self.coverOrderRadio(driver, logging)               
                time.sleep(timer_)
                noError = self.ClickLimitRadio(driver, logging)
                time.sleep(timer_)
                noError = self.enterQty(driver, logging, QTY)
                time.sleep(timer_) ##SLPrice   LimitEntryPrice
                noError = self.LimitEntryPrice(driver, logging, ENTRYPRICE)
                time.sleep(timer_)
                noError = self.SLPrice(driver, logging, STOP)
                time.sleep(timer_)
                
                if noError == True:                
                    try:
                        logging.info('BO {}'.format(36))
##                        elemPlaceOrder = WebDriverWait(driver,2).until(
##                                expect.visibility_of_element_located(
##                                (By.XPATH,"//button[@type='submit' and contains(@class,'"+TRADE+"')]")))
                        elemPlaceOrder = WebDriverWait(driver,2).until(
                                expect.visibility_of_element_located(
                                (By.XPATH,"//button[@type='submit' and contains(@class,'submit')]//span[contains(text(), '"+TRADE+"')]")))
                        logging.info('BO {}'.format(37))
                        elemPlaceOrder.click()
                        logging.info('BO {}'.format(38))
                    except Exception as e: ## "//input[@value='bo' and @type='radio']"
                        noError = False
                        print('error placing order', e)
                        logging.info('error placing order {}'.format(e))
                    time.sleep(.3)
                else:
                    print('noError == False, no order place.')
                    logging.info('noError == False, no order place.')
                    
                try:
                    logging.info('BO {}'.format(39))
                    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                    logging.info('BO {}'.format(40))
                except Exception as e:                
                    print('Error sending escape key.',e)
                    logging.info('Error sending escape key. {}'.format(e))
                print('buy/sell completed successfully.')
                logging.info('buy/sell completed successfully.')
            except Exception as e:
                print('Error in one of the function.{}'.format(e))
                logging.info('Error in one of the function.{}'.format(e))                
                            


    def BUY_SELL_SLM(self, logging, driver, TRADE, QTY, ENTRYPRICE, STOP, ABS_SL, ABS_TGT, i_dex, STOCK_):
        try:
            HoverClass = 'button-orange' if TRADE == 'Sell' else 'button-blue'
            noError = True
            logging.info('BO {}'.format(1)) 
            print('i_dex', i_dex)
            tab_chng = False
            if i_dex >  11:
                self.switchToTab2(driver, logging)
                tab_chng = True
                i_dex = i_dex - 12

            logging.info('i_dex {}'.format(i_dex))
            ele = driver.find_elements_by_xpath("//div[contains(@class, 'vddl-draggable') and contains(@class, 'instrument')]")[i_dex]
            logging.info('BO {}'.format(2))
            items1 = ele.find_element_by_xpath(".//div[contains(@class, 'info')]")
            logging.info('BO {}'.format(3))
            script = items1.find_element_by_xpath(".//span[contains(@class, 'nice-name')]").text
            print('SCRIPT found',script,'to be checked with', STOCK_)
            logging.info('BO {}'.format(4))
            logging.info('SCRIPT found {} to be checked with {}'.format(script, STOCK_))
        except Exception as e:
            noError = False
            print('Element not found in BUY_SELL ',e)
            logging.info('Element not found in BUY_SELL {}'.format(e))
        

        if script == STOCK_:
            logging.info('BO {}'.format(5))
            print('Script match = SUCCESS')
            logging.info('Script match = SUCCESS')
            print('hover and buy/sell')
            logging.info('hover and buy/sell')
            try:
                logging.info('BO {}'.format(6))
                Hover = ActionChains(driver).move_to_element(items1)
                Hover.perform()
                logging.info('BO {}'.format(7))
                time.sleep(.3)
                elebuy = WebDriverWait(driver,1, 1).until(            
                        expect.element_to_be_clickable(
                        (By.XPATH,"//button[contains(@class,'"+HoverClass+"')]")))
                logging.info('BO {}'.format(8))
                elebuy.click()              
            except Exception as e:
                noError = False
                print('Error performing hover and buy/sell', e)
                logging.info('Error performing hover and buy/sell {}'.format(e))

                
            print('Buy Button Clicked')
            logging.info('Buy Button Clicked')
            time.sleep(2)
            timer_ = 0.3
            try:
             
                noError = self.regularRadio(driver, logging)               
                time.sleep(timer_)
                noError = self.MISRadio(driver, logging)
                time.sleep(timer_)
                noError = self.slmRadio(driver, logging)
                time.sleep(timer_)
                noError = self.enterQty(driver, logging, QTY)
                time.sleep(timer_)
                noError = self.triggerPrice(driver, logging, ENTRYPRICE)
                time.sleep(timer_)

                
                if noError == True:                
                    try:
                        logging.info('BO {}'.format(36))
##                        elemPlaceOrder = WebDriverWait(driver,2).until(
##                                expect.visibility_of_element_located(
##                                (By.XPATH,"//button[@type='submit' and contains(@class,'"+TRADE+"')]")))
                        elemPlaceOrder = WebDriverWait(driver,2).until(
                                expect.visibility_of_element_located(
                                (By.XPATH,"//button[@type='submit' and contains(@class,'submit')]//span[contains(text(), '"+TRADE+"')]")))
                        logging.info('BO {}'.format(37))
                        elemPlaceOrder.click()
                        logging.info('BO {}'.format(38))
                    except Exception as e: ## "//input[@value='bo' and @type='radio']"
                        noError = False
                        print('error placing order', e)
                        logging.info('error placing order {}'.format(e))
                    time.sleep(.3)
                else:
                    print('noError == False, no order place.')
                    logging.info('noError == False, no order place.')
                    
                try:
                    logging.info('BO {}'.format(39))
                    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                    logging.info('BO {}'.format(40))
                    if tab_chng:
                        self.switchToTab1(driver, logging)
                except Exception as e:                
                    print('Error sending escape key.',e)
                    logging.info('Error sending escape key. {}'.format(e))
                print('buy/sell completed successfully.')
                logging.info('buy/sell completed successfully.')
            except Exception as e:
                print('Error in one of the function.{}'.format(e))
                logging.info('Error in one of the function.{}'.format(e))                
                
