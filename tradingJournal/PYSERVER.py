from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api, reqparse
from json import dumps
from flask_jsonpify import jsonify
import Trade_logs
import json
import os
from flask import flash, redirect, url_for
import pandas as pd
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'D:/Project/Angular/plant ops/src/assets/Trades_snap'
##UPLOAD_FOLDER_SWING = 'D:/Project/Angular/python/FileUploads/Swing'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
##app.config['UPLOAD_FOLDER_SWING'] = UPLOAD_FOLDER_SWING
api = Api(app)

CORS(app)

@app.route("/")
class AllTrades_positional(Resource):
    def get(self):
        return jsonify(Trade_logs.getAllTrades())

class AllPaperTradesPositional(Resource):
    def get(self):
        return jsonify(Trade_logs.getAllTradesPaper())

class Log_trade_with_file_positional(Resource):
    def post(self):
        log_df = pd.DataFrame()
        log_df['efilename'] = ['NONE']
        log_df['exfilename'] = ['NONE']
        
        if 'entryfile' not in request.files:
            print('No file part for entry')
        else:
            file = request.files['entryfile']        
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                log_df['efilename'] = [file.filename]

        if 'exitfile' not in request.files:
            print('No file part for exit')
        else:
            fileex = request.files['exitfile']        
            if fileex and allowed_file(fileex.filename):
                filename = secure_filename(fileex.filename)
                fileex.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                log_df['exfilename'] = [fileex.filename]            
        

        log_df['trade_num'] = [int(request.form['trade_num'])]
        log_df['tradedate'] = [request.form['tradedate']]
        log_df['scriptname'] = [request.form['scriptname']]
        log_df['nifty'] = [request.form['nifty']]
        log_df['sector'] = [request.form['sector']]
        log_df['quantity'] = [request.form['quantity']]
        log_df['entryprice'] = [request.form['entryprice']]
        log_df['slprice'] = [request.form['slprice']]
        log_df['entryreason'] = [request.form['entryreason']]
        log_df['entrytime'] = [request.form['entrytime']]
        log_df['exitprice'] = [request.form['exitprice']]
        log_df['exittime'] = [request.form['exittime']]
        log_df['exitreason'] = [request.form['exitreason']]
        log_df['tradetype'] = [request.form['tradetype']]
        log_df['riskreward'] = [request.form['riskreward']]
        log_df['profitloss'] = [request.form['profitloss']]
        log_df['capital'] = [request.form['capital']]        
        log_df['mistakeslearning'] = [request.form['mistakeslearning']]

        if (request.form['papertrade']).upper() == 'TRUE':
            log_df['papertrade'] = [True]

        elif (request.form['papertrade']).upper() == 'FALSE':
            log_df['papertrade'] = [False]
            
        log_df.set_index('trade_num', inplace  = True)
        status = Trade_logs.submitTradeWithFile(log_df)  
        if status == 'SUCCESS':
            return 'SUCCESS',201
        else:
            return 500
##--------------------------------------------------------------------------##
class AllTrades_swing(Resource):
    def get(self):
        return jsonify(Trade_logs.getAllTrades_swing())

class AllPaperTradesSwing(Resource):
    def get(self):
        return jsonify(Trade_logs.getAllTradesPaper_swing())

class Log_trade_with_file_swing(Resource):
    def post(self):
        log_df = pd.DataFrame()
        log_df['efilename'] = ['NONE']
        log_df['exfilename'] = ['NONE']
        
        if 'entryfile' not in request.files:
            print('No file part for entry')
        else:
            file = request.files['entryfile']        
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
##                print(UPLOAD_FOLDER_SWING)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                log_df['efilename'] = [file.filename]

        if 'exitfile' not in request.files:
            print('No file part for exit')
        else:
            fileex = request.files['exitfile']        
            if fileex and allowed_file(fileex.filename):
                filename = secure_filename(fileex.filename)
                fileex.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                log_df['exfilename'] = [fileex.filename]            
        

        log_df['trade_num'] = [int(request.form['trade_num'])]
        log_df['tradedate'] = [request.form['tradedate']]
        log_df['scriptname'] = [request.form['scriptname']]
        log_df['nifty'] = [request.form['nifty']]
        log_df['sector'] = [request.form['sector']]
        log_df['quantity'] = [request.form['quantity']]
        log_df['entryprice'] = [request.form['entryprice']]
        log_df['slprice'] = [request.form['slprice']]
        log_df['entryreason'] = [request.form['entryreason']]
        log_df['entrytime'] = [request.form['entrytime']]
        log_df['exitprice'] = [request.form['exitprice']]
        log_df['exittime'] = [request.form['exittime']]
        log_df['exitreason'] = [request.form['exitreason']]
        log_df['tradetype'] = [request.form['tradetype']]
        log_df['riskreward'] = [request.form['riskreward']]
        log_df['profitloss'] = [request.form['profitloss']]
        log_df['capital'] = [request.form['capital']]        
        log_df['mistakeslearning'] = [request.form['mistakeslearning']]

        if (request.form['papertrade']).upper() == 'TRUE':
            log_df['papertrade'] = [True]

        elif (request.form['papertrade']).upper() == 'FALSE':
            log_df['papertrade'] = [False]
            
        log_df.set_index('trade_num', inplace  = True)
        status = Trade_logs.submitTradeWithFile_swing(log_df)  
        if status == 'SUCCESS':
            return 'SUCCESS',201
        else:
            return 500

