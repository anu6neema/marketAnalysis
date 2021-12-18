##import pandas as pd
class patterns:
    def candleGreenRed(self, df_):
        chk     = 'NONE'
        try:            
            OPEN    = float(df_['OPEN'])
            HIGH    = float(df_['HIGH'])
            LOW     = float(df_['LOW'])
            CLOSE   = float(df_['CLOSE'])
            if OPEN > CLOSE:
                chk = 'RED'
            elif CLOSE > OPEN:
                chk = 'GREEN'
        except Exception as e:
            print(e)
        return chk        

    def IsCandleBigBody(self, df_):
        chk     = False
        GR = self.candleGreenRed(df_)
        try:            
            OPEN    = float(df_['OPEN'])
            HIGH    = float(df_['HIGH'])
            LOW     = float(df_['LOW'])
            CLOSE   = float(df_['CLOSE'])

            BODY = abs(CLOSE - OPEN)
            if GR =='GREEN':
                UWICK = HIGH - CLOSE
                LWICK = OPEN - LOW
            elif GR == 'RED':
                UWICK = HIGH - OPEN
                LWICK = CLOSE - LOW

            if GR != 'NONE':                
                if BODY > 1.5*UWICK and BODY > 1.5*LWICK:
                    chk = True  
                
        except Exception as e:
            print(e)
            chk = False
        return chk 

    def IsCandleMediumBody(self, df_):
        chk     = False
        GR = self.candleGreenRed(df_)
        try:            
            OPEN    = float(df_['OPEN'])
            HIGH    = float(df_['HIGH'])
            LOW     = float(df_['LOW'])
            CLOSE   = float(df_['CLOSE'])

            BODY = abs(CLOSE - OPEN)
            if GR =='GREEN':
                UWICK = HIGH - CLOSE
                LWICK = OPEN - LOW
            elif GR == 'RED':
                UWICK = HIGH - OPEN
                LWICK = CLOSE - LOW

            if GR != 'NONE':                
                if BODY > UWICK + LWICK:
                    chk = True  
##            if GR != 'NONE':                
##                if BODY > UWICK and BODY > LWICK:
##                    chk = True                 
        except Exception as e:
            print(e)
            chk = False
        return chk 

    def IsCandlePinbar(self, df_, UPDOWN ,color = 'NONE'):
        chk = False       
        if color == 'NONE':
            GR = self.candleGreenRed(df_)
        else:
            GR = color
        try:            
            OPEN    = float(df_['OPEN'])
            HIGH    = float(df_['HIGH'])
            LOW     = float(df_['LOW'])
            CLOSE   = float(df_['CLOSE'])
            BODY = abs(CLOSE - OPEN)
            if GR =='GREEN' and CLOSE > OPEN:
                UWICK = HIGH - CLOSE
                LWICK = OPEN - LOW
                if UPDOWN == 'UP' and LWICK > 1.5*BODY and LWICK > 2*UWICK:
                    chk = True
                elif UPDOWN == 'DOWN' and UWICK >1.5*BODY and UWICK > 2*LWICK:
                    chk = True
                elif UPDOWN == 'UP' and BODY > 2*LWICK and LWICK > 2*UWICK:
                    chk = True
##                elif UPDOWN == 'UP' and BODY > LWICK and LWICK > 2*UWICK:
##                    chk = True                     
            elif GR == 'RED' and CLOSE < OPEN:
                UWICK = HIGH - OPEN
                LWICK = CLOSE - LOW
                if UPDOWN == 'UP' and LWICK > 1.5*BODY and LWICK > 2*UWICK:
                    chk = True
                elif UPDOWN == 'DOWN' and UWICK > 1.5*BODY and UWICK > 2*LWICK:
                    chk = True
                elif UPDOWN == 'DOWN' and BODY > 2*LWICK and UWICK > 2*LWICK:
                    chk = True
##                elif UPDOWN == 'DOWN' and BODY > UWICK and UWICK > 2*LWICK:
##                    chk = True                      
        except Exception as e:
            print(e)
            chk = False
        return chk

    def IsCandleDoji(self, df_, color = 'NONE'):
        chk = False       
        if color == 'NONE':
            GR = self.candleGreenRed(df_)
        else:
            GR = color
        try:            
            OPEN    = float(df_['OPEN'])
            HIGH    = float(df_['HIGH'])
            LOW     = float(df_['LOW'])
            CLOSE   = float(df_['CLOSE'])
            BODY = abs(CLOSE - OPEN)
            if GR =='GREEN' and CLOSE > OPEN:
                UWICK = HIGH - CLOSE
                LWICK = OPEN - LOW
                if UWICK > BODY and LWICK > BODY:
                    chk = True

            elif GR == 'RED' and CLOSE < OPEN:
                UWICK = HIGH - OPEN
                LWICK = CLOSE - LOW
                if UWICK > BODY and LWICK > BODY:
                    chk = True
             
        except Exception as e:
            print(e)
            chk = False
        return chk

