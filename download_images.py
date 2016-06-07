import requests
import time
import urllib
import argparse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from multiprocessing import Pool
from lxml.html import fromstring
import os, sys

def search(url):
    # Create a browser
    browser = webdriver.Chrome()

    # Open the link
    browser.get(url)
    time.sleep(1)

    element = browser.find_element_by_tag_name("body")

    # Scroll down
    for i in range(30):
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)

    browser.find_element_by_id("smb").click()

    for i in range(50):
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)

    time.sleep(1)

    # Get page source and close the browser
    source = browser.page_source
    browser.close()

    return source

def download_image(link):
    # Use a random user agent header
    headers = {"User-Agent": ua.random}

    # Get the image link
    try:
        r = requests.get("https://www.google.com" + link.get("href"), headers=headers)
    except:
        print("Cannot get link.")
    title = str(fromstring(r.content).findtext(".//title"))
    link = title.split(" ")[-1]

    # Download the image
    print("Downloading from " + link)
    try:
        urllib.request.urlretrieve(link, "images/" + link.split("/")[-1])
    except:
        pass

if __name__ == "__main__":
    # parse command line options
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", help="the keyword to search")
    args = parser.parse_args()

    # set stack limit
    sys.setrecursionlimit(1000000)

    # get user input and search on google
    query = args.keyword
    url = "https://www.google.com/search?as_st=y&tbm=isch&as_q=" + query + \
          "&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=&safe=images&tbs=isz:lt,islt:svga,itp:photo,ift:jpg"
    source = search(url)

    # Parse the page source and download pics
    soup = BeautifulSoup(str(source), "html.parser")
    ua = UserAgent()

    # check directory and create if necessary
    if not os.path.isdir("images"):
        os.makedirs("images")

    # get the links
    links = soup.find_all("a", class_="rg_l")

    # open some processes to download
    with Pool() as pool:
        pool.map(download_image, links)
