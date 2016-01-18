from flask import Flask,render_template,request, redirect
#import json
import numpy as np
import pandas as pd
import datetime
import dateutil.relativedelta
from bokeh.plotting import figure, output_notebook, output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html, components
import requests

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def index():  #remember the function name does not need to match the URL
    if request.method == 'GET':
        #return render_template('GETpage.html')
        return render_template('userinfo.html')
    else:
        #request was a post
        ticker = request.form.get('ticker')
        closingPrice = int(request.form.get('close') or 0)
        adjClosingPrice = int(request.form.get('adjclose') or 0)

        stockdata = pd.read_json('https://www.quandl.com/api/v3/datasets/WIKI/%s.json?auth_token=ESVPzC14bhzi2xp9Nmgb' % ticker)

        dateIndex = stockdata['dataset']['column_names'].index('Date')
        closeIndex = stockdata['dataset']['column_names'].index('Close')
        adjcloseIndex = stockdata['dataset']['column_names'].index('Adj. Close')
        
        dates = []
        closes = []
        adjcloses = []

        #request was a post
        #month = request.form.get('month')
        #print "okokookokokok"
        #return render_template('POSTpage.html')

        for i in range(30):
            dates.append(stockdata['dataset']['data'][i][dateIndex])
            closes.append(stockdata['dataset']['data'][i][closeIndex])
            adjcloses.append(stockdata['dataset']['data'][i][adjcloseIndex])

        date = datetime.datetime.strptime(dates[1], "%Y-%m-%d") 
        date = datetime.date(date.year, date.month, date.day)
        onemonth = date - dateutil.relativedelta.relativedelta(months=1)
        onemonth = datetime.date(onemonth.year, onemonth.month, onemonth.day)

        start = 1
        end = 30

        printdates = []
        for j in range(start,end):
            printdates.append(datetime.datetime.strptime(dates[j], "%Y-%m-%d"))

        printdates = list(reversed(printdates))
        printcloses = list(reversed(closes[start:end]))
        printadjcloses = list(reversed(adjcloses[start:end]))
        
        output_file("stocks.html", title="Stock Grapher")
        plot = figure(x_axis_type="datetime", title="Stock Data for %s" % ticker)

        if closingPrice == 1 & adjClosingPrice == 1:
            plot.line(printdates,printcloses,line_width=3,color = 'blue',legend="Closing price")
            plot.line(printdates,printadjcloses,line_width=3,color = 'black', legend="Adj. closing price")
        elif closingPrice == 1:
            plot.line(printdates,printcloses,line_width=3,color = 'blue', legend = "Closing price")
        elif adjClosingPrice == 1:
            plot.line(printdates,printadjcloses,line_width=3, color = 'black', legend="Adj. closing price")
        
        plot.xaxis.axis_label="Date"
        plot.yaxis.axis_label="Price ($)"
        
        script, div = components(plot)
        return render_template('graph.html', script=script, div=div)
        #show(p)
        #return ticker
        
if __name__ == '__main__':
    #app.run(port=33507)
    #####
    app.run()