## multi candle patterns.#####################################    
    def BearThreeCandles1(self, Stock_df):
        ##First Candle greenBB.
        ##Second candle red, BB, IB
        ##third candle red.
        chk = False 
        try:
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            OPEN3   = float(Stock_df.iloc[2]['OPEN'])
            HIGH3   = float(Stock_df.iloc[2]['HIGH'])
            LOW3    = float(Stock_df.iloc[2]['LOW'])
            CLOSE3  = float(Stock_df.iloc[2]['CLOSE'])

            if self.candleGreenRed(Stock_df.iloc[0]) == 'GREEN' and \
               self.IsCandleBigBody(Stock_df.iloc[0]) and \
               self.candleGreenRed(Stock_df.iloc[1]) == 'RED'   and \
               self.IsCandleBigBody(Stock_df.iloc[1]) and \
               CLOSE2 < (OPEN1+CLOSE1)/2 and \
               self.candleGreenRed(Stock_df.iloc[2]) == 'RED':
                print('BearThreeCandles1')
                chk = True                

        except Exception as e:
            print(e)
            chk = False
        return chk ##[stock, QTY, SL, TGT, abs_sl, abs_tgt, trade]
    
    def BullThreeCandles1(self, Stock_df):
        ##First Candle RED BB.
        ##Second candle GREEN, BB, IB
        ##third candle red.
        chk = False 
        try:
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            OPEN3   = float(Stock_df.iloc[2]['OPEN'])
            HIGH3   = float(Stock_df.iloc[2]['HIGH'])
            LOW3   = float(Stock_df.iloc[2]['LOW'])
            CLOSE3  = float(Stock_df.iloc[2]['CLOSE'])

            if self.candleGreenRed(Stock_df.iloc[0]) == 'RED' and \
               self.IsCandleBigBody(Stock_df.iloc[0]) and \
               self.candleGreenRed(Stock_df.iloc[1]) == 'GREEN'   and \
               self.IsCandleBigBody(Stock_df.iloc[1]) and \
               CLOSE2 > (OPEN1+CLOSE1)/2 and \
               self.candleGreenRed(Stock_df.iloc[2]) == 'GREEN':
                print('BullThreeCandles1')
                chk = True                

        except Exception as e:
            print(e)
            chk = False
        return chk ##[stock, QTY, SL, TGT, abs_sl, abs_tgt, trade]


    def BearThreeCandles2(self, Stock_df):
        ##First Candle green .
        ##Second candle GREEN/RED. must be smaller than first
        ##third candle red Big body. Closing below mid of first.
        chk = False 
        try:
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            OPEN3   = float(Stock_df.iloc[2]['OPEN'])
            HIGH3   = float(Stock_df.iloc[2]['HIGH'])
            LOW3   = float(Stock_df.iloc[2]['LOW'])
            CLOSE3  = float(Stock_df.iloc[2]['CLOSE'])

            if self.candleGreenRed(Stock_df.iloc[0]) == 'GREEN' and \
               (HIGH2 - LOW2) < (HIGH1 - LOW1) and \
               CLOSE3 < (OPEN1+CLOSE1)/2 and \
               self.candleGreenRed(Stock_df.iloc[2]) == 'RED' and \
               self.IsCandleBigBody(Stock_df.iloc[2]):                
                print('BearThreeCandles2')
                chk = True
                
        except Exception as e:
            print(e)
            chk = False
        return chk ##[stock, QTY, SL, TGT, abs_sl, abs_tgt, trade]

    def BullThreeCandles2(self, Stock_df):
        ##First Candle green .
        ##Second candle GREEN/RED. must be smaller than first
        ##third candle red Big body. Closing below mid of first.
        chk = False 
        try:
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            OPEN3   = float(Stock_df.iloc[2]['OPEN'])
            HIGH3   = float(Stock_df.iloc[2]['HIGH'])
            LOW3   = float(Stock_df.iloc[2]['LOW'])
            CLOSE3  = float(Stock_df.iloc[2]['CLOSE'])

            if self.candleGreenRed(Stock_df.iloc[0]) == 'RED' and \
               (HIGH2 - LOW2) < (HIGH1 - LOW1) and \
               CLOSE3 > (OPEN1+CLOSE1)/2 and \
               self.candleGreenRed(Stock_df.iloc[2]) == 'GREEN' and \
               self.IsCandleBigBody(Stock_df.iloc[2]):                
                print('BullThreeCandles2')
                chk = True
                
        except Exception as e:
            print(e)
            chk = False
        return chk ##[stock, QTY, SL, TGT, abs_sl, abs_tgt, trade]


    def BearThreeCandles3(self, Stock_df):
        ##First Candle RED doji/pin .
        ##Second candle PIN down,  GREEN/RED. 
        ##third candle down pin, high of second break, and closing below mid of first.  
        chk = False 
        try:
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            OPEN3   = float(Stock_df.iloc[2]['OPEN'])
            HIGH3   = float(Stock_df.iloc[2]['HIGH'])
            LOW3   = float(Stock_df.iloc[2]['LOW'])
            CLOSE3  = float(Stock_df.iloc[2]['CLOSE'])

            if self.candleGreenRed(Stock_df.iloc[0]) == 'RED' and \
               self.IsCandlePinbar(Stock_df.iloc[1],'DOWN') and \
               self.IsCandlePinbar(Stock_df.iloc[2],'DOWN','RED') and \
               HIGH3 > HIGH2 and CLOSE3 < (HIGH1+LOW1)/2:    
                print('BearThreeCandles3')
                chk = True
                
        except Exception as e:
            print(e)
            chk = False
        return chk ##[stock, QTY, SL, TGT, abs_sl, abs_tgt, trade]

    def BullThreeCandles3(self, Stock_df):
        ##First Candle RED doji/pin .
        ##Second candle PIN down,  GREEN/RED. 
        ##third candle down pin, high of second break, and closing below mid of first.  
        chk = False 
        try:
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            OPEN3   = float(Stock_df.iloc[2]['OPEN'])
            HIGH3   = float(Stock_df.iloc[2]['HIGH'])
            LOW3   = float(Stock_df.iloc[2]['LOW'])
            CLOSE3  = float(Stock_df.iloc[2]['CLOSE'])

            if self.candleGreenRed(Stock_df.iloc[0]) == 'GREEN' and \
               self.IsCandlePinbar(Stock_df.iloc[1],'UP') and \
               self.IsCandlePinbar(Stock_df.iloc[2],'UP','GREEN') and \
               LOW3 < LOW2 and CLOSE3 > (HIGH1+LOW1)/2:    
                print('BullThreeCandles3')
                chk = True
                
        except Exception as e:
            print(e)
            chk = False
        return chk ##[stock, QTY, SL, TGT, abs_sl, abs_tgt, trade]

    def BullThreeReversalCandles5(self, Stock_df):
        ##First Candle RED Big body red. Very big in size.
        ##Second high below mid of first,  GREEN/RED.
        ## body size smaller than first one
        ## third candle high also below mid of first
        ## second candle low should be lower than third mid.
        ##third candle down pin, high of second break, and closing below mid of first.  
        chk = False 
        try:
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            MID1 = ( OPEN1 + HIGH1 + LOW1 + CLOSE1 )/ 4

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            MID2 = ( OPEN2 + HIGH2 + LOW2 + CLOSE2 )/ 4

            OPEN3   = float(Stock_df.iloc[2]['OPEN'])
            HIGH3   = float(Stock_df.iloc[2]['HIGH'])
            LOW3   = float(Stock_df.iloc[2]['LOW'])
            CLOSE3  = float(Stock_df.iloc[2]['CLOSE'])

            MID3 = ( OPEN3 + HIGH3 + LOW3 + CLOSE3 )/ 4

            if self.candleGreenRed(Stock_df.iloc[0]) == 'RED' and \
               (HIGH1 - LOW1) > 1.2*(HIGH2-LOW2) and CLOSE3 > HIGH1 and CLOSE2 > HIGH1 and\
               MID3 > MID2:            
                chk = True
                print('BullThreeReversalCandles5')
                
        except Exception as e:
            print(e)
            chk = False
        return chk ##[stock, QTY, SL, TGT, abs_sl, abs_tgt, trade]


    def BearThreeReversalCandles5(self, Stock_df):
        ##First Candle GREEB Big body. Very big in size.
        ##Second high below mid of first,  GREEN/RED.
        ## body size smaller than first one
        ## third candle high also above mid of first
        ## second candle high should be higher than third mid.
        ##third candle down pin, high of second break, and closing below mid of first.

        ## MID OF SECOND AND THIRD CANDLE.
        chk = False 
        try:
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            MID1 = ( OPEN1 + HIGH1 + LOW1 + CLOSE1 )/ 4

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            MID2 = ( OPEN2 + HIGH2 + LOW2 + CLOSE2 )/ 4

            OPEN3   = float(Stock_df.iloc[2]['OPEN'])
            HIGH3   = float(Stock_df.iloc[2]['HIGH'])
            LOW3   = float(Stock_df.iloc[2]['LOW'])
            CLOSE3  = float(Stock_df.iloc[2]['CLOSE'])

            MID3 = ( OPEN3 + HIGH3 + LOW3 + CLOSE3 )/ 4

            if self.candleGreenRed(Stock_df.iloc[0]) == 'GREEN' and \
               (HIGH1 - LOW1) > 1.2*(HIGH2-LOW2) and CLOSE3 < HIGH1 and CLOSE2 < HIGH1 and \
                MID3 < MID2:
                chk = True
                print('BearThreeReversalCandles5')
                
        except Exception as e:
            print(e)
            chk = False
        return chk ##[stock, QTY, SL, TGT, abs_sl, abs_tgt, trade]

    def BearThreeContinuationCandles4(self, Stock_df):
        ##First Candle RED Big body red. Very big in size.
        ##Second high below mid of first,  GREEN/RED.
        ## body size smaller than first one
        ## third candle high also below mid of first
        ## second candle low should be lower than third mid.
        ##third candle down pin, high of second break, and closing below mid of first.  
        chk = False 
        try:
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            MID1 = ( OPEN1 + HIGH1 + LOW1 + CLOSE1 )/ 4

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            MID2 = ( OPEN2 + HIGH2 + LOW2 + CLOSE2 )/ 4

            OPEN3   = float(Stock_df.iloc[2]['OPEN'])
            HIGH3   = float(Stock_df.iloc[2]['HIGH'])
            LOW3   = float(Stock_df.iloc[2]['LOW'])
            CLOSE3  = float(Stock_df.iloc[2]['CLOSE'])

            MID3 = ( OPEN3 + HIGH3 + LOW3 + CLOSE3 )/ 4

            if self.candleGreenRed(Stock_df.iloc[0]) == 'RED' and \
               (HIGH2 <= (HIGH1+LOW1)/2) and \
               (HIGH1 - LOW1) > 1.2*(HIGH2-LOW2) and \
               (HIGH1 - LOW1) < 5*(HIGH2-LOW2) and \
               MID3 < MID2:            
                chk = True
                print('BearThreeContinuationCandles4')
                
        except Exception as e:
            print(e)
            chk = False
        return chk ##[stock, QTY, SL, TGT, abs_sl, abs_tgt, trade]


    def BullThreeContinuationCandles4(self, Stock_df):
        ##First Candle GREEB Big body. Very big in size.
        ##Second high below mid of first,  GREEN/RED.
        ## body size smaller than first one
        ## third candle high also above mid of first
        ## second candle high should be higher than third mid.
        ##third candle down pin, high of second break, and closing below mid of first.

        ## MID OF SECOND AND THIRD CANDLE.
        chk = False 
        try:
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            MID1 = ( OPEN1 + HIGH1 + LOW1 + CLOSE1 )/ 4

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            MID2 = ( OPEN2 + HIGH2 + LOW2 + CLOSE2 )/ 4

            OPEN3   = float(Stock_df.iloc[2]['OPEN'])
            HIGH3   = float(Stock_df.iloc[2]['HIGH'])
            LOW3   = float(Stock_df.iloc[2]['LOW'])
            CLOSE3  = float(Stock_df.iloc[2]['CLOSE'])

            MID3 = ( OPEN3 + HIGH3 + LOW3 + CLOSE3 )/ 4

            if self.candleGreenRed(Stock_df.iloc[0]) == 'GREEN' and \
               (LOW2 >= (HIGH1+LOW1)/2) and \
               (HIGH1 - LOW1) > 1.2*(HIGH2-LOW2) and \
               (HIGH1 - LOW1) < 5*(HIGH2-LOW2) and \
                MID3 > MID2:
                chk = True
                print('BullThreeContinuationCandles4')
                
        except Exception as e:
            print(e)
            chk = False
        return chk ##[stock, QTY, SL, TGT, abs_sl, abs_tgt, trade]
    
    def BullTwoCandles1(self, Stock_df):###Bullish engulfing candles
        chk = False
        try: 
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            if self.candleGreenRed(Stock_df.iloc[1]) == 'GREEN' and \
               self.IsCandleBigBody(Stock_df.iloc[1]) == True and \
               self.candleGreenRed(Stock_df.iloc[0]) == 'RED':
                if HIGH2 > HIGH1 and LOW2 < LOW1:
                    print('Bullish engulfing candles')
                    chk = True
        except Exception as e:
            print(e)
            chk = False            
        return chk ##[stock, QTY, SL, TGT, abs_sl, abs_tgt, trade]

    def BullTwoCandles2(self, Stock_df): ###two bulish UP pins. second pin low lower than first one         
        chk = False
        try: 
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            if LOW2 < LOW1:
                if self.IsCandlePinbar(Stock_df.iloc[0],'UP','GREEN') and \
                   self.IsCandlePinbar(Stock_df.iloc[1],'UP','GREEN') and \
                   CLOSE2 > (HIGH1+LOW1) / 2:
                    chk = True
                    ## OPEN SHOULD BE GREATER THAN MID OF FIRST.
                elif self.IsCandleBigBody(Stock_df.iloc[0]) == True and \
                   self.candleGreenRed(Stock_df.iloc[0]) == 'GREEN' and \
                   self.IsCandlePinbar(Stock_df.iloc[1],'UP','GREEN') and \
                   CLOSE2 > (HIGH1+LOW1) / 2:                    
                    chk = True                                                                      
        except Exception as e:
            print(e)
            chk = False
            
        return chk ##[stock, QTY, SL, TGT, abs_sl, abs_tgt, trade]

    def BearTwoCandles1(self, Stock_df):###Bearish engulfing candles
        chk = False
        try: 
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            if self.candleGreenRed(Stock_df.iloc[1]) == 'RED' and \
               self.IsCandleBigBody(Stock_df.iloc[1]) == True and \
               self.candleGreenRed(Stock_df.iloc[0]) == 'GREEN':
                if HIGH2 > HIGH1 and LOW2 < LOW1:
                    print('Bearish engulfing candles')
                    chk = True
        except Exception as e:
            print(e)
            chk = False            
        return chk ##[stock, QTY, SL, TGT, abs_sl, abs_tgt, trade]

    def BearTwoCandles2(self, Stock_df): ###two Bearish down pins. second pin high higher than first one         
        chk = False
        try: 
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            if HIGH2 > HIGH1:
                if self.IsCandlePinbar(Stock_df.iloc[0],'DOWN','RED') and \
                   self.IsCandlePinbar(Stock_df.iloc[1],'DOWN','RED') and \
                   CLOSE2 < (HIGH1+LOW1) / 2:
                    chk = True
                    ## CLOSE SHOULD BE LESS THAN MID OF FIRST.
                elif self.IsCandleBigBody(Stock_df.iloc[0]) == True and \
                   self.candleGreenRed(Stock_df.iloc[0]) == 'RED' and \
                   self.IsCandlePinbar(Stock_df.iloc[1],'DOWN','RED') and \
                   CLOSE2 < (HIGH1+LOW1) / 2:                    
                    chk = True                                                                      
        except Exception as e:
            print(e)
            chk = False
            
        return chk ##[stock, QTY, SL, TGT, abs_sl, abs_tgt, trade]


    def BearThreeContinuationCandles5(self, Stock_df):
        chk = False 
        try:
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            MID1 = ( OPEN1 + HIGH1 + LOW1 + CLOSE1 )/ 4

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            MID2 = ( OPEN2 + HIGH2 + LOW2 + CLOSE2 )/ 4

            OPEN3   = float(Stock_df.iloc[2]['OPEN'])
            HIGH3   = float(Stock_df.iloc[2]['HIGH'])
            LOW3   = float(Stock_df.iloc[2]['LOW'])
            CLOSE3  = float(Stock_df.iloc[2]['CLOSE'])

            MID3 = ( OPEN3 + HIGH3 + LOW3 + CLOSE3 )/ 4

            if CLOSE2 < MID1 and \
               CLOSE3 < MID1:
                chk = True
                print('BearThreeContinuationCandles5')
                
        except Exception as e:
            print(e)
            chk = False
        return chk ##[stock, QTY, SL, TGT, abs_sl, abs_tgt, trade]


    def BullThreeContinuationCandles5(self, Stock_df):
        chk = False 
        try:
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            MID1 = ( OPEN1 + HIGH1 + LOW1 + CLOSE1 )/ 4

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            MID2 = ( OPEN2 + HIGH2 + LOW2 + CLOSE2 )/ 4

            OPEN3   = float(Stock_df.iloc[2]['OPEN'])
            HIGH3   = float(Stock_df.iloc[2]['HIGH'])
            LOW3   = float(Stock_df.iloc[2]['LOW'])
            CLOSE3  = float(Stock_df.iloc[2]['CLOSE'])

            MID3 = ( OPEN3 + HIGH3 + LOW3 + CLOSE3 )/ 4

            if CLOSE2 > MID1 and \
               CLOSE3 > MID1:
                chk = True
                print('BullThreeContinuationCandles5')
                
        except Exception as e:
            print(e)
            chk = False
        return chk ##[stock, QTY, SL, TGT, abs_sl, abs_tgt, trade]

