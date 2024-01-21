from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# directly clicking on a specific radio button
# driver.find_element(By.CSS_SELECTOR,"input[value=radio1]").click()

radiobuttons = driver.find_elements(By.CSS_SELECTOR,"input[type=radio]")

for radiobutton in radiobuttons:
    print(radiobutton.get_attribute("value"))
    if radiobutton.get_attribute("value") == "radio2":
        radiobutton.click()
        assert radiobutton.is_selected()
        print("radio button 2 is selected")
        break
