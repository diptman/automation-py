from selenium.webdriver.common.by import By


class PhoneRecharge:
    # locators
    _name_mobile_number_input = "mobile"
    _name_operator_input = "operator"
    _css_operator_name_dropdown = "li[data-show='{}']"

    # functions

    def __init__(self, driver):
        self.driver = driver

    def select_operator(self, operator_name):
        self.driver.find_element(By.CSS_SELECTOR, self._css_operator_name_dropdown.format(operator_name)).click()

    def open_operator_input(self):
        self.driver.find_element(By.NAME,self._name_operator_input).click();