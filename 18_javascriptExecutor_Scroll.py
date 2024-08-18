import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

service_obj = Service()
driver = webdriver.Chrome(service=service_obj,options=chrome_options)

driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.get_screenshot_as_file("landingPage.png")

driver.execute_script("window.scrollBy(0,500);")
driver.get_screenshot_as_file("scrollDown500px.png")

driver.execute_script("scrollBy(0,-500);")
driver.get_screenshot_as_file("scrollUp500px.png")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.get_screenshot_as_file("scrollBottom.png")

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
driver.get_screenshot_as_file("scrollTop.png")

driver.close()