###############################################################################

##    def BearRejectionTwoCandles(self, Stock_df):
##        chk = False 
##        try:
##            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
##            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
##            LOW1    = float(Stock_df.iloc[0]['LOW'])
##            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])
##
##            MID1 = ( OPEN1 + HIGH1 + LOW1 + CLOSE1 )/ 4
##
##            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
##            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
##            LOW2    = float(Stock_df.iloc[1]['LOW'])
##            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])
##
##            if self.candleGreenRed(Stock_df.iloc[0]) == 'RED' and \
##               self.IsCandleBigBody(Stock_df.iloc[0]) == True and \
##               self.IsCandlePinbar(Stock_df.iloc[1],'DOWN','RED'):
##                if HIGH2 > HIGH1 and CLOSE2 < MID1:
##                    print('BearRejectionTwoCandles')
##                    chk = True
##
##        except Exception as e:
##                    print(e)
##                    chk = False
##        return chk


    def BearRejectionTwoCandles(self, Stock_df):
        chk = False 
        try:
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            MID1 = ( OPEN1 + HIGH1 + LOW1 + CLOSE1 )/ 4

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            if self.IsCandlePinbar(Stock_df.iloc[1],'DOWN','RED'):
                if HIGH2 > HIGH1 and CLOSE2 < MID1:
                    print('BearRejectionTwoCandles')
                    chk = True

        except Exception as e:
                    print(e)
                    chk = False

        return chk

    def BullRejectionTwoCandles(self, Stock_df):
        chk = False 
        try:
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            MID1 = ( OPEN1 + HIGH1 + LOW1 + CLOSE1 )/ 4

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            if self.IsCandlePinbar(Stock_df.iloc[1],'UP','GREEN'):
                if LOW2 < LOW1 and CLOSE2 > MID1:
                    print('BullRejectionTwoCandles')
                    chk = True

        except Exception as e:
                    print(e)
                    chk = False
        return chk

    def BullEngulfingTwoCandles(self, Stock_df):###Bullish engulfing candles
        chk = False
        try: 
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            if self.candleGreenRed(Stock_df.iloc[1]) == 'GREEN' and \
               self.IsCandleBigBody(Stock_df.iloc[1]) == True:
                if HIGH2 > HIGH1 and LOW2 < LOW1:
                    print('Bullish engulfing candles')
                    chk = True
        except Exception as e:
            print(e)
            chk = False            
        return chk ##[stock, QTY, SL, TGT, abs_sl, abs_tgt, trade]            

    def BearEngulfingTwoCandles(self, Stock_df):###Bearish engulfing candles
        chk = False
        try: 
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            if self.candleGreenRed(Stock_df.iloc[1]) == 'RED' and \
               self.IsCandleBigBody(Stock_df.iloc[1]) == True:
                if HIGH2 > HIGH1 and LOW2 < LOW1:
                    print('Bearish engulfing candles')
                    chk = True
        except Exception as e:
            print(e)
            chk = False            
        return chk ##[stock, QTY, SL, TGT, abs_sl, abs_tgt, trade]

    def BearPiercingTwoCandles(self, Stock_df):###Bearish engulfing candles
        chk = False
        try: 
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])
            MID1 = ( OPEN1 + HIGH1 + LOW1 + CLOSE1 )/ 4
            
            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            if self.candleGreenRed(Stock_df.iloc[0]) == 'GREEN' and \
               self.candleGreenRed(Stock_df.iloc[1]) == 'RED' and \
               self.IsCandleBigBody(Stock_df.iloc[1]) == True and \
               CLOSE2 < MID1 and OPEN2 >= CLOSE1:
                print('BearPiercing')
                chk = True
        except Exception as e:
            print(e)
            chk = False            
        return chk ##[stock, QTY, SL, TGT, abs_sl, abs_tgt, trade]

    def BullPiercingTwoCandles(self, Stock_df):###Bearish engulfing candles
        chk = False
        try: 
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])
            MID1 = ( OPEN1 + HIGH1 + LOW1 + CLOSE1 )/ 4
            
            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            if self.candleGreenRed(Stock_df.iloc[0]) == 'RED' and \
               self.candleGreenRed(Stock_df.iloc[1]) == 'GREEN' and \
               self.IsCandleBigBody(Stock_df.iloc[1]) == True and \
               CLOSE2 > MID1 and OPEN2 <= CLOSE1:
                print('BullPiercing')
                chk = True
        except Exception as e:
            print(e)
            chk = False            
        return chk


    def BearishThreeEveningStar_IB(self, Stock_df):
        chk = False 
        try:
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            MID1 = ( OPEN1 + HIGH1 + LOW1 + CLOSE1 )/ 4

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            MID2 = ( OPEN2 + HIGH2 + LOW2 + CLOSE2 )/ 4

            OPEN3   = float(Stock_df.iloc[2]['OPEN'])
            HIGH3   = float(Stock_df.iloc[2]['HIGH'])
            LOW3   = float(Stock_df.iloc[2]['LOW'])
            CLOSE3  = float(Stock_df.iloc[2]['CLOSE'])

            MID3 = ( OPEN3 + HIGH3 + LOW3 + CLOSE3 )/ 4

            if self.candleGreenRed(Stock_df.iloc[0]) == 'GREEN' and self.IsCandleBigBody(Stock_df.iloc[0]) == True and \
               OPEN2 >= CLOSE1 and (HIGH2 - LOW2) < (HIGH1 - LOW1) and \
               self.candleGreenRed(Stock_df.iloc[2]) == 'RED' and CLOSE3 < MID1:
                print('BearishThreeEveningStar_IB1')
                chk = True

            if self.IsCandleBigBody(Stock_df.iloc[0]) == True and \
               HIGH2 < HIGH1 and LOW2 > LOW1 and \
               self.IsCandlePinbar(Stock_df.iloc[2],'DOWN','RED') and HIGH3 > HIGH1 and CLOSE3 < HIGH1:
                print('BearishThreeEveningStar_IB2')
                chk = True

            if HIGH2 < HIGH1 and LOW2 > LOW1 and \
               self.candleGreenRed(Stock_df.iloc[2]) == 'RED'  and CLOSE3 < LOW2:
                print('BearishThreeEveningStar_IB2')
                chk = True
                
        except Exception as e:
            print(e)
            chk = False
        return chk  


    def bullishThreeEveningStar_IB(self, Stock_df):
        chk = False 
        try:
            OPEN1   = float(Stock_df.iloc[0]['OPEN'])
            HIGH1   = float(Stock_df.iloc[0]['HIGH'])
            LOW1    = float(Stock_df.iloc[0]['LOW'])
            CLOSE1  = float(Stock_df.iloc[0]['CLOSE'])

            MID1 = ( OPEN1 + HIGH1 + LOW1 + CLOSE1 )/ 4

            OPEN2   = float(Stock_df.iloc[1]['OPEN'])
            HIGH2   = float(Stock_df.iloc[1]['HIGH'])
            LOW2    = float(Stock_df.iloc[1]['LOW'])
            CLOSE2  = float(Stock_df.iloc[1]['CLOSE'])

            MID2 = ( OPEN2 + HIGH2 + LOW2 + CLOSE2 )/ 4

            OPEN3   = float(Stock_df.iloc[2]['OPEN'])
            HIGH3   = float(Stock_df.iloc[2]['HIGH'])
            LOW3   = float(Stock_df.iloc[2]['LOW'])
            CLOSE3  = float(Stock_df.iloc[2]['CLOSE'])

            MID3 = ( OPEN3 + HIGH3 + LOW3 + CLOSE3 )/ 4

            if self.candleGreenRed(Stock_df.iloc[0]) == 'RED' and self.IsCandleBigBody(Stock_df.iloc[0]) == True and \
               OPEN2 <= CLOSE1 and (HIGH2 - LOW2) < (HIGH1 - LOW1) and \
               self.candleGreenRed(Stock_df.iloc[2]) == 'GREEN' and CLOSE3 > MID1:
                print('bullishThreeEveningStar_IB1')
                chk = True

            if self.IsCandleBigBody(Stock_df.iloc[0]) == True and \
               HIGH2 < HIGH1 and LOW2 > LOW1 and \
               self.IsCandlePinbar(Stock_df.iloc[2],'UP','GREEN') and LOW3 < LOW1 and CLOSE3 > LOW1:
                print('bullishThreeEveningStar_IB2')
                chk = True

            if HIGH2 < HIGH1 and LOW2 > LOW1 and \
               self.candleGreenRed(Stock_df.iloc[2]) == 'GREEN'  and CLOSE3 > HIGH2:
                print('bullishThreeEveningStar_IB3')
                chk = True
                
        except Exception as e:
            print(e)
            chk = False
        return chk


