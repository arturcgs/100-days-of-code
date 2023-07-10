from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time


def click_for_five_seconds(clickable_object: WebElement):
    """
    :param clickable_object: WebElement
    :return: None

    Clicks a clickable_object for 5 seconds
    """

    before_time = time.perf_counter()

    while True:
        clickable_object.click()

        after_time = time.perf_counter()

        if (after_time - before_time) >= 5:
            return


def get_current_money():
    """
    :return: int
    Returns the current amount of cookies
    """
    return int(money.text.replace(",", ""))


def get_upgrade_price(upgrade: WebElement):
    """
    :param upgrade: WebElement
    :return: int
    Returns the current price for the given upgrade
    """
    text_with_price = driver.find_element(By.CSS_SELECTOR, f"#{upgrade.get_attribute('id')} b").text
    for element in text_with_price.replace(",", "").split():
        if element.isdigit():
            return int(element)


def check_and_buy_upgrades():
    """
    :return: None
    Checks all upgrades, from most expansive to least expansive, and buys as much as possible from the most
    expansive available upgrade
    """
    for upgrade in upgrades:
        if not upgrade.get_attribute("class"):  # check if available
            while True:
                current_money = get_current_money()
                upgrade_price = get_upgrade_price(upgrade)

                print(f"cur {current_money} up {upgrade_price} if {current_money >= upgrade_price}")

                if current_money >= upgrade_price:  # buy upgrade
                    try:
                        upgrade.click()
                    except:
                        continue

                else:  # break loop
                    break


# selenium setup
URL = "https://orteil.dashnet.org/experiments/cookie/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(URL)

# selecting important game pieces
cookie = driver.find_element(By.ID, "cookie")
money = driver.find_element(By.ID, "money")


buy_cursor = driver.find_element(By.ID, "buyCursor")
buy_grandma = driver.find_element(By.ID, "buyGrandma")
buy_factory = driver.find_element(By.ID, "buyFactory")
buy_mine = driver.find_element(By.ID, "buyMine")
buy_shipment = driver.find_element(By.ID, "buyShipment")
buy_alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab")
buy_portal = driver.find_element(By.ID, "buyPortal")
buy_time_machine = driver.find_element(By.ID, "buyTime machine")
buy_elder_pledge = driver.find_element(By.ID, "buyElder Pledge")

upgrades = [
    buy_elder_pledge,
    buy_time_machine,
    buy_portal,
    buy_alchemy_lab,
    buy_shipment,
    buy_mine,
    buy_factory,
    buy_grandma,
    buy_cursor,
]

while True:
    click_for_five_seconds(cookie)
    check_and_buy_upgrades()




