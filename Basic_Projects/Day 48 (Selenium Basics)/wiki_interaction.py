from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# selenium setup
URL = "https://en.wikipedia.org/wiki/Main_Page"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(URL)

#search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'search')))
driver.find_element(By.XPATH, '//*[@id="p-search"]/a/span[1]').click()
search = driver.find_element(By.XPATH, '//*[@id="searchInput"]')

search.send_keys("python")
search.send_keys(Keys.ENTER)

time.sleep(2)
