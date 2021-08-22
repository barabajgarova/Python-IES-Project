import requests
import json
import pandas as pd
import numpy as np
from collections import defaultdict
from bs4 import BeautifulSoup

def get_individual():
    r = requests.get('https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/osoby.json')
    a = r.json()
    df = pd.DataFrame(a['data']).set_index('datum')
    return df

def get_individual_deaths():
    r = requests.get('https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/umrti.json')
    a = r.json()
    df = pd.DataFrame(a['data']).set_index('datum')
    return df

def get_individual_hospitalizations():
    r = requests.get('https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/hospitalizace.json')
    a = r.json()
    df = pd.DataFrame(a['data']).set_index('datum')
    return df

def get_stringency(start_date='2020-03-10',end_date='2021-08-18'):
    r = requests.get(f'https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/{start_date}/{end_date}')
    dt = r.json()
    data = {}
    for i in dt['data']:
        for j in dt['data'][i]:
            if dt['data'][i][j]['country_code'] == 'CZE':
                date = dt['data'][i][j]['date_value']
                data[date] = dt['data'][i][j]
                continue
    df = pd.DataFrame(data).T[['confirmed', 'deaths',
       'stringency_actual', 'stringency', 'stringency_legacy',
       'stringency_legacy_disp']]
    return df 

def get_general_daily_stats():
    r = requests.get('https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/nakazeni-vyleceni-umrti-testy.json')
    a = r.json()
    df = pd.DataFrame(a['data']).set_index('datum')
    return df