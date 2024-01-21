from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(service=service_obj,options=options)

driver.get("https://onecognizant.cognizant.com/")
driver.maximize_window()
print(driver.title)
# driver.find_element(By.XPATH,"//div[@class='expandQuickAccessCardIcon collapsedMode']").click()
