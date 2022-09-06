import configparser

from pages.page_phone_recharge import PhoneRecharge

config = configparser.ConfigParser()
config.read('config.ini')

operator = config.get("USER_DATA", "operator")
phone_number = config.get("USER_DATA", "phone")

class TestMobileRecharge:

    def test_recharge_mobile_phone(self,browser_type):
        self.driver = browser_type
        phone_recharge = PhoneRecharge(self.driver)
        phone_recharge.open_operator_input()
        phone_recharge.select_operator(operator)
