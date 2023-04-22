from bs4 import BeautifulSoup  # required to parse html
import requests  # required to make request
import csv



# get the url
url = 'https://www.tradiecentre.com.au/australia/girraween/home-commercial-services/action-electricians-sydney-jim-beasley'

# fetch content from server
html = requests.get(url).content

# soup fetched content
soup = BeautifulSoup(html, 'lxml')
clearfix = soup.find_all('div', class_='table-view-group clearfix')
about = soup.find('div', class_='tab-pane active')
deslist = about.find_all('p')

cname0= clearfix[0].find('li', class_= 'col-sm-8')
abn1= clearfix[1].find('li', class_= 'col-sm-8')
web2 = clearfix[2].find('li', class_= 'col-sm-8')
phone4 = clearfix[4].find('li', class_= 'col-sm-8')
loc5 = clearfix[5].find('li', class_= 'col-sm-8')




# variables initialised
cname = []
abn = []
web = []
phone =[]
loc = []
des =[]


# variables extracted
try:
    cname.append(cname0.find('span', class_='textbox textbox-company').text)
except:
    cname.append("not present")

print(cname)
try:
    abn.append(abn1.find('span', class_='textbox textbox-abn').text)
except:
    abn.append("not present")

print(abn)
try:
    web.append(web2.a.get("href"))
except:
    web.append("not present")
print(web)
try:
    phone.append(phone4.span.text)
except:
    phone.append("not present")
print(phone)
try:
    loc.append(loc5.find('span', class_='textarea textarea-locations').text)

except:
    loc.append("not present")
print(loc)

try:
    for i in range(len(deslist)-1):
        des.append(deslist[i].text)

except:
    des.append("not present")
print(des)