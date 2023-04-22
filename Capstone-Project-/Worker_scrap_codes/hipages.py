from bs4 import BeautifulSoup  # required to parse html
import requests  # required to make request
import csv
import datetime
import time

# read file
urls = [
    'https://hipages.com.au/connect/cjelectricalsolutions',
'https://hipages.com.au/connect/ecommelectricalservices',
'https://hipages.com.au/connect/kairoselectrics',
'https://hipages.com.au/connect/xproelectrical',
'https://hipages.com.au/connect/marollaelectrics',
'https://hipages.com.au/connect/sdelectricsptyltd',
'https://hipages.com.au/connect/connectedec',
'https://hipages.com.au/connect/htec',
'https://hipages.com.au/connect/powercoreelectricalservices',
'https://hipages.com.au/connect/smartelectricalsecuritysolutionsptyltd',
'https://hipages.com.au/connect/livesayelectrical',
'https://hipages.com.au/connect/sherbrookeelectrical',
'https://hipages.com.au/connect/tvelectrical',
'https://hipages.com.au/connect/sunlitelectrical',
'https://hipages.com.au/connect/willtesttag',
'https://hipages.com.au/connect/electriciantou',
'https://hipages.com.au/connect/ampcoreelectricalptyltd',
'https://hipages.com.au/connect/megaelectricalgroup',
'https://hipages.com.au/connect/amselectrician',
'https://hipages.com.au/connect/sikalecdataelectrical',
'https://hipages.com.au/connect/phaselogicsptyltd',
'https://hipages.com.au/connect/connectinu',
'https://hipages.com.au/connect/tbtelectrics',
'https://hipages.com.au/connect/lexity',
'https://hipages.com.au/connect/milletrical',
'https://hipages.com.au/connect/johnmasonelectrical',
'https://hipages.com.au/connect/parkerryanelectricalsolutions',
'https://hipages.com.au/connect/eastlecdataandelectrical',
'https://hipages.com.au/connect/darrenselectrical',
'https://hipages.com.au/connect/jetampereelectricalptyltd',
'https://hipages.com.au/connect/onsiteelectrical2',
'https://hipages.com.au/connect/attselectricalservices',
'https://hipages.com.au/connect/gpowerelectricalservices',
'https://hipages.com.au/connect/goodwillelectricalandmaintenance',
'https://hipages.com.au/connect/rdtelectrical',
'https://hipages.com.au/connect/roweelectrical',
'https://hipages.com.au/connect/dpswiredservices',
'https://hipages.com.au/connect/isoelectrical',
'https://hipages.com.au/connect/sparkyspot',
'https://hipages.com.au/connect/lumeservices',
'https://hipages.com.au/connect/princetonelectrical',
'https://hipages.com.au/connect/avonelectrical',
'https://hipages.com.au/connect/solarpluselectrical',
'https://hipages.com.au/connect/mpro',
'https://hipages.com.au/connect/woodelectrical',
'https://hipages.com.au/connect/audaciouselectricalcontractors',
'https://hipages.com.au/connect/boyichgroupptyltd',
'https://hipages.com.au/connect/regenerateelectricalptyltd',
'https://hipages.com.au/connect/tdelectrical',
'https://hipages.com.au/connect/slbsolutionsptyltd',
'https://hipages.com.au/connect/mwgelectricalservices',
'https://hipages.com.au/connect/contactelectricalsolutions',
'https://hipages.com.au/connect/hakwasolutions',
'https://hipages.com.au/connect/ampmodeelectrical',
'https://hipages.com.au/connect/prolekelectrical',
'https://hipages.com.au/connect/fenixaclasselectrical',
'https://hipages.com.au/connect/commanderelectrical',
'https://hipages.com.au/connect/melbourneelectropowerptyltd',
'https://hipages.com.au/connect/festervilleindustries',
'https://hipages.com.au/connect/scopecablingptyltd',
'https://hipages.com.au/connect/wellwired',
'https://hipages.com.au/connect/abbaelectricalservices',
'https://hipages.com.au/connect/leadzelectric',
'https://hipages.com.au/connect/guysaccoelectricalservices',
'https://hipages.com.au/connect/gdelectrical',
'https://hipages.com.au/connect/ttekelectricalservices',
'https://hipages.com.au/connect/jwattelectrix',
'https://hipages.com.au/connect/jasontrevorelectricalcontactor',
'https://hipages.com.au/connect/whelectricalserviceptyltd',
'https://hipages.com.au/connect/mrmelectricalanddata',
'https://hipages.com.au/connect/bcpheatingandcooling',
'https://hipages.com.au/connect/newstarelectrical',
'https://hipages.com.au/connect/selectelectricalcontractors',
'https://hipages.com.au/connect/dptelectrical2',
'https://hipages.com.au/connect/jboxelectrical',
'https://hipages.com.au/connect/newconnectionselectricalptyltd',
'https://hipages.com.au/connect/vantagewiringsolutions',
'https://hipages.com.au/connect/provisionelectricalairconditioningptyltdacn616529438',
'https://hipages.com.au/connect/rytechelectrical',
'https://hipages.com.au/connect/aarpelectricalcontractor',
'https://hipages.com.au/connect/chiefelectriciansptyltd',
'https://hipages.com.au/connect/ecohomeelectrical',
'https://hipages.com.au/connect/gmecmelbourneptyltd',
'https://hipages.com.au/connect/ecofitelectrical',
'https://hipages.com.au/connect/alloverit',
'https://hipages.com.au/connect/adelectricalsolutions',
'https://hipages.com.au/connect/mdunlimitedelectrics',
'https://hipages.com.au/connect/cidelectrics',
'https://hipages.com.au/connect/setcheselectrical',
'https://hipages.com.au/connect/watersidepower2',
'https://hipages.com.au/connect/cmbelectrical',
'https://hipages.com.au/connect/jljelectrical',
'https://hipages.com.au/connect/modelectricalptyltd',
'https://hipages.com.au/connect/wattkinselectrical2',
'https://hipages.com.au/connect/joneselectrixs',
'https://hipages.com.au/connect/davidtensek',
'https://hipages.com.au/connect/gunitelectrics',
'https://hipages.com.au/connect/salselectricalcontractors',
'https://hipages.com.au/connect/lbkelectrics',
'https://hipages.com.au/connect/rjlelectricalcommunications',
'https://hipages.com.au/connect/prioreelectrical',
'https://hipages.com.au/connect/premierelectricalco',
'https://hipages.com.au/connect/fishercoelectricalservices',
'https://hipages.com.au/connect/westvoltelectrical',
'https://hipages.com.au/connect/burlinelectricalptyltd',
'https://hipages.com.au/connect/lapthorneelectrical',
'https://hipages.com.au/connect/wattsebs',
'https://hipages.com.au/connect/vicspark',
'https://hipages.com.au/connect/brightsource2',
'https://hipages.com.au/connect/mpwrelectrical',
'https://hipages.com.au/connect/24hourpowerelectricalservicesptyltd',
'https://hipages.com.au/connect/prencelectrics',
'https://hipages.com.au/connect/adztekelectrical',
'https://hipages.com.au/connect/lighttrailelectrical',
'https://hipages.com.au/connect/elluminatedelectrical',
'https://hipages.com.au/connect/adwireelectrical',
'https://hipages.com.au/connect/smugelectricalservices',
'https://hipages.com.au/connect/payneelectricalsolutionsptyltd',
'https://hipages.com.au/connect/gisvegaselectrical',
'https://hipages.com.au/connect/skgelectricalsolutions2',
'https://hipages.com.au/connect/sjelectricalcontracting',
'https://hipages.com.au/connect/gspecelectricalservices',
'https://hipages.com.au/connect/ogdenelectricalcontracting',
'https://hipages.com.au/connect/gaskettelectricalservices',
'https://hipages.com.au/connect/sjmelectricaldataptyltd',
'https://hipages.com.au/connect/nhcelectrical',
'https://hipages.com.au/connect/markedmondsonelectricalservices2',
'https://hipages.com.au/connect/finlayelectrical',
'https://hipages.com.au/connect/bareautomation',
'https://hipages.com.au/connect/bennettbroselectrical',
'https://hipages.com.au/connect/jwpostleelectrical',
'https://hipages.com.au/connect/altitudeelectrics',
'https://hipages.com.au/connect/correctelectricalservices',
'https://hipages.com.au/connect/rhynoelectricalservice',
'https://hipages.com.au/connect/wharparillaelectricalptyltd',
'https://hipages.com.au/connect/superchargedenergyptyltd',
'https://hipages.com.au/connect/knightselectricool',
'https://hipages.com.au/connect/sjhelectrical',
'https://hipages.com.au/connect/ledriverinaelectrical',
'https://hipages.com.au/connect/trentparkerelectricalservices',
'https://hipages.com.au/connect/cobbincoelectrical',
'https://hipages.com.au/connect/patbyrneelectrical',
'https://hipages.com.au/connect/hirstelectricalservices',
'https://hipages.com.au/connect/alpinevalleyelectrical',
'https://hipages.com.au/connect/mitchellamblerelectrical',
'https://hipages.com.au/connect/jessecoolelectrical',
'https://hipages.com.au/connect/najjelectservicesptyltd',
'https://hipages.com.au/connect/anthonydruittelectricaldata',
'https://hipages.com.au/connect/redelectricalriverina',
'https://hipages.com.au/connect/telephonetechniques',
'https://hipages.com.au/connect/rustaberelectrical',
'https://hipages.com.au/connect/jasonlinsellelectricalcommunication',
'https://hipages.com.au/connect/russellwaight',
'https://hipages.com.au/connect/mattwilsonelectrical2',
'https://hipages.com.au/connect/advancedoneelectricalptyltd',
'https://hipages.com.au/connect/smaelectrical',
'https://hipages.com.au/connect/jdayelectrical',
'https://hipages.com.au/connect/danmelectrical',
'https://hipages.com.au/connect/svhelectrical',
'https://hipages.com.au/connect/efficientelectricalandairconditioning2',
'https://hipages.com.au/connect/kencoelectricalservices',
'https://hipages.com.au/connect/mcintoshelectrical',
'https://hipages.com.au/connect/bookerelectricalcontractors',
'https://hipages.com.au/connect/bennettdapaelectricalcontractors',
'https://hipages.com.au/connect/pilkselectrical2',
'https://hipages.com.au/connect/agelectrical',
'https://hipages.com.au/connect/mysparkysa',
'https://hipages.com.au/connect/jameselectrical2',
'https://hipages.com.au/connect/adelect',
'https://hipages.com.au/connect/wollondillyelectrical',
'https://hipages.com.au/connect/activelectrical',
'https://hipages.com.au/connect/smedleyelectricalservices',
'https://hipages.com.au/connect/anthonykellyelectrical',
'https://hipages.com.au/connect/baycoasteacs',
'https://hipages.com.au/connect/planetearthconnections',
'https://hipages.com.au/connect/dynamic2',
'https://hipages.com.au/connect/primroseelectrical',
'https://hipages.com.au/connect/electrical4solar',
'https://hipages.com.au/connect/hilltopselectricalsolutions2',
'https://hipages.com.au/connect/surefireelectrical',
'https://hipages.com.au/connect/spselectricalcontracting',
'https://hipages.com.au/connect/koalatyelectricalandcontracting',
'https://hipages.com.au/connect/ozlitptyltd',
'https://hipages.com.au/connect/takechargeelectrical',
'https://hipages.com.au/connect/enricsptyltd',
'https://hipages.com.au/connect/yourfriendinthetrade',
]

