from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

service_obj=Service()
driver = webdriver.Chrome(service=service_obj, options=options)

# driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.NAME,"enter-name").send_keys("Sumit")
driver.find_element(By.ID,"alertbtn").click()

alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert "Sumit" in alertText
sleep(5)
alert.accept()