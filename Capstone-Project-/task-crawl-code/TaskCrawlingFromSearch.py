from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import pandas as pd
from datetime import datetime
from selenium import webdriver
import time

# Execution Starting time
Start_Time = datetime.now()

# load task.csv list i have crawled if i have task_list.csv file
# the csv file should be stored in the same area with the this py file
# task_list = pd.read_csv("task_list.csv")
# task_page = list(task_list['task_page'])
#print(task_page)

# load task_new.csv
# task_list = pd.read_csv("./new/task_list_all_0516_electric.csv")
# task_page = list(task_list['task_page'])

task_page = []

file_output = 'C:\\uniMelb\\DSproject_winterTerm\\TaskCrawling\\2021_7_30\\tasklist_0730_Geelong_electric.csv'

########search bar#######################################################
# electrician
# electricMelbourne VIC, Australia

########search bar#######################################################

# 50km Melbourne city and remotely / electrician in search bar
initial_url = 'https://www.airtasker.com/tasks/?task_states=posted%2Cassigned%2Ccompleted%2Coverdue%2Cclosed&lat=-37.8136276&lon=144.9630576&location_name=Melbourne%20VIC%2C%20Australia&radius=100000&task_types=physical&max_price=9999&min_price=5&search_term=electrician&badges='


##########################################################################

login_url = 'https://www.airtasker.com/login/'
# solve the promblem that WebCrawling crawl 30 task each time
# excuate chrome driver
driver = webdriver.Chrome(executable_path="C:\\uniMelb\DSproject\chromedriver_win32\chromedriver.exe")
# log in the website
user_name = 'xin23ling0530@gmail.com'
pass_word = 'unimelbtest'
driver.get(login_url)

time.sleep(20)
print('sleep over!')
#driver.find_element_by_name("email").send_keys(user_name)
#driver.find_element_by_name("password").send_keys(pass_word)
#driver.find_element_by_link_text("Log in")



driver.get(initial_url)
#Loader = driver.find_element_by_class_name('loaderific-not-loading')
#driver.execute_script('arguments[0].scrollIntoView(true);', Loader)
time.sleep(50)
print('remain 50s!')
time.sleep(40)
print('remain 10s!')
time.sleep(10)
print('sleep over!Start crawl!!!!!')

#page = requests.get(initial_url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

base_url = 'https://www.airtasker.com/'

# scrawl the task list in the website
task_url = []

new_tasks = soup.select('a[data-ui-test="task-list-item"]')
for new_task in new_tasks:
    new_item = new_task['href']
    new_url = urljoin(base_url, new_item)
    task_url.append(new_url)

# add new task in csv and ignore the task have been colledted in the csv file
add_tasks = [url for url in task_url if url not in task_page]
for url in add_tasks:
    task_page.append(url)

#print(task_page)
#print(len(task_page))

# update the task csv file
# task_list = pd.DataFrame({'task_page': task_page})
# task_list.to_csv("task_list.csv", index=False, sep=',')

task_list = pd.DataFrame({'task_page': task_page})
task_list.to_csv(file_output, index=False, sep=',')

# Execution Ending time
End_Time = datetime.now()

# total time Measure
Total_Time = End_Time - Start_Time
print("Total execution time was " + str(Total_Time))
