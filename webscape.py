import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

company = []
ceo = []
cto = []
round = []
purpose = []
results =[]
myresults = pd.DataFrame()

i=0
results.append('Line' + str(i))
while i<50:

    status_code =  requests.get('http://18.207.112.240:8000/random_company')
    #status_code = requests.get('http://www.google.com', timeout = None)
    #status_code =  requests.get('http://18.207.92.139:8000/randomcompany',timeout= None)
    b_soup = BeautifulSoup(status_code.content,'html.parser')
    items = b_soup.find_all('li').__str__()
    payload = re.findall(r'[\w\.-]+:\s[\w\s\,.-]+', items)
    len = int(payload.__len__())
#    print(payload)
#    print(len)
    j=0
    k=0
    m=0

    while k<len:
        if (re.search('^Name:', payload[k])):
            a = payload[k].split(':', 1)
            results.append(a[1])

        if (re.search('^CEO:', payload[k])):
            b = payload[k].split(':', 1)
            results.append(b[1])
        if (re.search('^CTO:', payload[k])):
            c = payload[k].split(':', 1)
            results.append(c[1])
        if (re.search('^Round:', payload[k])):
            d = payload[k].split(':', 1)
            results.append(d[1])
        if (re.search('^Purpose:', payload[k])):
            e = payload[k].split(':', 1)
            results.append(e[1])

        k = k + 1
  #      print('K=', k)

    while m>50:
        if(re.search('^Name:',payload[j])):
            a = payload[j].split(':', 1)
            company.append(a[1])
            print('Company=',company)
        if (re.search('^CEO:', payload[j])):
            b = payload[j].split(':', 1)
            ceo.append(b[1])
        if (re.search('^CTO:', payload[j])):
            c = payload[j].split(':', 1)
            cto.append(c[1])
        if (re.search('^Round:', payload[j])):
            d = payload[j].split(':', 1)
            round.append(d[1])
        if (re.search('^Purpose:', payload[j])):
            e = payload[j].split(':', 1)
            purpose.append(e[1])
            print('Purpose=', purpose)
        m=m+1
 #       print ('m=',m)
    #     if payload[0]:
    #         a = payload[0].split(':',1)
    #         company.append(a[1])
    #     if payload[1]:
    #         b = payload[1].split(':',1)
    #         ceo.append(b[1])
    #     if payload[2]:
    #         c  = payload[2].split(':',1)
    #         cto.append(c[1])
    #     if payload[3]:
    #         d = payload[3].split(':',1)
    #         round.append(d[1])
    #     if payload[4]:
    #         e = payload[4].split(':',1)
    #         purpose.append(e[1])
    i = i+1

#    print('I=',i)

print(results)
#myresults = pd.concat([Company_Name,CEO_Name,CTO_Name,Round_No,Purpose_Desc],ignore_index=True,axis=1)
#myresults.to_csv('new.csv')


