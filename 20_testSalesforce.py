from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

service = Service()
driver = webdriver.Chrome(service=service,options=chrome_options)

# Dummy login to test.salesforce.com

driver.get("https://test.salesforce.com/")

driver.find_element(By.ID,"username").send_keys("test@mail.com")
driver.find_element(By.NAME,"pw").send_keys("testpass")
driver.find_element(By.NAME,"Login").click()