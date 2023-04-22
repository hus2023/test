from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import pandas as pd
from datetime import datetime
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Execution Starting time
Start_Time = datetime.now()

########## input area #######################

task_page = []

LocationList = ['Melbourne VIC, Australia', 'Geelong VIC, Australia', 'Bendigo VIC, Australia',
                'Horsham VIC, Australia', 'Warrnambool VIC, Australia', 'Shepparton VIC, Australia', 'Traralgon VIC, Australia']
# LocationInput = 'Melbourne VIC, Australia'

KeyWordsList = ['electrician', 'electric', 'eletronic']
# SearchKeyWord = 'electrician'

file_output = 'C:\\uniMelb\\DSproject_winterTerm\\TaskCrawling\\2021_8_30\\tasklist_combine_all.csv'

######## login page ######################
login_url = 'https://www.airtasker.com/login/'

driver = webdriver.Chrome(executable_path="C:\\uniMelb\DSproject\chromedriver_win32\chromedriver.exe")
driver.get(login_url)
driver.maximize_window()
time.sleep(5)

user_name = driver.find_element_by_xpath('//input[@id="label-1"]')
user_name.click()
user_name.send_keys('xin23ling0530@gmail.com')
time.sleep(1)

password = driver.find_element_by_xpath('//input[@id="label-2"]')
password.click()
password.send_keys('unimelbtest')
time.sleep(1)

submit = driver.find_element_by_xpath('//button[@type="submit"]')
submit.click()
time.sleep(1)

############################################
task_browse_url = 'https://www.airtasker.com/tasks/'
driver.get(task_browse_url)
time.sleep(5)

def getWorkersOneAreaOneKeyword(LocationInput, SearchKeyWord):
    # start circulation until crawling finish!!!!!!!!!
    LocationButton = driver.find_element_by_xpath('/html/body/div[1]/div/nav/nav/div/div/div[1]/div[1]/button/span')
    LocationButton.click()

    InPerson = driver.find_element_by_xpath('//button[@class="option-group__button option-group__button--selected"]')
    InPerson.click()

    # Location List
    # Melbourne VIC, Australia
    # LocationInput = 'Melbourne VIC, Australia'
    Location = driver.find_element_by_xpath('//input[@data-ui-test="location-input"]')
    Location.click()
    Location.send_keys(Keys.CONTROL, 'a')
    Location.send_keys(LocationInput)
    time.sleep(1)
    LoSelect = driver.find_element_by_xpath('//li[@role="button"]')
    LoSelect.click()
    time.sleep(2)
    #<button class="menu-flyout__apply button-sml button-cta">Apply</button>
    Apply1 = driver.find_element_by_xpath('//button[@class="menu-flyout__apply button-sml button-cta"]')
    Apply1.click()
    time.sleep(2)


    taskType = driver.find_element_by_xpath('/html/body/div[1]/div/nav/nav/div/div/div[1]/div[3]/button/span')
    taskType.click()
    time.sleep(1)
    SuggestForYou = driver.find_element_by_xpath('/html/body/div[1]/div/nav/nav/div/div/div[1]/div[3]/div/div[1]/div/div[2]/div[2]/div')
    if SuggestForYou.get_attribute("aria-checked") == "true":
        SuggestForYou.click()
    else:
        pass
    time.sleep(2)
    #<button class="menu-flyout__apply button-sml button-cta">Apply</button>
    Apply2 = driver.find_element_by_xpath('//button[@class="menu-flyout__apply button-sml button-cta"]')
    Apply2.click()
    time.sleep(2)


    # SearchKeyWord = 'electrician'
    SearchBar = driver.find_element_by_xpath('//input[@data-ui-test="search-input"]')
    SearchBar.click()
    SearchBar.send_keys(SearchKeyWord)
    #<svg class="search-input__icon" data-ui-test="search-input__icon-svg">
    SearchIcon = driver.find_element_by_xpath('/html/body/div[1]/div/nav/nav/div/div/div[2]/button')
    SearchIcon.click()
    time.sleep(2)

    ##################### Start Roll down the data ############################

    ScrollDown = driver.find_element_by_xpath('//div[@class="list vertical-scroll"]')
    ScrollDown.click()

    temp_height = 0
    x=20
    y=3000
    while True:
        js1 = "var q=document.getElementsByClassName('list vertical-scroll')[0].scrollTop={}".format(x)
        driver.execute_script(js1)
        time.sleep(2)
        x+=y
        check_height = driver.execute_script(
            "return document.getElementsByClassName('list vertical-scroll')[0].scrollTop;")
        if check_height == temp_height:
            break
        temp_height = check_height
        # print(check_height)

    ##################### start crawl data ############################

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

# circulation finish

for area in LocationList:
    for keyword in KeyWordsList:
        try:
            getWorkersOneAreaOneKeyword(area,keyword)
        except:
            pass
        # print(area, keyword)

task_list = pd.DataFrame({'task_page': task_page})
task_list.to_csv(file_output, index=False, sep=',')

driver.close()

# Execution Ending time
End_Time = datetime.now()

# total time Measure
Total_Time = End_Time - Start_Time
print("Total execution time was " + str(Total_Time))