#  Запуск всех тестов из этой категории осуществляется по команде:
#  pytest -v --driver Chrome --driver-path /Driver/chromedriver.exe Tests/test_cartPage.py

from Pages.cartPage import CartPage


def test_check_cart_content(web_browser):
    """ Проверяем соответствие (по названию) лежащего в корзине товара
        товару, который был в неё помещён.
    """

    page = CartPage(web_browser)

    page.ADD_TO_CART_BTN.click()
    page.CART_GOTO_POPUP.click()

    assert page.START_URL_PRODUCTS_NAME.get_text() in page.ITEM_IN_CART_NAME.get_text()


def test_delete_product_from_cart(web_browser):
    """ Кнопка удаления товара из корзины кликабельна.
    """

    page = CartPage(web_browser)

    page.ADD_TO_CART_BTN.click()
    page.CART_GOTO_POPUP.click()
    page.DELETE_ITEM_BTN.is_clickable()

    assert True


def test_in_cart_counter_displayed_correctly(web_browser):
    """ При помещении товара в корзину, счётчик в шапке сайта
        изменяется с 0 на 1.
    """

    page = CartPage(web_browser)

    page.ADD_TO_CART_BTN.click()
    page.CART_CLOSE_POPUP.click()

    assert page.CART_COUNTER.get_text() == '1'


def test_plus_one_item_button(web_browser):
    """ При нажатии на кнопку "+" общая стоимость товара увеличивается.
    """

    page = CartPage(web_browser)

    page.ADD_TO_CART_BTN.click()
    page.CART_GOTO_POPUP.click()
    page.INCREASE_ITEM_QUANTITY.click()
    page.wait_page_loaded()

    assert page.CART_TOTAL_PRICE.get_text() == '680 ₽'


def test_minus_one_item_button(web_browser):
    """ При нажатии на кнопку "-" общая стоимость товара уменьшается.
    """

    page = CartPage(web_browser)

    page.ADD_TO_CART_BTN.click()
    page.CART_GOTO_POPUP.click()
    page.INCREASE_ITEM_QUANTITY.click()
    page.wait_page_loaded()
    page.REDUCE_ITEM_QUANTITY.click()
    page.wait_page_loaded()

    assert page.CART_TOTAL_PRICE.get_text() == '340 ₽'


def test_cart_submit_button_is_clickable(web_browser):
    """ Проверка кликабельности кнопки оформления заказа из корзины.
    """

    page = CartPage(web_browser)

    page.ADD_TO_CART_BTN.click()
    page.CART_GOTO_POPUP.click()
    page.CART_SUBMIT_BTN.is_clickable()

    assert True


def test_cart_price_is_equal_to_product_price(web_browser):
    """ При добавлении товара в корзину общая стоимость товаров в корзине
        соответствует цене продукта.
    """

    page = CartPage(web_browser)

    product_price = page.PRODUCT_PRICE.get_text()
    page.ADD_TO_CART_BTN.click()
    page.CART_GOTO_POPUP.click()
    cart_price = page.CART_TOTAL_PRICE.get_text()

    assert cart_price == product_price
