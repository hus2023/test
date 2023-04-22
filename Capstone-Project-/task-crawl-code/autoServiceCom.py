from datetime import datetime
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import requests
import re

# Execution Starting time
Start_Time = datetime.now()

file_input = 'C:\\uniMelb\\DSproject_winterTerm\\service.com.au\\serviceLocationList.csv'
file_output = 'C:\\uniMelb\\DSproject_winterTerm\\service.com.au\\serviceComWorkersList_801_866.csv'
location_list = pd.read_csv(file_input)
location_page_ini = list(location_list['location_page'])

min_id = 801
max_id = 866
location_page = []
for n in range(min_id,max_id):
    location_page.append(location_page_ini[n])

worker_page = []

base_url = 'https://www.service.com.au'

# driver = webdriver.Chrome(executable_path="C:\\uniMelb\DSproject\chromedriver_win32\chromedriver.exe")

########## test section #######################

# test_location = location_page[0] # https://www.service.com.au/find/electrician/abbotsford-933-vic

# Apage = requests.get(test_location)
# ASoup = BeautifulSoup(Apage.text, 'html.parser')

# get worker url from one page
# w_section = ASoup.findAll('a',href=re.compile("^/listing/electrician-"))
# for wName in w_section:
#     w_url = wName['href']
#     w_url_new = w_url.rstrip('#reviews-section')
#     w_page = urljoin(base_url, w_url_new)
#     if w_page not in worker_page:
#         worker_page.append(w_page)
#     else:
#         pass
# print(worker_page)
# print(len(worker_page))

# for i in range(1,151):
#     page_url = str(test_location) + '?page=' + str(i)
#     print(page_url)

###############################################

def getFromOnePage(page_url):
    Apage = requests.get(page_url)
    ASoup = BeautifulSoup(Apage.text, 'html.parser')
    w_section = ASoup.findAll('a', href=re.compile("^/listing/electrician-"))
    for wName in w_section:
        w_url = wName['href']
        w_url_new = w_url.rstrip('#reviews-section')
        w_page = urljoin(base_url, w_url_new)
        if w_page not in worker_page:
            worker_page.append(w_page)
        else:
            pass

def getFromOneLocation(location_url):
    for i in range(1,101):
        pageN = str(location_url) + '?page=' + str(i)
        try:
            getFromOnePage(pageN)
        except requests.exceptions.ConnectionError as e:
            print(e)
            print('exceed limit :( sleep more than 10 mins to restart')
            time.sleep(10 * 60)
            print('sleep ended :)')
            continue

for area in location_page:
    getFromOneLocation(area)



###############################################


worker_get = pd.DataFrame({'worker_page': worker_page})
worker_get.to_csv(file_output, index=False, sep=',')

# Execution Ending time
End_Time = datetime.now()

# total time Measure
Total_Time = End_Time - Start_Time
print("Total execution time was " + str(Total_Time))