##------------------------------------------------------------------------------------------------------
        
class AllTrades(Resource):
    def get(self):
        return jsonify(Trade_logs.getAllTrades())

class AllPaperTrades(Resource):
    def get(self):
        return jsonify(Trade_logs.getAllTradesPaper())

class Get_trade(Resource):
    def get(self, tradeid):
        print('Trade id:' + tradeid)
        result = Trade_logs.getTrade(tradeid)
        return jsonify(result)

class SAVE_LOGS(Resource):
    def post(self):
        json_data = request.get_json(force=True)
##        print(json_data)
##        json_1 = json.loads(df.to_json(orient='records'))        
        status = Trade_logs.submitTrade(json_data)  
        if status == 'SUCCESS':
            return 'SUCCESS',201
        else:
            return 500
class TRADES_DATA_IN_RANGE(Resource):
    def get(self):
        startdate  = request.args.get('startdate')
        enddate  = request.args.get('enddate')
##        print('startdate='+ startdate+ ' enddate='+enddate) ##'2018-12-01','2018-12-28'
        return jsonify(Trade_logs.TRADES_DATA_IN_RANGE(startdate,enddate))

class PAPER_TRADES_CHART_DATA(Resource):
    def get(self):
        startdate  = request.args.get('startdate')
        enddate  = request.args.get('enddate')
##        print('startdate='+ startdate+ ' enddate='+enddate) ##'2018-12-01','2018-12-28'
        return jsonify(Trade_logs.PAPER_TRADES_CHART_DATA(startdate,enddate))    
    
class Log_trade_with_file(Resource):
    def post(self):
        log_df = pd.DataFrame()
        log_df['efilename'] = ['NONE']
        log_df['exfilename'] = ['NONE']
        
        if 'entryfile' not in request.files:
            print('No file part for entry')
        else:
            file = request.files['entryfile']        
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                log_df['efilename'] = [file.filename]

        if 'exitfile' not in request.files:
            print('No file part for exit')
        else:
            fileex = request.files['exitfile']        
            if fileex and allowed_file(fileex.filename):
                filename = secure_filename(fileex.filename)
                fileex.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                log_df['exfilename'] = [fileex.filename]            
        

        log_df['trade_num'] = [int(request.form['trade_num'])]
        log_df['tradedate'] = [request.form['tradedate']]
        log_df['scriptname'] = [request.form['scriptname']]
        log_df['nifty'] = [request.form['nifty']]
        log_df['sector'] = [request.form['sector']]
        log_df['quantity'] = [request.form['quantity']]
        log_df['entryprice'] = [request.form['entryprice']]
        log_df['slprice'] = [request.form['slprice']]
        log_df['entryreason'] = [request.form['entryreason']]
        log_df['entrytime'] = [request.form['entrytime']]
        log_df['exitprice'] = [request.form['exitprice']]
        log_df['exittime'] = [request.form['exittime']]
        log_df['exitreason'] = [request.form['exitreason']]
        log_df['tradetype'] = [request.form['tradetype']]
        log_df['riskreward'] = [request.form['riskreward']]
        log_df['profitloss'] = [request.form['profitloss']]
        log_df['capital'] = [request.form['capital']]        
        log_df['mistakeslearning'] = [request.form['mistakeslearning']]

        if (request.form['papertrade']).upper() == 'TRUE':
            log_df['papertrade'] = [True]

        elif (request.form['papertrade']).upper() == 'FALSE':
            log_df['papertrade'] = [False]
            
        log_df.set_index('trade_num', inplace  = True)
        status = Trade_logs.submitTradeWithFile(log_df)  
        if status == 'SUCCESS':
            return 'SUCCESS',201
        else:
            return 500
        

        
        


api.add_resource(AllPaperTrades, '/tradespaper')
api.add_resource(AllTrades, '/trades')
api.add_resource(Log_trade_with_file,'/savefile')
##----------------------------------------------------
api.add_resource(AllPaperTradesPositional, '/tradespaperpositional')
api.add_resource(AllTrades_positional, '/trades_positional')
api.add_resource(Log_trade_with_file_positional,'/savefile_positional')
##----------------------------------------------------
api.add_resource(AllPaperTradesSwing, '/tradespaperswing')
api.add_resource(AllTrades_swing, '/trades_swing')
api.add_resource(Log_trade_with_file_swing,'/savefile_swing')
##----------------------------------------------------

api.add_resource(TRADES_DATA_IN_RANGE,'/getTradesData')
api.add_resource(PAPER_TRADES_CHART_DATA,'/getChartingData')
api.add_resource(SAVE_LOGS,'/save')

if __name__ == '__main__':
   app.run(port=5002)
    
