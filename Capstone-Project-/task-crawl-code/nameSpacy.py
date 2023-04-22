from datetime import datetime
import pandas as pd
import spacy
import re

# Execution Starting time
Start_Time = datetime.now()

file_input = 'C:\\uniMelb\\DSproject_winterTerm\\taskname\\allTaskName.csv'
file_output = 'C:\\uniMelb\\DSproject_winterTerm\\taskname\\NounKeyList_trf.csv'

# load the taskName list csv file
tasKName_list = pd.read_csv(file_input)
taskNameList = list(tasKName_list['task_name'])

newNameList = []
for name in taskNameList:
    new_Lname = name.lower()
    nameL = new_Lname.split()
    nalList = []
    for nal in nameL:
        nal_1 = nal.replace("/", " ")
        nal_2 = nal_1.strip('-!?.)(,"\';:')
        nal_3 = re.sub(r'\d+', '', nal_2)
        nalList.append(nal_3)
    str_nal = " "
    new_nal = str_nal.join(nalList)
    newNameList.append(new_nal)
#print(newNameList)

# using spaCy # sm/trf
nlp = spacy.load("en_core_web_trf")
def nounExtract(taskName):
    doc = nlp(taskName)
    resultList = []
    for chunk in doc.noun_chunks:
        resultList.append(chunk.text)
    return resultList

NounCount = {}

for nName in newNameList:
    nNounL = nounExtract(nName)
    for nN in nNounL:
        if nN in NounCount:
            NounCount[nN] = NounCount[nN] + 1
        else:
            NounCount[nN] = 1

NounCount = {k: v for k, v in sorted(NounCount.items(), key=lambda item: item[1], reverse=True)}
#for key in NounCount : print(key, NounCount[key])

Nounkey = []
keyCount = []
for key in NounCount:
    Nounkey.append(key)
    keyCount.append(NounCount[key])

# load result in CSV file
NounKeyList_sm = pd.DataFrame({'Noun_key':Nounkey, 'key_Count':keyCount})
NounKeyList_sm.to_csv(file_output, index=False, sep=',')


# Execution Ending time
End_Time = datetime.now()

# total time Measure
Total_Time = End_Time - Start_Time
print("Total execution time was " + str(Total_Time))