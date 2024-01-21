import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj=Service()
driver = webdriver.Chrome(service=service_obj,options=options)

# Implicit Wait - Global timeout.
# 5 secs - Max timeout. If element is identified in 2 secs, wait ends and execution resumes. Hence, 3 secs saved
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver.maximize_window()
driver.find_element(By.CLASS_NAME,"search-keyword").send_keys("ber")

# Implicit wait will NOT work here as the search text will immediately return an empty list, which is still valid.
# Hence, time.sleep() is used so that the actual search results are loaded and stored in the list "products".
time.sleep(2)

products = driver.find_elements(By.XPATH,"//div[@class='products']/div")

print("Total products found = ",len(products))

for product in products:
    # print(product.text)
    product.find_element(By.XPATH, "div/button").click()

# driver.find_element(By.XPATH,"//a[@class='cart-icon']/img").click()    //Both this and the next commands are valid. Either of them can be used
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()

driver.find_element(By.XPATH,"//div[@class='cart-preview active']/div[2]/button").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

