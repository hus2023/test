from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import pandas as pd
from datetime import datetime

# Execution Starting time
Start_Time = datetime.now()

file_input = 'C:\\uniMelb\\DSproject_winterTerm\\TaskCrawling\\2021_7_30\\tasklist_combine_add_status.csv'

file_output_open = 'C:\\uniMelb\\DSproject_winterTerm\\TaskCrawling\\OpenStatus\\tasklist_0730_openStatus_0730.csv'
file_output_close = 'C:\\uniMelb\\DSproject_winterTerm\\TaskCrawling\\CloseStatus\\tasklist_0730_closeStatus_0730.csv'

# load task.csv list i have crawled if i have task_list.csv file
task_list = pd.read_csv(file_input)
task_page = list(task_list['task_page'])
task_status = list(task_list['task_status'])

base_url = 'https://www.airtasker.com/'

def getWorker(task_link):
    workers_pertask = []
    taskPage = requests.get(task_link)
    WSoup = BeautifulSoup(taskPage.text, 'html.parser')
    new_workers = WSoup.select('a[data-ui-test="user-info-name-link"]')
    for new_worker in new_workers:
        new_item = new_worker['href']
        new_url = urljoin(base_url, new_item)
        workers_pertask.append(new_url)
    return workers_pertask

def getStatus(task_page):
    status = "none"
    taskPage = requests.get(task_page)
    WSoup = BeautifulSoup(taskPage.text, 'html.parser')
    bar_section = WSoup.find('div', {'class': 'task_details_step_bar__Container-sc-1d7g3xl-0 kqzgXu'})
    if len(bar_section) == 2:
        statusText = bar_section.findChildren()[3].text
        status = statusText.lower()
    else:
        bar_1 = bar_section.findChildren()[0]
        bar_2 = bar_section.findChildren()[2]
        bar_3 = bar_section.findChildren()[4]
        ui_1 = bar_1['data-ui-test']
        ui_2 = bar_2['data-ui-test']
        ui_3 = bar_3['data-ui-test']
        if ui_1 == 'completed-task-state':
            statusText = bar_section.findChildren()[1].text
            status = statusText.lower()
        elif ui_2 == 'completed-task-state':
            statusText = bar_section.findChildren()[3].text
            status = statusText.lower()
        elif ui_3 == 'completed-task-state':
            statusText = bar_section.findChildren()[5].text
            status = statusText.lower()
        else:
            statusText = 'error happened'
            status = statusText.lower()
            print("error in " + task_page)
    return status

openTask = []
closeTask = []
closeTask_status = []
for i in range(0,len(task_page)):
    if task_status[i] == 'open':
        new_open = task_page[i]
        openTask.append(new_open)
    else:
        new_close = task_page[i]
        new_status = task_status[i]
        closeTask.append(new_close)
        closeTask_status.append(new_status)

new_openTask = []
cur_status = []
workerList = []
for link in openTask:
    current_status = getStatus(link)
    if current_status == 'open':
        new_openTask.append(link)
        cur_status.append(current_status)
        wList = getWorker(link)
        workerList.append(str(wList))
    else:
        closeTask.append(link)
        closeTask_status.append(current_status)

# update open task csv, it should be followed.
task_openFollow = pd.DataFrame({'task_page': new_openTask, 'task_status': cur_status, 'workerList': workerList})
task_openFollow.to_csv(file_output_open, index=False, sep=',')

cWorkerList = []
for link in closeTask:
    wList_c = getWorker(link)
    cWorkerList.append(str(wList_c))

# update close task csv
task_closeFollow = pd.DataFrame({'task_page': closeTask, 'task_status': closeTask_status, 'workerList': cWorkerList})
task_closeFollow.to_csv(file_output_close, index=False, sep=',')

# Execution Ending time
End_Time = datetime.now()

# total time Measure
Total_Time = End_Time - Start_Time
print("Total execution time was " + str(Total_Time))