from selenium.webdriver.common.by import By


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")