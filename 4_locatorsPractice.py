from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj=Service("C:/Users/user/PycharmProjects/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=options)
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Practice").click()
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Sumit Ranjan Kar")
driver.find_element(By.CSS_SELECTOR,"#email").send_keys("sumit38494@gmail.com")
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
driver.find_element(By.XPATH,"//input[@id='name']").clear()
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Sumit Kar")
driver.find_element(By.CSS_SELECTOR,"#email").send_keys("sumitrkar@gmail.com")
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
#driver.close()
# driver.find_element(By.NAME, "email").send_keys("xyz.com")
# driver.find_element(By.NAME, "current-password").send_keys("123456")
#
# driver.find_element(By.XPATH,"//button[@class='Button_button__URNp+ Button_primary__d2Jt3 Button_fullwidth__0HLEu']").click()
