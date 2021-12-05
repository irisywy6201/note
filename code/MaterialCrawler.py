# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 18:31:22 2021

@author: yawen
"""

import requests
from bs4 import BeautifulSoup
import urllib
import pdfkit
config = pdfkit.configuration(wkhtmltopdf='C:/Users/yawen/Desktop/wkhtmltopdf/bin/wkhtmltopdf.exe')
#%%
class MaterialCrawler:
    def __init__(self):
        self.finnhub_key = 'c5s0nuqad3ia8bfb66ag'
        self.header = {'Accept': '*/*',
                       'Host': 'www.sec.gov',
                       'Accept-Encoding': 'gzip, deflate, br',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
                       'Connection':'close',
                       'X-Requested-With': 'XMLHttpRequest',
                       'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       }
    def Get8k(self, company, _from, to):
#        finnhub_client = finnhub.Client(api_key = self.finnhub_key)
#        result = finnhub_client.filings(symbol = company, form = '8-K', _from = '2020-01-01', to = '2020-06-11')
        # _from -> from: _from is not work with finnhub_client.filings()
        api_uri = 'https://finnhub.io/api/v1/stock/filings?symbol={}&form={}&from={}&to={}&token={}'.format(company, '8-k', _from, to, self.finnhub_key)
        result = requests.get(api_uri).json()
        
        return result
    
    def html2PDF(self, url, output):
        response = requests.get(url, headers = header)
        soup = BeautifulSoup(response.text, 'html.parser')
        pdfkit.from_string(str(soup), output, configuration=config)
       
        
    def GetPressRelease(self, url_8k_list):
#        url_8k_list = self.Get8kUrl(company)
        for index_8k in range(len(url_8k_list)):
            url_8k = result[index_8k]['reportUrl'].replace('ix?doc=/', '')
            response = requests.get(url_8k,headers = self.header)
            soup = BeautifulSoup(response.text, 'html.parser')
            press_release_list = soup.select('div a span')
            
            if len(press_release_list) == 0:
                print('can not find press release!')
            else:
                for index_p in range(len(press_release_list)):
                    if 'press release' in str(press_release_list[index_p]).lower():
                        print('find press release!')
                        url = press_release_list[index_p].find_parents('a')[0]['href']
                        print('url:', url)
                        split = url_8k.split('/')
                        split[-1] = url
                        press_release_url = '/'.join(split)
                        self.html2PDF(url, 'test.pdf')
                        break
        
    def Get10Q(self, company, _from, to):
        api_uri = 'https://finnhub.io/api/v1/stock/filings?symbol={}&form={}&from={}&to={}&token={}'.format(company, '10-Q', _from, to, self.finnhub_key)
        result = requests.get(api_uri).json()
        
        return result
#%%
if __name__ == '__main__':
    Crawler = MaterialCrawler()
         
            
#%%
a = soup.find_all("a", style = 'text-decoration:underline;color:#0000FF;-sec-extract:exhibit;')
div = soup.find_all('div', style = 'text-align:left;font-size:9pt;')
for i in range(len(div)):
    if '99.1' in div[i].select("span")[0]:
        print(div[i].select("span"))
        result = div[i].find_parents("td")[0].find_next_siblings("td")[1].find('a')
        
        
#%%
https://www.sec.gov/Archives/edgar/data/320193/000032019320000050/a8-kq220203282020.htm
https://www.sec.gov/Archives/edgar/data/320193/000032019320000050/a8-kexhibit991q2202032.htm
