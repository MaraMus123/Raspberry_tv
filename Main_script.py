import datetime
import selenium
from selenium import webdriver
import pycec
import time
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options

def turn_on_tv():
    try:
        cec = CECAdapter()
        cec.power_on()
        cec.close()
        print("TV turned on successfully")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
def turn_off_tv():
    try:
        cec = CECAdapter()
        cec.standby()
        cec.close()
        print("TV turned off successfully")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def show_page():
    chrome_driver = "C:\\Users\\musin\\IdeaProjects\\Chrome-driver-114\\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver)
    driver.get("https://hockeyslavia.cz/")
    stranka = driver.page_source
    return stranka
def return_source():
    options = Options()
    options.add_experimental_option("--headless")
    chrome_driver = "C:\\Users\\musin\\IdeaProjects\\Chrome-driver-114\\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver,options=options)
    driver.get("https://hockeyslavia.cz/")
    stranka = driver.page_source
    return stranka

stranka_check = None
while True:
    current_time = datetime.datetime.now()
    current_date = datetime.date.today()
    starter_time = datetime.time(10,00,00)
    starter = datetime.datetime.combine(current_date,starter_time)
    ender_time = datetime.time(18,00,00)
    ender = datetime.datetime.combine(current_date,ender_time)
    while starter < current_time < ender:
        current_time = datetime.datetime.now()
        turn_on_tv()
        if stranka_check != return_source():
            stranka_check = show_page()
        time.sleep(600)
    turn_off_tv()
    time.sleep(600)



