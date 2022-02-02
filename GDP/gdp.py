import csv
import urllib.request as urllib
from bs4 import BeautifulSoup

url='https://www.investopedia.com/insights/worlds-top-economies/'

request=urllib.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'})
page=urllib.urlopen(request)

soup=BeautifulSoup(page,'html.parser')
rows=soup.find('tbody',{'data-check':'-1'}).find_all('tr',recursive=False)[1:]


file=open('top_10_gdp.csv','w',encoding='utf-8',newline='')
writer=csv.writer(file)
writer.writerow(['Country','Nominal GDP','Adjusted GDP','Annual Growth','GDP Per Capita'])


for row in rows:
    all_data=row.find_all('td')
    country=all_data[0].text.strip()
    nominal_gdp=all_data[1].text.strip()
    adjusted_gdp=all_data[2].text.strip()
    annual_growth=all_data[3].text.strip()
    gdp_per_capita=all_data[3].text.strip()

    writer.writerow([country,nominal_gdp,adjusted_gdp,annual_growth,gdp_per_capita])
print("Thank you...")
file.close()