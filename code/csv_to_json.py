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
