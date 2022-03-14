# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 23:19:46 2022

@author: yawen

"""
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True



@app.route('/uploadajax', methods = ['POST'])
def upldfile():
    file_val = request.files['file']
    return('','200')
    


app.run(host='0.0.0.0', port=5000)