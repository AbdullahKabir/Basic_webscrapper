#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 22:07:28 2021

@author: abdullahkabir
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def get_carsale():
    year = []
    sale = []
    url = 'https://carsalesbase.com/bangladesh-car-sales-data/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    for i in range(30):
        for table in soup.findAll('tr',{'id':'table_13_row_'+str(i)}):
            a = table.findAll('td')
            year.append(a[0].string)
            sale.append(a[1].string)
    df = pd.DataFrame({'Year': year,
           'Sale': sale})
    return df

def get_population():
    datas = []
    url = 'https://www.macrotrends.net/countries/BGD/bangladesh/population'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    for table in soup.findAll('div',{'class':'col-xs-6'}):
        for t_row in table.findAll('td'):
            data = t_row.string
            datas.append(data)
    newarr = np.array_split(datas, 72)
    df = pd.DataFrame(data=newarr, columns=['Year','population','growth',"a"])
    df = df.iloc[1:17 , :]
    return df

carsale = get_carsale()
population = get_population()

final = pd.merge(carsale, population, on="Year")

desktoppath = "A:\\Basic webscrap\\"
print(final)
final.to_csv(desktoppath+"combain_data.csv")

    


# In[ ]:




