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

file_input = 'C:\\uniMelb\\DSproject_winterTerm\\hiPage\\hiPageLocation.csv'
file_output = 'C:\\uniMelb\\DSproject_winterTerm\\hiPage\\hiPageworkers.csv'
location_list = pd.read_csv(file_input)
location_page_ini = list(location_list['location_page'])

worker_page = []

##############################################

# test_page = location_page_ini[0]

driver = webdriver.Chrome(executable_path="C:\\uniMelb\DSproject\chromedriver_win32\chromedriver.exe")
# driver.get(test_page)
# driver.maximize_window()
# time.sleep(1)

#<a class="Suburb__ViewMoreLink-sc-1snaqf0-1 jWcZWo">View More Electricians</a>
#//a[@class="Suburb__ViewMoreLink-sc-1snaqf0-1 jWcZWo"]

def viewMoreClick():
    ViewMore = driver.find_element_by_xpath('//a[@class="Suburb__ViewMoreLink-sc-1snaqf0-1 jWcZWo"]')
    driver.execute_script("arguments[0].scrollIntoView();", ViewMore)
    js='window.scrollBy(0,-50)'
    driver.execute_script(js)
    time.sleep(0.5)
    ViewMore.click()

# for i in range(50):
#     try:
#         viewMoreClick()
#         time.sleep(0.5)
#     except:
#         break
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# base_url = 'https://hipages.com.au'
# workers_section = soup.findAll('a',href=re.compile("^/connect/"))
# for worker in workers_section:
#     new_url = worker['href']
#     w_page = urljoin(base_url, new_url)
#     if w_page not in worker_page:
#         worker_page.append(w_page)
#     else:
#         pass
# print(worker_page)
# print(len(worker_page))
# driver.close()

def getworkerFromOneLocation(location_url):
    driver.get(location_url)
    driver.maximize_window()
    time.sleep(1)
    for i in range(50):
        try:
            viewMoreClick()
            time.sleep(0.5)
        except:
            break
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    base_url = 'https://hipages.com.au'
    workers_section = soup.findAll('a',href=re.compile("^/connect/"))
    for worker in workers_section:
        new_url = worker['href']
        w_page = urljoin(base_url, new_url)
        if w_page not in worker_page:
            worker_page.append(w_page)
        else:
            pass

for area_url in location_page_ini:
    getworkerFromOneLocation(area_url)
    print(area_url + "has been crawled.")
    time.sleep(2)

worker_get = pd.DataFrame({'worker_page': worker_page})
worker_get.to_csv(file_output, index=False, sep=',')

driver.close()

# Execution Ending time
End_Time = datetime.now()

# total time Measure
Total_Time = End_Time - Start_Time
print("Total execution time was " + str(Total_Time))