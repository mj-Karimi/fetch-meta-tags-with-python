How can you use this file?
1- Setup python
2- Make a file and copy & paste this code (fetch.py)
3- make a list of urls and save at input.txt (beside your file)
4- Choose meta tag or main tag such as <article> or <title>
5- Run the file.
Note: you can fetch <div>, <span>, <p>, <li> and ... tag with specific class with this code:
story = soup.find('div', {'class': 'story'}).text if soup.find('div', {'class': 'story'}) else 'N/A'
