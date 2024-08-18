from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

service_obj = Service()
driver = webdriver.Chrome(service=service_obj,options=options)

driver.get("https://trailhead.salesforce.com/")

actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.LINK_TEXT,"Login"))