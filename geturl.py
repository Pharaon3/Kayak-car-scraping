import csv
import threading

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
import pandas as pd
import time
import re
import csv
from datetime import datetime
from datetime import date

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)

searchBtn = 'Iqt3-mod-stretch'

id = 0
with open('links43.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    with open('43.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(id)
            id = id + 1
            driver.get(row[0])
            time.sleep(0.3)
            eles = driver.find_elements(By.CLASS_NAME, searchBtn)
            for ele in eles:
                if ele.text == "Search":
                    ele.click()
                    new_tab_url = driver.current_url
                    print(new_tab_url)
                    writer.writerow([new_tab_url])
                    break
driver.close()
