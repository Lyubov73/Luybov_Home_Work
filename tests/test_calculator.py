import time
from selenium import webdriver
from pages.calculator_page import CalculatorPage

def test_calculator_addition():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    calc = CalculatorPage(driver)
    calc.set_delay(45)
    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")

    time.sleep(45)  # ожидание результата
    assert calc.get_result() == "15"

    driver.quit()
