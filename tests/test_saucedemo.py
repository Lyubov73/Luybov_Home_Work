from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_saucedemo_checkout():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    LoginPage(driver).login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_to_cart("Sauce Labs Backpack")
    inventory.add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory.add_to_cart("Sauce Labs Onesie")
    inventory.go_to_cart()

    CartPage(driver).click_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_form("Ivan", "Ivanov", "123456")
    total = checkout.get_total()

    driver.quit()
    assert total == "Total: $58.29"
