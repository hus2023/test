from datetime import datetime
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd


# Execution Starting time
Start_Time = datetime.now()

########## test elements ###############################
# locationCity = 'Bulleen,VIC'
location_url = 'https://www.serviceseeking.com.au/electricians/vic/altona-meadows'
########################################################

worker_page = []

file_output = 'C:\\uniMelb\\DSproject_winterTerm\\serviceseeking\\autoCrawl\\0827test.csv'
########################################################

driver = webdriver.Chrome(executable_path="C:\\uniMelb\DSproject\chromedriver_win32\chromedriver.exe")
# driver.get('https://www.serviceseeking.com.au/electricians')
driver.get(location_url)

driver.maximize_window()
time.sleep(1)

# SearchBar = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[2]/div/form/div[1]/div/input[1]')
# SearchBar.click()
# SearchBar.send_keys('Electricians')
# time.sleep(1)
# SearchSelect = Select(SearchBar)
# SearchSelect.select_by_index(0)
# time.sleep(1)
#
# Location = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[2]/div/form/div[2]/div/span/input[2]')
# Location.click()
# Location.send_keys(locationCity)
# time.sleep(1)

#<button class="btn btn-clear btn-block btn-lg view-more">View More</button>
# xpath: //button[@class="btn btn-clear btn-block btn-lg view-more"]
# stop until
#<button class="btn btn-clear btn-block btn-lg view-more" style="opacity: 0; display: none;">View More</button>
# xpath: //button[@style="opacity: 0; display: none;"]

for i in range(20):
    try:
        stopWord = driver.find_element_by_xpath('//button[@style="opacity: 0; display: none;"]')
        break
    except:
        ViewMore = driver.find_element_by_xpath('//button[@class="btn btn-clear btn-block btn-lg view-more"]')
        ViewMore.click()
        time.sleep(5)

# for i in range(20):
#     try:
#         ViewMore = driver.find_element_by_xpath('//button[@class="btn btn-clear btn-block btn-lg view-more"]')
#         ViewMore.click()
#         time.sleep(5)
#     except:
#         break

print("view more over! Start Crawl!")
###################################################################################
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

worker_get = pd.DataFrame({'worker_page': worker_page})
worker_get.to_csv(file_output, index=False, sep=',')
###################################################################################

# Execution Ending time
End_Time = datetime.now()

# total time Measure
Total_Time = End_Time - Start_Time
print("Total execution time was " + str(Total_Time))