# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 16:17:08 2022

@author: DS
"""

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

def todayweather(result):
    weather_url = 'https://www.weather.go.kr/w/obs-climate/land/city-obs.do'
    html = urllib.request.urlopen(weather_url)
    soupWeather = BeautifulSoup(html, 'html.parser')
    tag_tbody = soupWeather.find('tbody')
    for row in tag_tbody.find_all('tr'):
        row_td = row.find_all('td')
        row_a = row.find('a')
        #print(row_a.get_text())
        row_sidogu = row_a.get_text()
        row_temp = row_td[5].string
        #print(row_temp)
        row_humidity = row_td[10].string
        #print(row_humidity)
        result.append([row_sidogu]+[row_temp]+[row_humidity])
        #print(result)
    return

def main():
    result= []
    print('weather crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    todayweather(result)
    today_tb = pd.DataFrame(result, columns=('sido-gu','온도','습도'))
    #today_tb.to_csv('E:/빅데이터 수업자료/week06/weather.csv', encoding='cp949', mode='w', index=True)
    print(today_tb)
if __name__ == '__main__':
    main()
     