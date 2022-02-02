import csv
import itertools
from platform import release
from reprlib import recursive_repr
import urllib.request as urllib
from bs4 import BeautifulSoup
url='https://editorial.rottentomatoes.com/guide/2021-fall-tv-survey-30-top-tv-streaming-movies/'
request=urllib.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'})
page=urllib.urlopen(request)

soup=BeautifulSoup(page,'html.parser')
rows=soup.find_all('div',{'class':"countdown-item"})

file=open('topmovies_from_rottentomato.csv','w',encoding='utf-8',newline='')
writer=csv.writer(file)
writer.writerow(['SN','Movie Name','Genre','Release date','Lead Actor/Actress'])

for row in rows:
    sn=row.find('div',{'class':"countdown-index-resposive"}).text.strip()
    movie=row.find('div',{'class':"article_movie_title"})
    moviename=movie.find('a').text.strip()
    castdata=row.find('div',{'class':"countdown-item-details"})
    castlist=castdata.find('div',{'class':'col-sm-24'})
    castlead=castlist.find_all('a')
    lead_role=[]
    for p in castlead:
        lead_role.append(p.text)

    if len(castlead)>=1:
        new_link=castlead[0].get('href')
    else:
        new_link='#'


    if new_link=='#':
        genre=[]
        release_date=''


    else:
        new_url=new_link
        new_request=urllib.Request(new_url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'})
        new_page=urllib.urlopen(new_request)

        new_soup=BeautifulSoup(new_page,'html.parser')
        new_rows=new_soup.find('div',{'class':"media-body"}).find('div',{'class':'panel-body'}).find('ul',recursive=False)
        list_data=new_rows.find_all('li')

        label_list=[]
        for k,i in enumerate(list_data):
            compa=i.find('div',{'data-qa':'movie-info-item-label'})
            label_list.append(compa.text.strip())
        if 'Release Date (Streaming):' in label_list:
            my_index=label_list.index('Release Date (Streaming):')
            release_date=list_data[my_index].find('div',{'data-qa':'movie-info-item-value'}).text.strip()
        else:
            release_date=''

        genre_list=[]
        if 'Genre:' in label_list:
            my_genre_index=label_list.index('Genre:')
        else:
            my_ultimate_list=[]

        genre=list_data[my_genre_index].find('div',{'data-qa':'movie-info-item-value'})
        genre_list.append(genre.text.strip())
        final_genre_list=[]
        for i in genre_list:
            final_genre_list.append(i.replace('\n',''))
        finalListofgenre=[x.split(',') for x in final_genre_list]
        my_final=list(itertools.chain.from_iterable(finalListofgenre))
        my_ultimate_list=[x.strip(' ') for x in my_final]


        writer.writerow([sn,moviename,my_ultimate_list,release_date,lead_role[1:]])

print('Thank you...')
file.close()