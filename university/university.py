import csv
import urllib.request as urllib
from bs4 import BeautifulSoup
url='https://www.topuniversities.com/where-to-study/north-america/united-states/ranked-top-100-us-universities'
request=urllib.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'})
page=urllib.urlopen(request)

soup=BeautifulSoup(page,'html.parser')
rows=soup.find('tbody').find_all('tr',recursive=False)[2:]


file=open('topuniversityname.csv','w',encoding='utf-8',newline='')
writer=csv.writer(file)
writer.writerow(['SN.','University Name'])


for row in rows:
    sn=row.find('td',attrs={'style':'width: 74px;'}).text.strip()
    uniname=row.find('td',attrs={'style':'width: 413px;'}).text.strip()


    writer.writerow([sn,uniname])

print('Thank you...')
file.close()