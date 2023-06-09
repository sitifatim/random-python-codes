# -*- coding: utf-8 -*-
"""news-scrapping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S_r8nB8ulPgxPpOkag6QsdMrnrbh1iOG
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
pd.set_option('display.max_colwidth',None)

# detik-hukum
# automation for some page index

all_text = []
page_limit = 5

for i in range(10,15):
    url= f"https://news.detik.com/hukum/indeks?date=05%2F{i}%2F2023" # get the main link
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    #find all the box news
    html = soup.find_all('article', 'list-content__item') # insspect the news box (the bigger one)

    for article in html:
        news_link = article.find('a')['href']  # get the link to the news article
        article_response = requests.get(news_link)
        article_soup = BeautifulSoup(article_response.text, "html.parser")

        #find the text content of the news article
        article_text = [j.get_text() for j in article_soup.find_all('p')]

        all_text.append(article_text)

pd.DataFrame({'text': all_text})

# check one page only
url = 'https://news.detik.com/hukum/indeks?date=05%2F20%2F2023'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

html = soup.find_all('article', 'list-content__item')
all_text = []
for article in html:
        news_link = article.find('a')['href']  # Get the link to the news article
        article_response = requests.get(news_link)
        article_soup = BeautifulSoup(article_response.text, "html.parser")

        # Find the text content of the news article
        article_text = [j.get_text() for j in article_soup.find_all('p')]
        all_text.append(article_text)
        print(article_text)

pd.DataFrame({'data': all_text})