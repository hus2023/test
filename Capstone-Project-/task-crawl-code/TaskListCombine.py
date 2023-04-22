from datetime import datetime
import pandas as pd

# Execution Starting time
Start_Time = datetime.now()

# file_input_1 = 'C:\\uniMelb\\DSproject_winterTerm\\TaskCrawling\\2021_7_22\\tasklist_0722_Traralgon_electrician.csv'
# file_input_2 = 'C:\\uniMelb\\DSproject_winterTerm\\TaskCrawling\\2021_7_22\\tasklist_0722_Traralgon_electric.csv'
file_input_1 = 'C:\\uniMelb\\DSproject_winterTerm\\TaskCrawling\\2021_7_30\\tasklist_combine_6.csv'
file_input_2 = 'C:\\uniMelb\\DSproject_winterTerm\\TaskCrawling\\2021_7_30\\tasklist_0730_Traralgon_electrician.csv'

# file_output = 'C:\\uniMelb\\DSproject_winterTerm\\TaskCrawling\\2021_7_22\\tasklist_combine_Traralgon.csv'
file_output = 'C:\\uniMelb\\DSproject_winterTerm\\TaskCrawling\\2021_7_30\\tasklist_combine_7.csv'

task_list_1 = pd.read_csv(file_input_1)
task_list_2 = pd.read_csv(file_input_2)
task_page_1 = list(task_list_1['task_page'])
task_page_2 = list(task_list_2['task_page'])

task_page_out = []

for i in range(0,len(task_page_1)):
    new_page = task_page_1[i]
    if new_page not in task_page_out:
        task_page_out.append(new_page)
    else:
        pass

for i in range(0,len(task_page_2)):
    new_page = task_page_2[i]
    if new_page not in task_page_out:
        task_page_out.append(new_page)
    else:
        pass

task_list_out = pd.DataFrame({'task_page': task_page_out})
task_list_out.to_csv(file_output, index=False, sep=',')

# Execution Ending time
End_Time = datetime.now()

# total time Measure
Total_Time = End_Time - Start_Time
print("Total execution time was " + str(Total_Time))