from datetime import datetime
import pandas as pd

# Execution Starting time
Start_Time = datetime.now()

# file_input_1 = 'C:\\uniMelb\\DSproject_winterTerm\\WorkerCrawling\\workerExtract_combine_5_closeStatus_0708.csv'
# file_input_2 = 'C:\\uniMelb\\DSproject_winterTerm\\WorkerCrawling\\workerExtract_combine_5_closeStatus_0709.csv'
# file_input_1 = 'C:\\uniMelb\\DSproject_winterTerm\\WorkerCrawling\\workerExtract_combine_5_openStatus_0708.csv'
# file_input_2 = 'C:\\uniMelb\\DSproject_winterTerm\\WorkerCrawling\\workerExtract_combine_5_openStatus_0709.csv'
file_input_1 = 'C:\\uniMelb\\DSproject_winterTerm\\WorkerCrawling\\0730extract\\0730_0730_close.csv'
file_input_2 = 'C:\\uniMelb\\DSproject_winterTerm\\WorkerCrawling\\0730extract\\0730_0730_open.csv'

# file_output = 'C:\\uniMelb\\DSproject_winterTerm\\WorkerCrawling\\workers_combineClose_0708_0709.csv'
# file_output = 'C:\\uniMelb\\DSproject_winterTerm\\WorkerCrawling\\workers_combine_Open_0708_0709.csv'
file_output = 'C:\\uniMelb\\DSproject_winterTerm\\WorkerCrawling\\0730extract\\0730_all_1.csv'

# load the 2 workers.csv we want to combine
worker_list_1 = pd.read_csv(file_input_1)
worker_page_1 = list(worker_list_1['worker_page'])
worker_list_2 = pd.read_csv(file_input_2)
worker_page_2 = list(worker_list_2['worker_page'])

workerCombine = []
for workers in worker_page_1:
    if workers not in workerCombine:
        workerCombine.append(workers)
    else:
        pass

for workers in worker_page_2:
    if workers not in workerCombine:
        workerCombine.append(workers)
    else:
        pass

# store the combine result in another csv file
workerCombine = pd.DataFrame({'worker_page': workerCombine})
workerCombine.to_csv(file_output, index=False, sep=',')

# Execution Ending time
End_Time = datetime.now()

# total time Measure
Total_Time = End_Time - Start_Time
print("Total execution time was " + str(Total_Time))