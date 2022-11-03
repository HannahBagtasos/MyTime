#import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.get("https://www.google.com")

#PATH = "C:\Program Files (x86)\chromedriver.exe"
#driver = webdriver.Chrome(PATH)

#driver.get("https://apps.maynoothuniversity.ie/timetable/?")
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product