for url in urls:

    # fetch content from serverclear
    html = requests.get(url).content
    # soup fetched content
    soup = BeautifulSoup(html, 'html.parser')

    # Company
    company = []
    try:
        company.append(soup.select('h1', class_="typography__Text-sc-1junnpl-0 typography__Heading-sc-1junnpl-2 eMRsDt")[0].get_text(separator=" ",
                                                                                                                                     strip=True))
        print(f'Company :{company}')
    except:
        company.append(" ")

    # Name and suburb info
    information = []
    info = []
    name = []
    suburb = []

    try:
        for i in soup.find_all('span', class_='Contact__Item-sc-1giw2l4-2 iLuGcX'):
            information.append(i.text)

        # don't need phone number
        info = information[:2]
        
        #print(info)
        # name
        n = info[0] if "VIC" not in info[0] else " "
        name.append(n)
        print(f'Name: {name}')

        # suburb
        if "VIC" in info[0]:
            s = info[0]
        else:
            s = info[1]
        suburb.append(s)
        print(f'Suburb: {suburb}')

    except:
        name.append(" ")
        suburb.append(" ")

    # About
    description = []
    try:
        parent = soup.find(
            'div', class_='sc-dlnjwi btKpNj').select('div> div:nth-child(2)')
        description.append(parent[0].get_text(strip=True))
        #print(f"Description: {description}")
    except:
        description.append("Contact us today for more information.")

    # Ratings
    rating = []
    try:
        rating.append(soup.find('div', class_='Rating__RatingText-sc-1r9ytu8-1 cfWbGA').get_text(
            strip=True))
        print(f'rating :{rating}')
    except:
        rating.append(" ")

    # licence number
    licence = []
    vic_licence = []
    try:
        for lic in soup.find_all('div', class_='Licences__LicenceBlockWrapper-jotd42-0 gtudFq'):
            licence.append(lic.text)
        # print(licence)
        for k in range(0, len(licence)):
            vic_licence.append(
                licence[k]) if "VIC Energysafe" in licence[k] else " "
        print(f'Licence No.: {vic_licence}')

    except:
        vic_licence.append(" ")

    #url
    profile_url = []
    profile_url.append(url)

    # date
    date = []
    d = datetime.datetime.now()
    #print(f'Date: {d.strftime("%x")}')
    date.append(d)

    profile_list = []
    profile_list = list(zip(company, name, suburb, description,
                        vic_licence, rating, date, profile_url))

    with open('hipages_28_09_V2.csv','a') as f:
        worker = csv.writer(f)
        for i in profile_list:
            worker.writerow(i)
        f.close()

    time.sleep(2)
