#import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

#PATH = "C:\Program Files (x86)\chromedriver.exe"
#driver = webdriver.Chrome(PATH)

#driver.get("https://www.amazon.co.uk/Eye-Caring-Charging-Dimmable-Bedside-Brightness/dp/B09JF3GVN7/ref=sr_1_5?crid=3K9B2Z8M6Q7NP&keywords=lamp&qid=1665521494&qu=eyJxc2MiOiI4LjMxIiwicXNhIjoiNy41OCIsInFzcCI6IjcuMDcifQ%3D%3D&sprefix=lamp%2Caps%2C50&sr=8-5")
print ("Test123")