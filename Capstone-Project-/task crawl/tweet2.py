from bs4 import BeautifulSoup  # required to parse html
import requests  # required to make request
import csv

# read file
with open('task_list2.csv', 'r') as f:
    csv_raw_cont = f.read()

# split by line
split_csv = csv_raw_cont.split('\n')

# specify separator
separator = ";"

# iterate over each line
for each in split_csv:

    # specify the row index
    url_row_index = 0  # in our csv example file the url is the first row so we set 0

    # get the url
    url = each.split(separator)[url_row_index]

    # fetch content from server
    html = requests.get(url).content

    # soup fetched content
    soup = BeautifulSoup(html, 'lxml')

    pro = soup.find('div', class_='posted-details')
    loc = soup.find('div', class_= 'location-item posted-details-item')
    time = soup.find('div', class_= 'propose-time-holder posted-details-item')
    budget = soup.find('div',class_= 'sidebar center')
    title = soup.find('div',class_= 'details-panel')
    des = soup.find('div', class_= 'splitter-section-container')

    profile_list = []


    # variables initialised
    postername = []
    Address = []
    duedate = []
    description = []
    prize = []
    tit =[]

    # variables extracted
    try:
        tit.append(title.find('h1', class_='task-title text-h2').text)
    except:
        tit.append("not present")
    try:
        postername.append(pro.find('a', class_='user-name').text)
    except:
        postername.append("not present")

    try:
        Address.append(loc.find('p', class_='text').text)
    except:
        Address.append("not present")


    try:
        duedate.append(time.find('div', class_='time-date').text)
    except:
        duedate.append("not present")
    try:
        prize.append(budget.find('div', class_='price text-h2').span.text)
    except:
        prize.append("not present")

    try:
        description.append(des.find('p', class_='Text__StyledTypographyComponent-sc-35e02v-0 gIiAgB').text)
    except:
        description.append("not present")

    print(f'title: {tit}')
    print(f'posterName: {postername}')
    print(f'Address: {Address}')
    print(f'duedate: {duedate}')
    print(f'prize: {prize}')
    print(f'About: {description} \n')


    # header_names = ["Name","Address","Member Since","Description","No of Stars out of 5","Total Reviews given","Tasks Completed","Completion Rate"
    #             ,"Education","Specialities","Languages","Experience","Transportation"]
    profile_list = list(zip(tit,postername, Address, duedate,prize , description))

    with open('AllTaskinfoo.csv', 'a') as f:
        worker = csv.writer(f)
        # writing header row
        # worker.writerow({x: x for x in header_names})
        for i in profile_list:
            worker.writerow(i)
        f.close()