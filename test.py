import requests
from bs4 import BeautifulSoup

req = requests.get("https://apps.maynoothuniversity.ie/timetable/?")

soup = BeautifulSoup(req.content, "html.parser")
#quotes = soup.find_all('div', {'class': 'table_listing'})
#res = soup.title
for i in soup.findAll("table",{"class": "table_listing"}):
    print((i.find("table", {"class": "table_listing"})).text)
#print(quotes.get_text())
#print(soup.prettify())