from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urljoin
import pandas as pd
from datetime import datetime
from selenium import webdriver

# Execution Starting time
Start_Time = datetime.now()

hiPageLocation = []
file_output = 'C:\\uniMelb\\DSproject_winterTerm\\hiPage\\hiPageLocation.csv'

area_url = 'https://hipages.com.au/find/electricians/vic'

Apage = requests.get(area_url)
ASoup = BeautifulSoup(Apage.text, 'html.parser')

base_url = 'https://hipages.com.au'

places = ASoup.findAll('a',href=re.compile("^/find/electricians/vic/"))
for place in places:
    area_url = place['href']
    area_page = urljoin(base_url, area_url)
    if area_page not in hiPageLocation:
        hiPageLocation.append(area_page)
    else:
        pass

locationUrl_get = pd.DataFrame({'location_page': hiPageLocation})
locationUrl_get.to_csv(file_output, index=False, sep=',')

# Execution Ending time
End_Time = datetime.now()

# total time Measure
Total_Time = End_Time - Start_Time
print("Total execution time was " + str(Total_Time))