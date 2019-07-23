print('****Getting words from UrbanDictionary****')
from datetime import date, timedelta
import requests
from bs4 import BeautifulSoup as bs
yesterday = date.today() - timedelta(days=1)
url = "https://www.urbandictionary.com/yesterday.php?date="+str(yesterday)
response = requests.get(url)
soup = bs(response.content, 'html.parser')
links = soup.find("ul",class_="no-bullet")
wordLista =""
for words in links.findAll('a'):
    
    wordLista = wordLista + words.string+"\n"
fileWords= open("aggwords.txt","w+")
fileWords.write(wordLista)
fileWords.close()
