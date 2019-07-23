import requests
from bs4 import BeautifulSoup as bs
import os
import random
subjectWords = [line.rstrip('\n') for line in open('subjects.txt', 'r')]
print("****Getting images****")
for i in range(len(subjectWords)):
    url = 'https://www.pexels.com/search/'+subjectWords[i]+'/'
    print('Getting images from \n'+url)
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    image_tags = soup.findAll('img')
    if not os.path.exists(subjectWords[i]):
        os.makedirs(subjectWords[i])
    os.chdir(subjectWords[i])
    x = 0
    for image in image_tags:
        try:
            url = image['src']
            response = requests.get(url)
            if response.status_code == 200 and x <= 10:
                with open(subjectWords[i]+'-' + str(x) + '.jpg', 'wb') as f:
                    f.write(requests.get(url).content)
                    f.close()
                    x += 1
                    if (x > 10):
                        break
                    
        
        except:
            pass
    os.chdir('..')




