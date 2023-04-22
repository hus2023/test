from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urljoin
import pandas as pd
from datetime import datetime

# Execution Starting time
Start_Time = datetime.now()

area_page = []
file_output = 'C:\\uniMelb\\DSproject_winterTerm\\serviceseeking\\autoCrawl\\Location_Url_List.csv'

initial_url = 'https://www.serviceseeking.com.au/electricians/vic'

page = requests.get(initial_url)
Soup = BeautifulSoup(page.text, 'html.parser')

base_url = 'https://www.serviceseeking.com.au'
#<div class="container mb30">
locationSecs = Soup.findAll('a',href=re.compile("^/electricians/vic/"))
for area in locationSecs:
    location_url = area['href']
    location_page = urljoin(base_url,location_url)
    if location_page not in area_page:
        area_page.append(location_page)

locationUrl_get = pd.DataFrame({'location_page': area_page})
locationUrl_get.to_csv(file_output, index=False, sep=',')

# Execution Ending time
End_Time = datetime.now()

# total time Measure
Total_Time = End_Time - Start_Time
print("Total execution time was " + str(Total_Time))