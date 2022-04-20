from config import TestData

from Pages.base import WebPage
from Pages.elements import WebElement


class CartPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = TestData.MAIN_URL + 'product/beal_verevka_wall_school_unicore_10_2mm_200m/'
        super().__init__(web_driver, url)

    # CartLocators:
    START_URL_PRODUCTS_NAME = WebElement(xpath='/html/body/main/div/div/div/section/div/h1/text()')
    ADD_TO_CART_BTN = WebElement(xpath='//*[@id="product"]/div[1]/div[2]/div[2]/div[2]/button[1]')
    DELETE_ITEM_BTN = WebElement(xpath='//span[@class="basket-item-actions-remove"]')
    INCREASE_ITEM_QUANTITY = WebElement(xpath='//span[@class="basket-item-amount-btn-plus"]')
    REDUCE_ITEM_QUANTITY = WebElement(xpath='//span[@data-entity="basket-item-quantity-minus"]')
    CART_SUBMIT_BTN = WebElement(xpath='//span[@data-entity="basket-checkout-button"]')
    CART_COUNTER = WebElement(xpath='//*[@id="personal-icons"]/a[4]/div/span')
    CART_CLOSE_POPUP = WebElement(xpath='//*[@id="modal"]/div/div/div[1]/button/i')
    CART_GOTO_POPUP = WebElement(xpath='//*[@id="modal"]/div/div/div[3]/a')
    ITEM_IN_CART_NAME = WebElement(xpath='//span(@data-entity="basket-item-name")')
    CART_TOTAL_PRICE = WebElement(class_name='basket-coupon-block-total-price-current')
    PRODUCT_PRICE = WebElement(id='product-price')