#mongodb data export using pymongo MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pymongo import MongoClient
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options = options)
driver.implicitly_wait(2)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
client = MongoClient("mongodb://localhost:27017/")          # connection string you get it from mongo
db = client["add"]
collection = db["Python_Script_Selenium_Project"]
documents = collection.find()
for i in documents:
    user_name = i["username"]
    password = i["password"]
driver.find_element(By.XPATH,"//div/input[@name='username']").send_keys(user_name)
driver.find_element(By.XPATH,"//div/input[@name='password']").send_keys(password)
driver.find_element(By.XPATH,"//div/button[@type='submit']").click()
WebDriverWait(driver,10).until(ec.url_contains('dashboard'))
print(driver.current_url)
time.sleep(5)
driver.quit()