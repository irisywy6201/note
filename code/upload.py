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


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
keyword = 'TSMC'
download_path = 'data/' + keyword
chrome_options = Options()
download_prefs = {'download.default_directory' : download_path,
                    'download.prompt_for_download' : False,
                    'profile.default_content_settings.popups' : 0}

chrome_options.add_experimental_option('prefs', download_prefs)
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920x1080')
url = 'https://trends.google.com/trends/' 
# Start up browser
browser = webdriver.Chrome(options=chrome_options)
# browser.get(url) 


# browser.command_executor._commands["send_command"] = \
#         ("POST", '/session/$sessionId/chromium/send_command')
 
# params = {'cmd': 'Page.setDownloadBehavior',
#             'params': {'behavior': 'allow', 'downloadPath': download_path}}
# browser.execute("send_command", params)
# # Load webpage
browser.get(url)
time.sleep(5)
elem = browser.find_element(By.ID, 'i9')
elem.clear()
elem.send_keys("TSMC,APPLE")
elem.send_keys(Keys.RETURN)

time.sleep(5)
elem = browser.find_element(By.CLASS_NAME, 'widget-actions-item.export')
elem.click()
elem.send_keys(Keys.ENTER)
time.sleep(10)
browser.quit()
