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
        return render_template('GETpage.html')
    else:
        #request was a post
        #month = request.form.get('month')
        print "okokookokokok"
        return render_template('POSTpage.html')
if __name__ == '__main__':
    #app.run(port=33507)
    #####
    app.run()
