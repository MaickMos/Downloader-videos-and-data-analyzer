import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def ScrollPage(scroll_pause_time):
    #get the screen_height tes 
    screen_height = driver.execute_script("return window.screen.height;")
    i = 1
    print("Scrolling page...")
    while True:
        #execute the scroll the size of the screen until arrive to end
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
        i += 1
        time.sleep(scroll_pause_time)
        scroll_height = driver.execute_script("return document.body.scrollHeight;")  
        if (screen_height) * i > scroll_height:
            break

def Click(class_element):
    try:
        print("Doing Click in button collection")
        element = driver.find_element(By.CSS_SELECTOR, class_element)
        print("Waiting that existed the element")
        WebDriverWait(driver,10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR,class_element))
        )
        element.click()
        print("click")
        
    except Exception as error:
        print(f"Error en: {error}")

def Getlinkstiktoksfrompage(className):
    print("Getting links of videos...")
    script  = "let l = []; "
    script += "Array.from(document.getElementsByClassName(\"" +className + "\")).forEach(item => { "
    script += "    let link = item.querySelector('a'); "
    script += "    if (link) { l.push(link.href); } "
    script += "}); "
    script += "return l;"

    wait = WebDriverWait(driver, 10)  # Espera hasta 10 segundos
    if className[0] == ".":
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,className.replace(" ","."))))
    else:
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "."+className.replace(" ","."))))
    
    urlsToDownload = driver.execute_script(script)
    print(f"Found {len(urlsToDownload)} videos")
    return urlsToDownload

link_home_page_tiktok = "https://www.tiktok.com/@maickmos"
class_button_favorite = "css-1wncxfu-PFavorite e1jjp0pq3"
class_collection = "css-13fa1gi-DivWrapper e1cg0wnj1"
class_tiktok_video = "css-8dx572-DivContainer-StyledDivContainerV2 eq741c50"

#driver = webdriver.Chrome()
#Open the page in a chrome already open
#First is necessary open chrome from the terminal: r"
#Put the port 9222 and indicate that the user c:selenium will be the instance going to use
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  # Connect to depurate's port

#open the driver that is already open
driver = webdriver.Chrome(options=chrome_options)
#Go to the page of the user
driver.get(link_home_page_tiktok)
#click in the button of favorite videos
Click("."+class_button_favorite.replace(" ","."))
#get the list of the links of the collections
collections = Getlinkstiktoksfrompage(class_collection)
print(collections)
#save in the database

#links = Getlinkstiktoksfrompage(class_tiktok_video)
#print(links)

print("Esperando para cerrar...")
time.sleep(60)