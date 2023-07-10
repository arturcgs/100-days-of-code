from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# selenium setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org")

event_dates = driver.find_elements(By.CSS_SELECTOR, 'div.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, 'div.event-widget li a')

upcoming_events = {index: {'time': date.text, 'name': name.text}
                   for date, name, index
                   in zip(event_dates, event_names, range(len(event_dates)))}


print(upcoming_events)


