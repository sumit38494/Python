import time

from Tools.scripts.var_access_benchmark import B
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("headless")

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")
# time.sleep(3)
driver.find_element(By.LINK_TEXT, "Shop").click()
# time.sleep(3)
phoneList = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
print("\nList of Available phones:")

phToBeSelected="Nokia Edge"
i = 1
for phone in phoneList:
    print(phone.find_element(By.CLASS_NAME, "card-title").text)
    if phone.find_element(By.CLASS_NAME, "card-title").text == phToBeSelected:
        driver.find_element(By.XPATH, "//app-card-list/app-card[" + str(i) + "]/div/div/button").click()
        pass
        # phone.find_element(By.XPATH,"//button[@class='btn btn-info']").click()
    i += 1
# time.sleep(3)

print("\nPhone to be selected for purchase:", phToBeSelected)

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
# time.sleep(3)
# driver.find_element(By.CLASS_NAME,'nav-link btn btn-primary').click()
driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
phone = driver.find_element(By.XPATH, "//div/h4/a").text

assert phone == phToBeSelected
print("\nPhone added to cart is:", phone)

driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

driver.find_element(By.ID,"country").send_keys("In")
time.sleep(10)

countries = driver.find_elements(By.XPATH,"//div[@class='suggestions']/ul")
print("Number of countries found:", len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break


# driver.find_element(By.XPATH,"//input[@id='checkbox2']").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@class='btn btn-success btn-lg']").click()