##_------------------------------------------------------------------------- or (self.IsCandleMediumBody(Stock_df) == True) 
##    def singleBearCandle(self, Stock_df):
##        chk = False 
##        try:
##            if ((self.candleGreenRed(Stock_df) == "RED" and ((self.IsCandleBigBody(Stock_df) == True) or (self.IsCandleMediumBody(Stock_df) == True) )) or (self.IsCandlePinbar(Stock_df,"DOWN","RED") == True) or (self.IsCandleDoji(Stock_df,"RED") == True)):
##                chk = True                
##        except Exception as e:
##            print("Error in singleBearCandle ", e)
##            chk = False
##        return chk
##
##    def singleBullCandle(self, Stock_df):
##        chk = False 
##        try:
##            if ((self.candleGreenRed(Stock_df) == "GREEN" and ((self.IsCandleBigBody(Stock_df) == True) or (self.IsCandleMediumBody(Stock_df) == True) )) or (self.IsCandlePinbar(Stock_df,"UP","GREEN") == True) or (self.IsCandleDoji(Stock_df,"GREEN") == True)):
##                chk = True                
##        except Exception as e:
##            print("Error in singleBullCandle ", e)
##            chk = False
##        return chk     

    def singleBearCandle(self, Stock_df):
        chk = False 
        try:
            if ((self.candleGreenRed(Stock_df) == "RED" and ((self.IsCandleBigBody(Stock_df) == True) or (self.IsCandleMediumBody(Stock_df) == True) )) or (self.IsCandlePinbar(Stock_df,"DOWN","RED") == True)):
                chk = True                
        except Exception as e:
            print("Error in singleBearCandle ", e)
            chk = False
        return chk

    def singleBullCandle(self, Stock_df):
        chk = False 
        try:
            if ((self.candleGreenRed(Stock_df) == "GREEN" and ((self.IsCandleBigBody(Stock_df) == True) or (self.IsCandleMediumBody(Stock_df) == True) )) or (self.IsCandlePinbar(Stock_df,"UP","GREEN") == True)):
                chk = True                
        except Exception as e:
            print("Error in singleBullCandle ", e)
            chk = False
        return chk
    
