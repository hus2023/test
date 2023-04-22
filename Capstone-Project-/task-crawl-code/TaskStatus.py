from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import pandas as pd
from datetime import datetime

# Execution Starting time
Start_Time = datetime.now()

file_input = 'C:\\uniMelb\\DSproject_winterTerm\\TaskCrawling\\2021_7_30\\tasklist_combine_7(new_add).csv'
file_output = 'C:\\uniMelb\\DSproject_winterTerm\\TaskCrawling\\2021_7_30\\tasklist_combine_add_status.csv'

# load task.csv list i have crawled if i have task_list.csv file
task_list = pd.read_csv(file_input)
task_page = list(task_list['task_page'])

# test_page = task_page[0]
# print(test_page)

# <div class="task_details_step_bar__Container-sc-1d7g3xl-0 kqzgXu">
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

task_status = []
for link in task_page:
    try:
        new_status = getStatus(link)
    except IndexError:
        print(link)
    task_status.append(new_status)

# update the worker csv file
task_pageStatus = pd.DataFrame({'task_page': task_page, 'task_status': task_status})
task_pageStatus.to_csv(file_output, index=False, sep=',')

# Execution Ending time
End_Time = datetime.now()

# total time Measure
Total_Time = End_Time - Start_Time
print("Total execution time was " + str(Total_Time))