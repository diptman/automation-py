import configparser
import logging
from pages.page_phone_recharge import PhoneRecharge

config = configparser.ConfigParser()
config.read('config.ini')

operator = config.get("USER_DATA", "operator")
phone_number = config.get("USER_DATA", "phone")
recharge_amount = config.get("USER_DATA", "amount")

class TestMobileRecharge:

    def test_recharge_mobile_phone(self,browser_type):
        self.driver = browser_type
        phone_recharge = PhoneRecharge(self.driver)
        logging.info("# Enter Phone Number")
        phone_recharge.enter_phone_number(phone_number)
        logging.info("# Select the operator from Drop down")
        phone_recharge.open_operator_input()
        phone_recharge.select_operator(operator)
        logging.info("# Select Recharge Amount")
        phone_recharge.enter_the_recharge_amount(recharge_amount)
