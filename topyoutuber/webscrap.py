import csv
import urllib.request as urllib
from bs4 import BeautifulSoup
url='https://socialblade.com/youtube/top/50/mostviewed'
request=urllib.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'})
page=urllib.urlopen(request)

soup=BeautifulSoup(page,'html.parser')
rows=soup.find('div',attrs={'style':"float: right; width: 900px;"}).find_all('div',recursive=False)[4:]
file=open('topyoutubers.csv','w',encoding='utf-8')
writer=csv.writer(file)

writer.writerow(['Username','Uploads','Views'])
for row in rows:
    username=row.find('a').text.strip()
    numbers=row.find_all('span',attrs={'style':'color:#555;'})
    uploads=numbers[0].text.strip()
    views=numbers[1].text.strip()

    print(username+' '+uploads+' '+views)
    writer.writerow([username,uploads,views])
file.close()