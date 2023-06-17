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

driver.get("https://www.kayak.com/")

with open('fullLocation.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    time.sleep(0.3)
    # elements = driver.find_elements_by_class_name("P_Ok-sublink-link")
    elements = driver.find_elements(By.CLASS_NAME, "P_Ok-sublink-link")
    for c in range(0, len(elements)):
        link = elements[c].get_attribute('href')
        print("link: " + link)
        writer.writerow([link])
driver.close()    
