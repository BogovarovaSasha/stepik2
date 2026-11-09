import math

from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


    def get_product_name(self):
        """Возвращает название товара со страницы."""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        """Возвращает цену товара со страницы."""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text


    def should_be_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение о добавлении товара не появилось"

    def should_product_name_match_in_message(self, expected_name):
        message_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert message_name == expected_name, \
            f"Название товара в сообщении ('{message_name}') не совпадает с названием товара ('{expected_name}')"

    def should_basket_total_match_product_price(self, expected_price):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert basket_total == expected_price, \
            f"Стоимость корзины ('{basket_total}') не совпадает с ценой товара ('{expected_price}')"