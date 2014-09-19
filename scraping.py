from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()

driver.get("https://ww2.aauw.org/branch_locator/index.php")
elem = driver.find_element_by_id("submit_state")
elem.click()
dbElement = WebDriverWait(driver, 20).until(lambda x : x.find_element_by_class_name("state_search_even"))

clicker = driver.find_element_by_xpath('//div[@class="state_search_even"]')
links = clicker.find_elements_by_xpath('//div[@class="branch_name"]')
for link in links:
    #ensure all elements are visited
    print link.text
    link.click()
    #after clicking then look at the map
    try:
        WebDriverWait(driver,20).until(lambda x: x.find_element_by_class_name("branch_detail_map"))
        load_map = link.find_element_by_xpath('//span[@class="branch_detail_map"]')
        load_map.click()
        WebDriverWait(driver,20).until(lambda x: x.find_element_by_id("map-container"))
        desired_map = driver.find_element_by_id("map-container")
        #this is the map we want, do whatever with the data from here
    except:
        continue
driver.close()
