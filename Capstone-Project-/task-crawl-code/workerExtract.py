import pandas as pd
from datetime import datetime

# Execution Starting time
Start_Time = datetime.now()

# file_input = 'C:\\uniMelb\\DSproject_winterTerm\\TaskCrawling\\CloseStatus\\tasklist_combine_5_closeStatus_0708.csv'
file_input = 'C:\\uniMelb\\DSproject_winterTerm\\TaskCrawling\\CloseStatus\\tasklist_0730_closeStatus_0730.csv'
file_output = 'C:\\uniMelb\\DSproject_winterTerm\\WorkerCrawling\\0730extract\\0730_0730_close.csv'

# load tasks.csv list
task_list = pd.read_csv(file_input)
task_page = list(task_list['task_page'])
workerList = list(task_list['workerList'])

workers_page = []
for i in range(0,len(task_page)):
    new_workerList = workerList[i].strip('[]')
    if new_workerList == '':
        pass
    else:
        new_wlist = new_workerList.split(', ')
        for new_workers in new_wlist:
            new_workers_str = new_workers.strip('\'')
            if new_workers_str not in workers_page:
                workers_page.append(new_workers_str)
            else:
                pass


    # if len(newList) == 0:
    #     pass
    # elif len(newList) == 1:
    #     new_worker = workerList[i].strip('[]')
    #     new_worker_str = new_worker.strip('\'')
    #     if new_worker_str not in workers_page:
    #         workers_page.append(new_worker_str)
    #     else:
    #         pass
    # else:
    #     new_workerList = workerList[i].strip('[]').split(',')
    #     for new_workers in new_workerList:
    #         new_workers_str = new_workers.strip('\'')
    #         if new_workers_str not in workers_page:
    #             workers_page.append(new_workers_str)
    #         else:
    #             pass

# store result in csv file
workerExtract = pd.DataFrame({'worker_page': workers_page})
workerExtract.to_csv(file_output, index=False, sep=',')

# Execution Ending time
End_Time = datetime.now()

# total time Measure
Total_Time = End_Time - Start_Time
print("Total execution time was " + str(Total_Time))