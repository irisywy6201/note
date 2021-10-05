# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 01:31:29 2021

@author: yawen
"""
import pandas as pd
import argparse
import os
'''
parser = argparse.ArgumentParser(description='convert and converted file path')
parser.add_argument(
    '--csvPath',
    type=str,
    default='csv_file.csv',
    help='path')
parser.add_argument(
    '--jsonPath',
    default='json_file.json',
    type=str,
    help='path')
args = parser.parse_args()
'''
if __name__ == '__main__':
    
    file_name_list = os.listdir()
    
    for fname in file_name_list:
        if fname[-3:] == 'csv':
            print(fname)
            df = pd.read_csv (r'./' + fname)
            df.to_json (r'./json/' + fname[:-4] + '.json')
        

#%%
import pymongo

#%%
myclient = pymongo.MongoClient('mongodb://localhost:27017',
                                username='root',
                                password='root',
                                authMechanism='SCRAM-SHA-256')
print(myclient.list_database_names())      
#%%
import json
 
# Opening JSON file
f = open('tt.json',)
 
# returns JSON object as
# a dictionary
data = json.load(f)
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mycol.insert_many(data)   

#%%
from bson import json_util
import json
from flask import Flask, jsonify
import flask
import pymongo
app = Flask(__name__)
myclient = pymongo.MongoClient('mongodb://localhost:27017',
                                username='root',
                                password='root',
                                authMechanism='SCRAM-SHA-256')

db = myclient["mydatabase"]
@app.route("/add_one")
def add_one():
    db.todos.insert_one({'title': "todo title", 'body': "todo body"})
    return flask.jsonify(message="success")
@app.route("/")
def home():
    data = db["customers"].find()
    return str(json.loads(json_util.dumps(data)))

@app.route("/")
def home():
    data = db["tt"].find()
    output = []
    for s in data:
        output.append({'_id' : str(s['_id']), 'name': s['name'], 'email': s['email']})
    return jsonify({'result' : output})
#https://www.footmark.info/programming-language/design/restful-webapi-design-guide/
@app.route("/")
def home():
    data = list(db["tt"].find())
#    output = []
    for index,s in enumerate(data):
        data[index]['_id'] = str(s['_id'])
#        output.append({'_id' : str(s['_id']), 'name': s['name'], 'email': s['email']})
    return jsonify({'result' : data})
    #json_data = json_util.loads(json_util.dumps(list(data)))
    #return json_data
# https://github.com/jrussumbrella/dress-shop/blob/78a06cd9173ab79a14027ef8a7e79748152b1383/client/pages/index.tsx
if __name__ == "__main__":
    app.run(debug=True)  
    
#https://stackabuse.com/integrating-mongodb-with-flask-using-flask-pymongo/

#%%
textfile = open("a_file.txt", "w")
for element in data:
    json.dump(element,textfile)
    textfile.write("\n")
textfile.close()
