from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Code will execute without opening the browser on passing the argument "headless"
chrome_options.add_argument("headless")

service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

browserSortedVeglist = []
originalBrowserSortedVeglist = []

driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# veg = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]").text
# print(veg)
#
# i = 1
# while i < 6:
#     veg = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[i]/td[1]").text
#     print(veg)
#     i += 1

#  Manually sort the table in the browser by clicking on column header
driver.find_element(By.XPATH,"//tr/th[1]").click()

# Collect the browser sorted veg names in originalBrowserSortedVeglist
vegWebElements = driver.find_elements(By.XPATH,"//tr/td[1]")

for sortedVeg in vegWebElements:
    browserSortedVeglist.append(sortedVeg.text)

originalBrowserSortedVeglist = browserSortedVeglist
print("originalBrowserSortedVeglist : \n",originalBrowserSortedVeglist)

# Sort the browserSortedVeglist
browserSortedVeglist.sort()
print("browserSortedVeglist : \n",browserSortedVeglist)

# Compare originalBrowserSortedVeglist with browserSortedVeglist
assert originalBrowserSortedVeglist==browserSortedVeglist

driver.close()

