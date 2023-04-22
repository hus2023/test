from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import pandas as pd
from datetime import datetime
from selenium import webdriver
import time

# Execution Starting time
Start_Time = datetime.now()

task_name = []

file_output = 'C:\\uniMelb\\DSproject_winterTerm\\taskname\\allTaskName.csv'

############### task name url bar ################
# https://www.airtasker.com/electricians/
# https://www.airtasker.com/electricians/adsl-technician/
# https://www.airtasker.com/electricians/air-source-heat-pump-installation-repairs/
# https://www.airtasker.com/electricians/aircon-cleaning/
# https://www.airtasker.com/electricians/aircon-installation/
# https://www.airtasker.com/electricians/aircon-repair/
# https://www.airtasker.com/electricians/bar-fridge-repairs/
###################################################
name_page = []
base_url = 'https://www.airtasker.com/'
category_url = 'https://www.airtasker.com/categories/'
cPage = requests.get(category_url)
cSoup = BeautifulSoup(cPage.text, 'html.parser')
electricianPart = cSoup.find('h2', text='Electricians')
allPart = electricianPart.parent.parent.parent
for i in range(7,53):
    if i%2==1:
        nameParts = allPart.findChildren()[i]['href']
        new_url = urljoin(base_url, nameParts)
        name_page.append(new_url)
    else:
        pass
# nameParts = allPart.findChildren()[7]['href']
# new_url = urljoin(base_url, nameParts)
# print(new_url)
# print(name_page)
####################################################

for page in name_page:
    surfPage = requests.get(page)
    Soup = BeautifulSoup(surfPage.text, 'html.parser')
    new_tasknames = Soup.select('h3[class="Text__StyledTypographyComponent-sc-35e02v-0 dDdAxQ"]')
    for name in new_tasknames:
        new_name = name.text
        task_name.append(new_name)
# taskName_url = 'https://www.airtasker.com/electricians/adsl-technician/'
# surfPage = requests.get(taskName_url)
# Soup = BeautifulSoup(surfPage.text, 'html.parser')
# new_tasknames = Soup.select('h3[class="Text__StyledTypographyComponent-sc-35e02v-0 dDdAxQ"]')
# for name in new_tasknames:
#     new_name = name.text
#     task_name.append(new_name)

task_name_list = pd.DataFrame({'task_name': task_name})
task_name_list.to_csv(file_output, index=False, sep=',')

##########################################################################

# Execution Ending time
End_Time = datetime.now()

# total time Measure
Total_Time = End_Time - Start_Time
print("Total execution time was " + str(Total_Time))