from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urljoin
import pandas as pd
from datetime import datetime
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Execution Starting time
Start_Time = datetime.now()

serviceLocation = []
file_output = 'C:\\uniMelb\\DSproject_winterTerm\\service.com.au\\serviceLocationList.csv'

area_url = 'https://www.service.com.au/find/electrician/vic/suburbs'

Apage = requests.get(area_url)
ASoup = BeautifulSoup(Apage.text, 'html.parser')

base_url = 'https://www.service.com.au'

places = ASoup.findAll('a',href=re.compile("^/find/electrician/"))
for place in places:
    area_url = place['href']
    area_page = urljoin(base_url, area_url)
    if area_page not in serviceLocation:
        serviceLocation.append(area_page)
    else:
        pass

locationUrl_get = pd.DataFrame({'location_page': serviceLocation})
locationUrl_get.to_csv(file_output, index=False, sep=',')

# Execution Ending time
End_Time = datetime.now()

# total time Measure
Total_Time = End_Time - Start_Time
print("Total execution time was " + str(Total_Time))
