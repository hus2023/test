from bs4 import BeautifulSoup  # required to parse html
import requests  # required to make request
import csv
import datetime

# read file
urls = ['https://www.gumtree.com.au/s-ad/gardenvale/electrical/saffer-electrics-pty-ltd/1241218382',
'https://www.gumtree.com.au/s-ad/st-kilda/electrical/benjamin-o-rourke-electrical-services/1247182379',
'https://www.gumtree.com.au/s-ad/mill-park/other-building-construction/1-7t-mini-excavator-kanga-dingo-dry-hire/1275760693',
'https://www.gumtree.com.au/s-ad/mulgrave/electrical/a-grade-professional-electrician-free-quotes/1260639098',
'https://www.gumtree.com.au/s-ad/caroline-springs/mechanics-garages/super-mobile-mechanic/1268984791',
'https://www.gumtree.com.au/s-ad/officer/landscaping-gardening/dingo-hire-with-experienced-operator-for-excavating-and-concreting/1067992036',
'https://www.gumtree.com.au/s-ad/fitzroy/handyman/handyman-all-around-electrician/1280404198',
'https://www.gumtree.com.au/s-ad/preston/electrical/elevator-services/1248795750',
'https://www.gumtree.com.au/s-ad/epping/other-automotive/qualified-auto-electrician-epping-vic-3076/1280353344',
'https://www.gumtree.com.au/s-ad/pakenham/other-business-services/fibreglass-and-boat-repairs/1280288171',
'https://www.gumtree.com.au/s-ad/dingley-village/electrical/electricians-based-in-dingley-village/1280248623',
'https://www.gumtree.com.au/s-ad/narre-warren-east/carpentry/house-renovations-free-quote-quick-fast-reliable/1280202027',
'https://www.gumtree.com.au/s-ad/sandringham/electrical/sandringham-electrician-bell-electrical-contractors/1280119140',
'https://www.gumtree.com.au/s-ad/spotswood/electrical/a-grade-electrician-mokka-electrical/1280111189',
'https://www.gumtree.com.au/s-ad/clyde/cars-trailers-excavators-hire/direct-dingo-excavations-hire-with-experienced-operator/1138835391',
'https://www.gumtree.com.au/s-ad/truganina/mechanics-garages/quickfix-auto-service-mechanical-tyre-auto-electrician/1280102388',
'https://www.gumtree.com.au/s-ad/tarneit/other-hiring/electrician-apprenticeship-wanted/1279986515',
'https://www.gumtree.com.au/s-ad/roxburgh-park/air-conditioning-heating/jls-electrical-data-services-air-conditioning-installation/1279968750',
'https://www.gumtree.com.au/s-ad/roxburgh-park/other-business-services/jls-electrical-data-services/1279966659',
'https://www.gumtree.com.au/s-ad/langwarrin/electrical/qualified-electrician/1241795758',
'https://www.gumtree.com.au/s-ad/melbourne-cbd/electrical/electrician-builder-handyman/1279847654',
'https://www.gumtree.com.au/s-ad/flemington/electrical/emergency-electrician-/1239590155',
'https://www.gumtree.com.au/s-ad/cranbourne-east/other-business-services/qualified-a-grade-electrician/1279831539',
'https://www.gumtree.com.au/s-ad/dandenong/electrical/reliable-electrician/1279792072',
'https://www.gumtree.com.au/s-ad/mill-park/electrical/cheap-and-reliable-electrician-/1279729860',
'https://www.gumtree.com.au/s-ad/werribee/electrical/quality-affordable-electrician/1279726587',
'https://www.gumtree.com.au/s-ad/east-bendigo/landscaping-gardening/mini-excavator-hire-kubota-1-7t-trailer-buckets-hammer-bendigo/1279704547',
'https://www.gumtree.com.au/s-ad/altona-meadows/electrical/licensed-electrician/1279704481',
'https://www.gumtree.com.au/s-ad/keilor-downs/electrical/local-electrician/1279692134',
'https://www.gumtree.com.au/s-ad/bentleigh-east/electrical/electrician-electrical-contractor/1230984749',
'https://www.gumtree.com.au/s-ad/craigieburn/electrical/a-grade-electrician-residential-commercial-industrial/1264010313',
'https://www.gumtree.com.au/s-ad/berwick/electrical/electrician-berwick-electrical-installations-and-maintenance/1249998043',
'https://www.gumtree.com.au/s-ad/noble-park/electrical/looking-for-electrician-to-fix-antenna-alignment/1279433270',
'https://www.gumtree.com.au/s-ad/mickleham/other-automotive/mobile-auto-electrician/1275572993',
'https://www.gumtree.com.au/s-ad/brighton/electrical/professional-electrician-cheap-prices-/1279393902',
'https://www.gumtree.com.au/s-ad/narre-warren-south/electrical/woke-electrics-licenced-and-insured-electrician-/1276191459',
'https://www.gumtree.com.au/s-ad/melbourne-cbd/electrical/affordable-electrician/1279349308',
'https://www.gumtree.com.au/s-ad/caulfield-north/electrical/electrician/1279342436',
'https://www.gumtree.com.au/s-ad/keysborough/electrical/local-electrician-/1269092814',
'https://www.gumtree.com.au/s-ad/cairnlea/electrical/electrician/1159382196',
'https://www.gumtree.com.au/s-ad/mill-park/electrical/electrical-services-lights-power-data-security/1279093359',
'https://www.gumtree.com.au/s-ad/croydon-south/other-business-services/cec-accredited-electrician-solar-installer-required/1279063087',
'https://www.gumtree.com.au/s-ad/rowville/other-building-construction/shipping-container-self-contained-bedroom/1278608864',
'https://www.gumtree.com.au/s-ad/truganina/electrical/local-electrician/1278319936',
'https://www.gumtree.com.au/s-ad/glenroy/electrical/a-grade-electrrician-for-solar-installation/1278265251',
'https://www.gumtree.com.au/s-ad/mentone/electrical/kingston-bayside-electrician/1278237507',
'https://www.gumtree.com.au/s-ad/alfredton/electrical/electrician-apprenticeship/1278158819',
'https://www.gumtree.com.au/s-ad/tarneit/electrical/electrician-instant-quotes-tv-wall-mounts-pillar-lights-downlights-/1277855129',
'https://www.gumtree.com.au/s-ad/hallam/electrical/electrician-your-power-services-any-job-big-or-small/1277853650',
'https://www.gumtree.com.au/s-ad/langwarrin/electrical/electrician-for-all-your-needs/1277616881',
'https://www.gumtree.com.au/s-ad/southbank/handyman/all-purpose-handy-man/1277516197',
'https://www.gumtree.com.au/s-ad/keysborough/electrical/electrician/1277429993',
'https://www.gumtree.com.au/s-ad/seabrook/electrical/local-qualified-electrician/1277413393',
'https://www.gumtree.com.au/s-ad/keysborough/handyman/stylish-home-renovation/1277405641',
'https://www.gumtree.com.au/s-ad/seaford/carpentry/home-renovations-free-quote-/1277249847',
'https://www.gumtree.com.au/s-ad/melbourne-cbd/carpentry/need-a-builder-s-license-get-qualified-today-via-rpl/1277199317',
'https://www.gumtree.com.au/s-ad/endeavour-hills/other-building-construction/electricians-kit-new-no-negotiable-pick-up-endeavour-hills/1277185568',
'https://www.gumtree.com.au/s-ad/lalor/electrical/electrician-all-electrical-work-/1277174695',
'https://www.gumtree.com.au/s-ad/fitzroy-north/electrical/a-grade-electrician/1277173048',
'https://www.gumtree.com.au/s-ad/pearcedale/electrical/sams-sparky-services/1271641991',
'https://www.gumtree.com.au/s-ad/narre-warren-south/electrical/smart-connect-electrics-electrician-/1276655022',
'https://www.gumtree.com.au/s-ad/wendouree/electrical/6-66kw-trina-panels-fronius-5kw-921-21/1241763083',
'https://www.gumtree.com.au/s-ad/greenvale/hsc-university-school-tutoring/maths-physics-tutor-year-7-to-12/1275932639',
'https://www.gumtree.com.au/s-ad/clifton-springs/electrical/electrician/1256974756',
'https://www.gumtree.com.au/s-ad/melton-south/electrical/status-electrical-data/1270441882',
'https://www.gumtree.com.au/s-ad/ocean-grove/air-conditioning-heating/white-ceiling-fan-free-/1275111171',
'https://www.gumtree.com.au/s-ad/epping/electrical/a-grade-electrician-electrical-services-power-lighting-/1273912791',
'https://www.gumtree.com.au/s-ad/shepparton/electrical/licenced-electricial-contractor/1274886871',
'https://www.gumtree.com.au/s-ad/sydenham/electrical/grey-army-electrical-service/1274822648',
'https://www.gumtree.com.au/s-ad/officer/electrical/mr-bright-side-electrical/1274790538',
'https://www.gumtree.com.au/s-ad/werribee/electrical/your-local-domestic-electrician-and-safety-compliance-auditor/1274325748',
'https://www.gumtree.com.au/s-ad/narre-warren/electrical/qualified-electrician/1274257946',
'https://www.gumtree.com.au/s-ad/warrnambool/electrical/edwards-electrical-contracting/1273692817',
'https://www.gumtree.com.au/s-ad/keilor-lodge/electrical/a-grade-electrician-fully-insured-free-quotes/1273635539',
'https://www.gumtree.com.au/s-ad/toorak/electrical/emergency-electrician-and-solar-installations-toorak/1273624077',
'https://www.gumtree.com.au/s-ad/glen-iris/electrical/electrician-glen-iris-experienced-qualified-and-reliable/1273621937',
'https://www.gumtree.com.au/s-ad/glen-waverley/electrical/electrician-glen-waverley/1273550490',
'https://www.gumtree.com.au/s-ad/carnegie/electrical/electrician-all-areas-24-7-all-jobs-/1273380147',
'https://www.gumtree.com.au/s-ad/mount-waverley/carpentry/building-construction-and-carpentry/1273366688',
'https://www.gumtree.com.au/s-ad/point-cook/other-automotive/mobile-auto-electrician/1273270331',
'https://www.gumtree.com.au/s-ad/bendigo/electrical/electrician-bendigo/1273177225',
'https://www.gumtree.com.au/s-ad/lower-plenty/electrical/local-electrician/1273168081',
'https://www.gumtree.com.au/s-ad/kilsyth/carpentry/s-j-construction-group/1273158792',
'https://www.gumtree.com.au/s-ad/chirnside-park/electrical/electrician-core-power-electrical-services-/1273113252',
'https://www.gumtree.com.au/s-ad/seaford/other-automotive/-4r-motors-european-automotive-engineers-spare-parts-since-1962/1057106526',
'https://www.gumtree.com.au/s-ad/lake-boga/electrical/lithium-bus-motorhome-off-grid-kit-13999/1272999137',
'https://www.gumtree.com.au/s-ad/blackburn/electrical/reliable-electrician-in-blackburn/1272804438',
'https://www.gumtree.com.au/s-ad/kurunjang/handyman/that-guys-home-handyman-service/1272756080',
'https://www.gumtree.com.au/s-ad/meadow-heights/mechanics-garages/licensed-mobile-auto-electrician/1272752148',
'https://www.gumtree.com.au/s-ad/truganina/handyman/welder-fabricator-mechanic-electrician/1272716930',
'https://www.gumtree.com.au/s-ad/essendon/electrical/electrician-essendon/1272584095',
'https://www.gumtree.com.au/s-ad/mill-park/electrical/electrician/1272564375',
'https://www.gumtree.com.au/s-ad/pakenham/electrical/seasoned-solar/1272158232',
'https://www.gumtree.com.au/s-ad/hampton-east/electrical/electrician/1272108641',
'https://www.gumtree.com.au/s-ad/healesville/electrical/dcp-electrical-fast-friendly-and-reliable-electricians/1271731133',
'https://www.gumtree.com.au/s-ad/mill-park/electrical/after-hours-maintenance-electrician/1271497158',
'https://www.gumtree.com.au/s-ad/werribee/air-conditioning-heating/split-system-installs-in-werribee-area-prices-starting-from-650/1271434430',
'https://www.gumtree.com.au/s-ad/narre-warren/electrical/electrician/1271369027',
'https://www.gumtree.com.au/s-ad/south-morang/electrical/guy-sacco-electrical/1271125262',
'https://www.gumtree.com.au/s-ad/glenroy/electrical/electrician-electrical-contractor/1270764710',
'https://www.gumtree.com.au/s-ad/kingsville/electrical/electrical-work-/1270551937',
'https://www.gumtree.com.au/s-ad/mulgrave/electrical/electrician/1270496000',
'https://www.gumtree.com.au/s-ad/wollert/electrical/electrician-services/1270476303',
'https://www.gumtree.com.au/s-ad/frankston/handyman/handyman-services/1270028858',
'https://www.gumtree.com.au/s-ad/melton-south/electrical/spark-it-up/1269966870',
'https://www.gumtree.com.au/s-ad/altona/electrical/electrician-available-24-7-service/1269798557',
'https://www.gumtree.com.au/s-ad/wheelers-hill/electrical/electrician-wheelers-hill-available-24-7/1269376959',
'https://www.gumtree.com.au/s-ad/preston/electrical/qualified-electrician/1268325886',
'https://www.gumtree.com.au/s-ad/drouin/electrical/electrician-south-east-suburb-gippsland-/1268295843',
'https://www.gumtree.com.au/s-ad/werribee/electrical/featherbrook-electrical-pty-ltd/1266511186',
'https://www.gumtree.com.au/s-ad/mentone/electrical/ammp-electric-a-grade-electrician/1265157319',
'https://www.gumtree.com.au/s-ad/bendigo/electrical/free-led-globe-upgrade-installed-by-a-local-licenced-electrician/1265056898',
'https://www.gumtree.com.au/s-ad/melbourne-cbd/tools-equipment-hire/perfect-addiction-dingo-hire-and-handyman-services-/1261376991',
'https://www.gumtree.com.au/s-ad/point-cook/air-conditioning-heating/electrician-point-cook-mitsubishi-air-conditioner-installation/1258943306',
'https://www.gumtree.com.au/s-ad/werribee/electrical/melbourne-electrician/1257972416',
'https://www.gumtree.com.au/s-ad/epping/electrical/a-grade-licensed-electrician-cheapest-prices/1257467266',
'https://www.gumtree.com.au/s-ad/ormond/electrical/electrician-quality-work-reasonable-price-/1254998708',
'https://www.gumtree.com.au/s-ad/wallan/other-automotive/mobile-caravan-electrician/1254712258',
'https://www.gumtree.com.au/s-ad/preston/electrical/preston-electrician-your-local-high-quality-electrical-contractors/1252556004',
'https://www.gumtree.com.au/s-ad/bacchus-marsh/other-business-services/electrician-melbourne-all-electrical-cctv-sec-installations/1250983179',
'https://www.gumtree.com.au/s-ad/hampton-park/electrical/spilt-system-installs-and-electrical-works/1249946056',
'https://www.gumtree.com.au/s-ad/melbourne-region/mechanics-garages/auto-electrician-service-jag-automotive-solutions/1190799997',
'https://www.gumtree.com.au/s-ad/glenroy/electrical/electrician-electrical-installation-maintenance-and-repairs-/1248252419',
'https://www.gumtree.com.au/s-ad/campbellfield/electrical/mts-electric-service-and-renovation/1247607569',
'https://www.gumtree.com.au/s-ad/mulgrave/electrical/electrician-electrical-security-great-rates-registered-insured-/1247178536',
'https://www.gumtree.com.au/s-ad/cranbourne-east/electrical/nad-electrical/1244504878',
'https://www.gumtree.com.au/s-ad/cranbourne-east/air-conditioning-heating/airconditioning-heating-installation-split-system-specialist/1131911977',
'https://www.gumtree.com.au/s-ad/carnegie/electrical/electrician-quality-service-at-affordable-prices-electrical-air-con/1239446162',
'https://www.gumtree.com.au/s-ad/caroline-springs/electrical/electrician-services/1237864099',
'https://www.gumtree.com.au/s-ad/mitcham/other-business-services/electrician-industrial-commercial-domestic/1232011650',
'https://www.gumtree.com.au/s-ad/thomastown/electrical/electrician/1231625568',
'https://www.gumtree.com.au/s-ad/thomastown/electrical/industrial-electrician-installation-maintenance-and-repairs-/1230871992',
'https://www.gumtree.com.au/s-ad/doncaster/electrical/manningham-area-electrician/1225480498',
'https://www.gumtree.com.au/s-ad/knoxfield/electrical/electrician/1212654516',
'https://www.gumtree.com.au/s-ad/glenroy/electrical/led-downlights-install-upgarde-or-repair-electrician/1212108953',
'https://www.gumtree.com.au/s-ad/melbourne-cbd/mechanics-garages/mobile-auto-electrician-vic-wide/1202319008',
'https://www.gumtree.com.au/s-ad/south-morang/electrical/electrician/1190631813',
'https://www.gumtree.com.au/s-ad/bellfield/electrical/elecontrol-services-electrical-contractor/1189382478',
'https://www.gumtree.com.au/s-ad/taylors-hill/electrical/electrician/1178120909',
'https://www.gumtree.com.au/s-ad/melbourne-cbd/other-business-services/i-generate-leads-for-small-businesses/1169316147',
'https://www.gumtree.com.au/s-ad/melbourne-cbd/electrical/jws-electrical-services-solar-installation/1140755074',
'https://www.gumtree.com.au/s-ad/northcote/other-automotive/about-town-mobile-mechanics-melbourne/1077418579',
'https://www.gumtree.com.au/s-ad/collingwood/other-automotive/mobile-auto-electrician-melbourne/1042162533',
'https://www.gumtree.com.au/s-ad/taylors-lakes/electrical/local-electrician/1279692134',
'https://www.gumtree.com.au/s-ad/mulgrave/electrical/spelectrical-residential-and-commercial-mulgrave-electricians/1246379704',
'https://www.gumtree.com.au/s-ad/craigieburn/electrical/hakwa-solutions/1241987182',
'https://www.gumtree.com.au/s-ad/thomastown/electrical/electrician-electrical-contractor-/1242970185',
'https://www.gumtree.com.au/s-ad/st-albans/air-conditioning-heating/boost-electrical/1281024195',
'https://www.gumtree.com.au/s-ad/mill-park/electrical/cheap-reliable-licensed-electrician/1281022052',
'https://www.gumtree.com.au/s-ad/truganina/mechanics-garages/quickfix-auto-service-mechanical-tyre-auto-electrician/1280832384',
'https://www.gumtree.com.au/s-ad/melbourne-cbd/mechanics-garages/mobile-mechanic-auto-electrician-cars-and-motorbikes-7-days/1276829380',
'https://www.gumtree.com.au/s-ad/glenroy/electrical/electrician-electrical-contractor-/1269390151',
'https://www.gumtree.com.au/s-ad/richmond/electrical/qualified-electrician/1268325886',
'https://www.gumtree.com.au/s-ad/bundoora/electrical/electrician-24-7-cheap-reliable-insured-professional-/1219900047',
'https://www.gumtree.com.au/s-ad/keilor-downs/electrical/electrician-24-7/1281136590',
'https://www.gumtree.com.au/s-ad/rowville/graphic-web-design/websites-graphic-design-photography-tech-support-services/1281114158',
'https://www.gumtree.com.au/s-ad/melbourne-cbd/other-business-services/sentenal-technologies/1281214864',
'https://www.gumtree.com.au/s-ad/werribee/electrical/quality-affordable-electrician/1281199988',
'https://www.gumtree.com.au/s-ad/pakenham/electrical/a-grade-electrician/1269450345',
'https://www.gumtree.com.au/s-ad/clayton-south/electrical/electrician-/1281587879',
'https://www.gumtree.com.au/s-ad/doreen/electrical/electrical-stock-bulk-electrician-stock/1281484666',
'https://www.gumtree.com.au/s-ad/wheelers-hill/electrical/emergency-electrician-wheeler-hill-servicing-melbourne-se-melbourne/1281387986',
'https://www.gumtree.com.au/s-ad/mickleham/electrical/powercorp-electrical-services/1281349731',
'https://www.gumtree.com.au/s-ad/truganina/mechanics-garages/quickfix-auto-service-mechanical-tyre-auto-electrician/1281308635',
'https://www.gumtree.com.au/s-ad/keilor-downs/electrical/electrician-qualified-/1281136590',
'https://www.gumtree.com.au/s-ad/cranbourne-west/electrical/domestic-electrical-work/1281790492',]

