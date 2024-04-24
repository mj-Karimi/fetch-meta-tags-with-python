import requests
from bs4 import BeautifulSoup

# read a list of website address + support Persian, Arabic and other utf8 languages:
with open('input.txt', 'r', encoding='utf-8') as file:
    urls = file.readlines()

# Make a file for export data:
with open('results.csv', 'w', encoding='utf-8') as file:
    file.write('num,title,h1,img,webfilter,address,spanna,email\n')

    headers = {
    'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/118.0.5993.70 Safari/537.36'  # Set the user agent
}

    request_interval = 1  # Requests per second
    for url in urls:
        url = url.strip() 
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # read meta[@property='og:img'] <-- you can replace it with any tag, like meta[@property='og:description'] or meta[@property='og:title']
        meta_img = soup.find('meta', {'property': 'og:image'})
        img_content = meta_img['content'] if meta_img else 'N/A'

        # read <title> tag:   story = soup.find('div', {'class': 'story'}).text if soup.find('div', {'class': 'story'}) else 'N/A' 
        title = soup.find('title').text if soup.find('title') else 'N/A'

        img = soup.findAll('img', {'class': 'shop-logo'})    
        src = [img['src'] for img in img]

        h1 = soup.find('h1').text if soup.find('h1') else 'N/A'


        webfilter = soup.find('a', {'id': 'webfilter'}).text if soup.find('span') else 'N/A'

        address = soup.find('span', {'id': 'address'}).text if soup.find('span') else 'N/A'
        spanna = soup.find('span', {'id': 'masol'}).text if soup.find('span') else 'N/A'
        email = soup.find('span', {'id': 'masol'}).text if soup.find('span') else 'N/A'


        # save at file:
        file.write(f'"1","{title}","{h1}","{src}","{webfilter}","{address}","{spanna}","{email}"\n')
