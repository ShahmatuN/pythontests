from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def test_add_product_to_cart():
    driver = webdriver.Chrome()
    driver.get("http://www.vseinstrumenti.ru/")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-qa="cart"]')))
    driver.find_element(By.CSS_SELECTOR,'[data-qa="cart"]').click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-qa="checkout-total"]')))
    driver.quit()