for url in urls:
    # fetch content from server
    html = requests.get(url).content
    # soup fetched content
    soup = BeautifulSoup(html, 'html.parser')

    # variables initialised
    profile_list = []
    company = []
    suburb = []
    name = []
    description = []
    Expertise = []
    license_number = []
    rating = []
    date = []
    # variables extracted

    # company name
    try:
        company.append(soup.find('h1', class_='vip-ad-title__header').text)
        print(f'Company name: {company}')
    except:
        company.append(" ")

    # suburb
    try:
        suburb.append(
            soup.find('span', class_='vip-ad-title__location-address').text)
        print(f'Location: {suburb}')
    except:
        suburb.append(" ")

    # name
    try:
        name.append(soup.find('span', class_='seller-profile__name').text)
        print(f'Name: {name}')
    except:
        name.append(" ")

    # description
    try:
        description.append(
            soup.find('div', class_='vip-ad-description__content').text)
        print(f'Description: {description}')
    except:
        description.append(" ")

    # Expertise
    try:
        Expertise.append(soup.find('div', class_='vip-ad-services__list').text)
        print(f'Expertise: {Expertise}')
    except:
        Expertise.append(" ")

    # license number
    try:
        ln = soup.select_one('.vip-ad-attributes__value:-soup-contains("Accreditation") + span').text
        license_number.append(ln) if ln else " "
        #license_number.append(soup.find('span', class_='vip-ad-attributes__name').text)
        print(f'license_number: {license_number}')
    except:
        license_number.append(" ")
    
    #Rating
    try:
        rating.append(soup.find('span', class_='rating__score-text').text.replace(" / 5",""))
        print(f'Rating: {rating}')
    except:
        rating.append(" ")
    
    #url
    profile_url = []
    profile_url.append(url)
    
    #date
    d = datetime.datetime.now()
    print(f'Date: {d.strftime("%x")}')
    date.append(d)
       
    profile_list = list(zip(company, name, suburb,description,Expertise,license_number,rating,profile_url,date))

    with open('gumtree_worker_allprofiles_0925.csv', 'a') as f:
        worker = csv.writer(f)
        for i in profile_list:
            worker.writerow(i)
        f.close() 