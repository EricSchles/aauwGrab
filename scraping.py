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

links = driver.find_element_by_xpath('//div[@class="state_search_even"]//div[@class="branch_name"]')
links.click()
driver.close()
