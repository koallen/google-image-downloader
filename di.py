import requests
import time
import urllib
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent

query = input("What to search? ")
url = "https://www.google.com/search?as_st=y&tbm=isch&as_q=" + query + "&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=&safe=images&tbs=isz:lt,islt:svga,itp:photo,ift:jpg"

#
# Get page source from browser
#
browser = webdriver.Chrome()

browser.get(url)
time.sleep(1)

element = browser.find_element_by_tag_name("body")

for i in range(30):
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)

browser.find_element_by_id("smb").click()

for i in range(50):
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)

time.sleep(1)
source = browser.page_source
browser.close()

#
# Parse the page source and download pics
#
soup = BeautifulSoup(str(source), "html.parser")

ua = UserAgent() # set user agent

# get the links
for link in soup.find_all("a", class_="rg_l"):
    headers = {"User-Agent": ua.random}
    try:
        r = requests.get("https://www.google.com" + link.get("href"), headers=headers)
    except:
        print("Cannot get link")
        continue
    soup = BeautifulSoup(str(r.text), "html.parser")
    link = soup.title.string.split(" ")[-1]
    print("Downloading from " + link)
    try:
        urllib.request.urlretrieve(link, "images/" + link.split("/")[-1])
    except:
        print("Images folder not created")