##
##    def singleBearCandle(self, Stock_df):
##        chk = False 
##        try:
##            if self.candleGreenRed(Stock_df) == "RED":
##                chk = True                
##        except Exception as e:
##            print("Error in singleBearCandle ", e)
##            chk = False
##        return chk
##
##    def singleBullCandle(self, Stock_df):
##        chk = False 
##        try:
##            if self.candleGreenRed(Stock_df) == "GREEN":
##                chk = True                
##        except Exception as e:
##            print("Error in singleBullCandle ", e)
##            chk = False
##        return chk

    
##import pandas as pd
##df_ = pd.DataFrame()
##df_['OPEN']     = [277.05, 277.45, 12084.75]
##df_['HIGH']     = [279.3, 278.85, 12142.25]
##df_['LOW']      = [276.95, 276.55, 12005.00]
##df_['CLOSE']    = [278.1, 278.55, 12134.20]
####
####print(df_.iloc[2])
####277.05	279.3	276.95	278.1
##ptn = patterns()
####print(df_.iloc[2]['OPEN']) 7.5 
##print(ptn.IsCandlePinbar(df_.iloc[1],'UP','GREEN'))
##print(ptn.IsCandleMediumBody(df_.iloc[1]))
##print(ptn.IsCandleBigBody(df_.iloc[1]))
