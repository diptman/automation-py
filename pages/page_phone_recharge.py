from selenium.webdriver.common.by import By


class PhoneRecharge:
    # locators
    _name_mobile_number_input = "mobile"
    _name_operator_input = "operator"
    _css_operator_name_dropdown = "li[data-show='{}']"
    _name_amount_input = "amount"
    _xpath_recharge_amount_value ="(//*[@class='main-info data-value']/b[text() ='{}'])[1]"

    # functions
    def __init__(self, driver):
        self.driver = driver

    def select_operator(self, operator_name):
        self.driver.find_element(By.CSS_SELECTOR, self._css_operator_name_dropdown.format(operator_name)).click()

    def open_operator_input(self):
        self.driver.find_element(By.NAME,self._name_operator_input).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(By.NAME, self._name_mobile_number_input).send_keys(phone_number)

    def enter_the_recharge_amount(self, amount):
        self.driver.find_element(By.NAME, self._name_amount_input).click()
        self.driver.find_element(By.XPATH, self._xpath_recharge_amount_value.format(amount)).click()