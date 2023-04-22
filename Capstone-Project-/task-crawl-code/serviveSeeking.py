from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urljoin
import pandas as pd
from datetime import datetime
from selenium import webdriver
import time

# Execution Starting time
Start_Time = datetime.now()

worker_page = []

file_output = 'C:\\uniMelb\\DSproject_winterTerm\\serviceseeking\\VIC3000.csv'
##########################################################

# initial_url = 'https://www.serviceseeking.com.au/electricians'
# page = requests.get(initial_url)
# soup = BeautifulSoup(page.text, 'html.parser')
# base_url = 'https://www.serviceseeking.com.au'
#
# card_section = soup.select('div[class="card-content card-pad-md hidden-xs"]')
# for section in card_section:
#     new_item = section.findChildren('a')[0]['href']
#     new_page = urljoin(base_url, new_item)
#     print(new_page)

##########################################################

# req_url = 'https://www.serviceseeking.com.au/local-electricians/vic/melbourne?page=17&format=js&sort_filter=false&_=1628318292539'
# req_page = requests.get(req_url)
# Ctext = req_page.text
#
# base_url = 'https://www.serviceseeking.com.au'
# pattern = re.compile(r'href=\\\"/profile/[0-9]+\?source=')
# results = pattern.findall(Ctext)
# for result in results:
#     new_item = result.lstrip("href=\"\\")
#     new_page = urljoin(base_url,new_item)
#     print(new_page)

################function#################################
base_url = 'https://www.serviceseeking.com.au'

for i in range(1,18):
    req_url = 'https://www.serviceseeking.com.au/local-electricians/vic/melbourne?page='+str(i)+'&format=js&sort_filter=false&_=1628318292539'
    req_page = requests.get(req_url)
    Ctext = req_page.text
    pattern = re.compile(r'href=\\\"/profile/[0-9]+\?source=')
    results = pattern.findall(Ctext)
    for result in results:
        new_item = result.lstrip("href=\"\\")
        new_page = urljoin(base_url,new_item)
        if new_page not in worker_page:
            worker_page.append(new_page)
        else:
            pass

##########################################################

worker_list_out = pd.DataFrame({'worker_page': worker_page})
worker_list_out.to_csv(file_output, index=False, sep=',')

# Execution Ending time
End_Time = datetime.now()

# total time Measure
Total_Time = End_Time - Start_Time
print("Total execution time was " + str(Total_Time))