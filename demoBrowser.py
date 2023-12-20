from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chromium import service

# -- Chrome driver
# Service() object is automatically downloading the chromedriver in each execution from selenium class(present in web). This is slow.
# service_obj = Service()
# driver = webdriver.Chrome(service=service_obj)

# Manually added the location of the chromedriver to the Service() object. No need to download again and again. This is fast.
# service_obj = Service("C:/Users/user/PycharmProjects/chromedriver-win64/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)

# service_obj = Service("C:/Users/user/PycharmProjects/geckodriver-v0.33.0-win64/geckodriver.exe")
# driver = webdriver.Firefox(service=service_obj)

service_obj = Service()
driver = webdriver.Firefox(service=service_obj)

driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.close()
