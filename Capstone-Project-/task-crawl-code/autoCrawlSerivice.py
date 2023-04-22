from datetime import datetime
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

# Execution Starting time
Start_Time = datetime.now()

file_input = 'C:\\uniMelb\\DSproject_winterTerm\\serviceseeking\\autoCrawl\\Location_Url_List.csv'
location_list = pd.read_csv(file_input)
location_page = list(location_list['location_page'])

worker_page = []

file_output = 'C:\\uniMelb\\DSproject_winterTerm\\serviceseeking\\autoCrawl\\Autotest.csv'

def getWorkerOneArea(location_url):
    driver = webdriver.Chrome(executable_path="C:\\uniMelb\DSproject\chromedriver_win32\chromedriver.exe")
    driver.get(location_url)
    driver.maximize_window()
    time.sleep(1)
    for i in range(20):
        try:
            stopWord = driver.find_element_by_xpath('//button[@style="opacity: 0; display: none;"]')
            break
        except:
            ViewMore = driver.find_element_by_xpath('//button[@class="btn btn-clear btn-block btn-lg view-more"]')
            ViewMore.click()
            time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    base_url = 'https://www.serviceseeking.com.au'
    card_section = soup.select('div[class="card-content card-pad-md hidden-xs"]')
    for section in card_section:
        new_item = section.findChildren('a')[0]['href']
        new_page = urljoin(base_url, new_item)
        new_url = new_page.rstrip('\'business_directory')
        # print(new_page)
        if new_url not in worker_page:
            worker_page.append(new_url)
    time.sleep(1)
    driver.close()
    time.sleep(1)


for area_url in location_page:
    getWorkerOneArea(area_url)
    print(area_url + "has been crawled.")


worker_get = pd.DataFrame({'worker_page': worker_page})
worker_get.to_csv(file_output, index=False, sep=',')

# Execution Ending time
End_Time = datetime.now()

# total time Measure
Total_Time = End_Time - Start_Time
print("Total execution time was " + str(Total_Time))