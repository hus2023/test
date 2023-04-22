from bs4 import BeautifulSoup  # required to parse html
import requests  # required to make request
import re
import csv


# read file
urls = [
    'https://www.serviceseeking.com.au/profile/80028?source=',
'https://www.serviceseeking.com.au/profile/57447?source=',
'https://www.serviceseeking.com.au/profile/231543?source=',
'https://www.serviceseeking.com.au/profile/212435?source=',
'https://www.serviceseeking.com.au/profile/148583?source=',
'https://www.serviceseeking.com.au/profile/9382?source=',
'https://www.serviceseeking.com.au/profile/89973?source=',
'https://www.serviceseeking.com.au/profile/189129?source=',
'https://www.serviceseeking.com.au/profile/239095?source=',
'https://www.serviceseeking.com.au/profile/197972?source=',
'https://www.serviceseeking.com.au/profile/153242?source=',
'https://www.serviceseeking.com.au/profile/70663?source=',
'https://www.serviceseeking.com.au/profile/86130?source=',
'https://www.serviceseeking.com.au/profile/172160?source=',
'https://www.serviceseeking.com.au/profile/62941?source=',
'https://www.serviceseeking.com.au/profile/65208?source=',
'https://www.serviceseeking.com.au/profile/86967?source=',
'https://www.serviceseeking.com.au/profile/83956?source=',
'https://www.serviceseeking.com.au/profile/137947?source=',
'https://www.serviceseeking.com.au/profile/123501?source=',
'https://www.serviceseeking.com.au/profile/207218?source=',
'https://www.serviceseeking.com.au/profile/106871?source=',
'https://www.serviceseeking.com.au/profile/110529?source=',
'https://www.serviceseeking.com.au/profile/160052?source=',
'https://www.serviceseeking.com.au/profile/187241?source=',
'https://www.serviceseeking.com.au/profile/244415?source=',
'https://www.serviceseeking.com.au/profile/86328?source=',
'https://www.serviceseeking.com.au/profile/78036?source=',
'https://www.serviceseeking.com.au/profile/104886?source=',
'https://www.serviceseeking.com.au/profile/27073?source=',
'https://www.serviceseeking.com.au/profile/62635?source=',
'https://www.serviceseeking.com.au/profile/173529?source=',
'https://www.serviceseeking.com.au/profile/219597?source=',
'https://www.serviceseeking.com.au/profile/76680?source=',
'https://www.serviceseeking.com.au/profile/74543?source=',
'https://www.serviceseeking.com.au/profile/31882?source=',
'https://www.serviceseeking.com.au/profile/89495?source=',
'https://www.serviceseeking.com.au/profile/45655?source=',
'https://www.serviceseeking.com.au/profile/142419?source=',
'https://www.serviceseeking.com.au/profile/85671?source=',
'https://www.serviceseeking.com.au/profile/82818?source=',
'https://www.serviceseeking.com.au/profile/217438?source=',
'https://www.serviceseeking.com.au/profile/191188?source=',
'https://www.serviceseeking.com.au/profile/232221?source=',
'https://www.serviceseeking.com.au/profile/157473?source=',
'https://www.serviceseeking.com.au/profile/226579?source=',
'https://www.serviceseeking.com.au/profile/86739?source=',
'https://www.serviceseeking.com.au/profile/127907?source=',
]
serviceseek_list = []

for url in urls:
    # specify the row index; in our csv example file the url is the first row so we set 0
    html = requests.get(url).content  # fetch content from server
    soup = BeautifulSoup(html, 'html.parser')

    # Electrical Company
    try:
        ec = []
        ec.append(
            soup.find("div", class_="font-21 bold pb4 mt16 sm-mt0 text-copy-2").text)
        #print(f'Company: {ec}')
    except:
        ec.append(" ")

    # Electrician Name
    try:
        name = []
        name.append(soup.select_one(
            ".ficon-user").find_next("div").get_text(strip=True))
        print(f'Name: {name}')
    except:
        name.append(" ")

    # Suburb
    try:
        addr = []
        addr.append(soup.select_one(
            ".ficon-coverage").find_next("div").get_text(strip=True))
        #print(f'Address: {addr}')
    except:
        addr.append(" ")

    # ABN
    try:
        abn = []
        abn.append(soup.select_one(
            'strong:-soup-contains("ABN")').find_next_sibling(text=True))
        #print(f'ABN: {abn}')
    except:
        abn.append(" ")

    # Licence Number
    try:
        vic_licence = []
        vic = soup.select_one('.license-name:-soup-contains("VIC Energy Safe") + div').text
        vic_licence.append(vic) if vic else "N/A"
        print(f"Licence Number:{vic_licence}")
    except:
        vic_licence.append(" ")

    # Reviews
    try:
        rev = []
        rev.append(soup.find(
            "a", class_="js-scroll-to-reviews color-black-hover flat-link").text.replace('Reviews', ''))
        #print(f'Reviews: {rev}')
    except:
        rev.append(" ")

    # Rating
    try:
        rating = []
        rat = soup.find("span", class_="star-rating star-rating-sm").text
        rating.append(int(re.search(r'\d+', rat).group(0)))
        #print(f'Rating: {rating}')
    except:
        rating.append(" ")

    # Description
    try:
        desc = []
        desc.append(
            soup.find("div", class_="card-content card-pad-md card-section pb8 pt24").text)
        #print(f'Decription: {desc}')
    except:
        desc.append(" ")

    # #Number of times hired
    # try:
    #     hire = []
    #     hired = soup.find("div",class_= "col-xs-12 border-bottom p0 pt8 pb8").text
    #     hire.append(int(re.search(r'\d+', hired).group(0)))
    #     #print(f'Hired: {hire}')
    # except:
    #     hire.append(" ")

    # #Response Time
    # try:
    #     res = []
    #     res.append(soup.find_all("div",class_= "col-xs-12 border-bottom p0 pt8 pb8")[2].text.replace('Response time:', ''))
    #     #print(f'Response Time: {res}')
    # except:
    #     res.append(" ")

    profile_url = []
    profile_url.append(url)

    serviceseek_list = list(zip(ec, name, addr, abn, vic_licence, rev, rating,
                                desc, profile_url))

    #df = pd.DataFrame(serviceseek_list, columns=['ec', 'name', 'addr', 'abn', 'vic_licence', 'rev', 'rating',
     #                                            'desc', 'profile_url'])
    
    #df.to_csv('serviceseek_allprofiles0813.csv', index=False, sep=';')
    
    # headerList = ['Company','Electrician Name', 'Address','Member since',
    #             'ABN','Licence Number','Reviews',
    #            'Ratings','Description','Number of Times Hired','Response Time']

    with open('ss_allprofiles0813.csv','a') as file:
        worker = csv.writer(file)
        for i in serviceseek_list:
            worker.writerow(i)
        file.close()
