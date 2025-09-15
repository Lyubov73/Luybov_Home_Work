from selenium.webdriver.common.by import By

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def set_delay(self, seconds):
        self.driver.find_element(By.ID, "delay").clear()
        self.driver.find_element(By.ID, "delay").send_keys(str(seconds))

    def click_button(self, value):
        self.driver.find_element(By.XPATH, f"//button[text()='{value}']").click()

    def get_result(self):
        return self.driver.find_element(By.ID, "result").text