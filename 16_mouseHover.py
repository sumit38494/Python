import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

service_obj = Service()
driver = webdriver.Chrome(service=service_obj,options=options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()

# driver.execute_script("window.scrollTo(5,1080)")

dropdown= Select(driver.find_element(By.ID,"dropdown-class-example"))
dropdown.select_by_value("option2")
time.sleep(2)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
# action.move_to_element(driver.find_element(By.LINK_TEXT,"Top")).click().perform()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Reload").click()
driver.maximize_window()
