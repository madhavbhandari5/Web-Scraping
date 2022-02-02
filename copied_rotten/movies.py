from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH=Service('C:\Program Files (x86)\chromedriver.exe')
driver=webdriver.Chrome(service=PATH)
driver.get('https://editorial.rottentomatoes.com/guide/2021-fall-tv-survey-30-top-tv-streaming-movies')


try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "articleContentBody"))
    )
    movies=main.find_elements(By.CLASS_NAME,"countdown-item")
    for movie in movies:
        sn=movie.find_element(By.CLASS_NAME,'countdown-index')
        moviename=movie.find_element(By.CLASS_NAME,'article_movie_title').find_element(By.TAG_NAME,'a')
        cast=movie.find_elements(By.CLASS_NAME,'col-sm-24')
        print(cast.text)

except:
    driver.quit()



driver.quit()