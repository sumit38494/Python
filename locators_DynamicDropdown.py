import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

service_obj=Service()
driver = webdriver.Chrome(service=service_obj,options=options)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID,'autosuggest').send_keys("in")
time.sleep(2)
# countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
countries = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/a")

print("Total countries found=",len(countries),"\n")

for country in countries:
    print(country.text)
    if country.text=="India":
        country.click()
        print("\nBreaking the loop as the country is found")
        break

print("\nSelected the country from the auto suggestive dropdown")

# below working code is to practice in a real website

# driver.get("https://www.amazon.in/")
#
# driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("Cam")
# time.sleep(2)
# items = driver.find_elements(By.XPATH,"//div[@class='s-suggestion s-suggestion-ellipsis-direction']/span")
#
# print(len(items))
#
# for item in items:
#     print(item.text)
#     if item.text=="era":
#         item.click()
#         break


