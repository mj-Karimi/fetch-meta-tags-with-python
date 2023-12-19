<h2>How can you use this file?</h2>
<p>1- Setup python</p>
<p>2- Make a file and copy & paste this code (fetch.py)</p>
<p>3- make a list of urls and save at input.txt (beside your file)</p>
<p>4- Choose meta tag or main tag such as <article> or <title></p>
<p>5- Run the file.</p>
<h3>Note:</h3> you can fetch div, span, p, li and ... tag with specific class with this code:
<code> story = soup.find('div', {'class': 'story'}).text if soup.find('div', {'class': 'story'}) else 'N/A' </code>
