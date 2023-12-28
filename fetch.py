import requests
from bs4 import BeautifulSoup

# read a list of website address + support Persian, Arabic and other utf8 languages:
with open('input.txt', 'r', encoding='utf-8') as file:
    urls = file.readlines()

# Make a file for export data:
with open('results.csv', 'w', encoding='utf-8') as file:
    file.write('img,title,article\n')

    
    for url in urls:
        url = url.strip() 
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # read meta[@property='og:img'] <-- you can replace it with any tag, like meta[@property='og:description'] or meta[@property='og:title']
        meta_img = soup.find('meta', {'property': 'og:image'})
        img_content = meta_img['content'] if meta_img else 'N/A'

        # read <title> tag:
        title = soup.find('title').text if soup.find('title') else 'N/A'
        article = soup.find('article').text if soup.find('article') else 'N/A'
        
        # save at file:
        file.write(f'"{img_content}","{title}","{article}"\n')
