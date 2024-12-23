from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
driver = webdriver.Chrome()
def GetData(links):
    #for index, url in enumerate(links):
    #    print(f"Video {index}")

    #UserName
    className = "tiktok-41hm0z"
    descript=BeautifulSoup(driver.page_source, "html.parser")
    findas = descript.find_all("img", {"class":className})
    soup = descript.img["alt"]

    print(findas)
    print("////////////////////////////////////////////////////")
    print(soup) 

def GetLinksTiktoksFromCollection(link_cole):
    print("1: Opening Page...")
    driver = webdriver.Chrome()

    # Change the tiktok link
    driver.get(link_cole)
    # IF YOU GET A TIKTOK CAPTCHA, CHANGE THE TIMEOUT HERE
    # to 60 seconds, just enough time for you to complete the captcha yourself.
    time.sleep(1)

    scroll_pause_time = 1
    screen_height = driver.execute_script("return window.screen.height;")
    i = 1

    print("2: Scrolling page...")
    while True:
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
        i += 1
        time.sleep(scroll_pause_time)
        scroll_height = driver.execute_script("return document.body.scrollHeight;")  
        if (screen_height) * i > scroll_height:
            break 

    # this class may change, so make sure to inspect the page and find the correct class
    #LINK
    print("3: getting link of videos...")
    className = "tiktok-c83ctf-DivWrapper"
    script  = "let l = [];"
    script += "document.getElementsByClassName(\""
    script += className
    script += "\").forEach(item => { l.push(item.querySelector('a').href)});"
    script += "return l;"
    urlsToDownload = driver.execute_script(script)
    print(f"Found {len(urlsToDownload)} videos")
    return urlsToDownload