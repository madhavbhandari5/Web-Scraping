import csv
from re import L
import urllib.request as urllib
from bs4 import BeautifulSoup
url='http://www.nepalstock.com/annualtrading/annual'
request=urllib.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'})
page=urllib.urlopen(request)

soup=BeautifulSoup(page,'html.parser')
#rows=soup.find('table',attrs={'class':'table table-hover table-condensed'}).find_all('tr',recursive=False)[3:]
file=open('nepsedatascraping.csv','w',encoding='utf-8',newline='')
main_table=soup.find('div',{'class':'col-md-9'})
data_table=main_table.find_all('tr')[2:]
#table=soup.find_all('table')
writer=csv.writer(file)
#print(main_table)
#print(data_table)
#print(table)
writer.writerow(['S.N','Company','High','Low','Average','Closing','Trade Volume','Share Volume'])
for row in data_table:
    sn=row.find('td').text.strip()
    script_name=row.find('td',{'data-toggle':'tooltip'}).text.strip()
    numbers=row.find_all('td',{'align':'right'})
    High=numbers[0].text.strip()
    Low=numbers[1].text.strip()
    Average=numbers[2].text.strip()
    Closing=numbers[3].text.strip()
    Trade_Volume=numbers[4].text.strip()
    Share_Volume=numbers[5].text.strip()
    writer.writerow([sn,script_name,High,Low,Average,Closing,Trade_Volume,Share_Volume])
    
print('Thank you...')
file.close()

