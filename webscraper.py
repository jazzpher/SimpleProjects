import requests
from bs4 import BeautifulSoup

url = 'https://yourwebsitelink.com'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    article_titles = []
    for title in soup.find_all('h2', class_='article-title'):
        article_titles.append(title.text)
    
    for title in article_titles:
        print(title)
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
