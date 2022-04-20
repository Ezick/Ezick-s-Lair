#  Запуск всех тестов из этой категории осуществляется по команде:
#  pytest -v --driver Chrome --driver-path /Driver/chromedriver.exe Tests/test_mainPage.py

import time
from Pages.mainPage import MainPage
from config import TestData


def test_delivery_button_is_visible(web_browser):
    """ В шапке сайта отображается кнопка Доставка.
    """

    page = MainPage(web_browser)

    page.DELIVERY.is_visible()

    assert True


def test_delivery_button_opens_correct_page(web_browser):
    """ Нажатие кнопки Доставка ведёт на соответствующую страницу.
    """

    page = MainPage(web_browser)

    page.DELIVERY.click()

    assert page.get_current_url() == TestData.MAIN_URL + 'support/dostavka.php'


def test_return_button_is_visible(web_browser):
    """ В шапке сайта отображается кнопка Возврат.
    """

    page = MainPage(web_browser)

    page.RETURN.is_visible()

    assert True


def test_return_button_opens_correct_page(web_browser):
    """ Нажатие кнопки Возврат ведёт на соответствующую страницу.
    """

    page = MainPage(web_browser)

    page.RETURN.click()

    assert page.get_current_url() == TestData.MAIN_URL + 'support/vozvrat.php'


def test_contacts_button_is_visible(web_browser):
    """ В шапке сайта отображается кнопка Контакты.
    """

    page = MainPage(web_browser)

    page.CONTACTS.is_visible()

    assert True


def test_contacts_button_opens_correct_page(web_browser):
    """ Нажатие кнопки Контакты ведёт на соответствующую страницу.
    """

    page = MainPage(web_browser)

    page.CONTACTS.click()

    assert page.get_current_url() == TestData.MAIN_URL + 'services/kontakty.php'


def test_vkontakte_button_is_clickable(web_browser):
    """ Проверка кликабельности иконки ВК.
    """

    page = MainPage(web_browser)

    page.VK_LINK.is_clickable()

    assert True


def test_vkontakte_button_has_correct_link_address(web_browser):
    """ Иконка соцсети ВК содержит корректную ссылку на соответствующий ресурс.
    """

    page = MainPage(web_browser)

    vk_url = page.VK_LINK.get_attribute('href')

    assert vk_url == 'https://vk.com/tramontana'


def test_twitter_button_is_clickable(web_browser):
    """ Проверка кликабельности иконки Твиттера.
    """

    page = MainPage(web_browser)

    page.TWITTER_LINK.is_clickable()

    assert True


def test_twitter_button_has_correct_link_address(web_browser):
    """ Иконка соцсети Твиттер содержит корректную ссылку на соответствующий ресурс.
    """

    page = MainPage(web_browser)

    twitter_url = page.TWITTER_LINK.get_attribute('href')

    assert twitter_url == 'https://twitter.com/TramontanaShop'


def test_youtube_button_is_clickable(web_browser):
    """ Проверка кликабельности иконки Ютуба.
    """

    page = MainPage(web_browser)

    page.YOUTUBE_LINK.is_clickable()

    assert True


def test_youtube_button_has_correct_link_address(web_browser):
    """ Иконка Ютуба содержит корректную ссылку на соответствующий ресурс.
    """

    page = MainPage(web_browser)

    youtube_url = page.YOUTUBE_LINK.get_attribute('href')

    assert youtube_url == 'https://www.youtube.com/user/TramontanaRU'


def test_telegram_button_is_clickable(web_browser):
    """ Проверка кликабельности иконки Телеграма.
    """

    page = MainPage(web_browser)

    page.TELEGRAM_LINK.is_clickable()

    assert True


def test_telegram_button_has_correct_link_address(web_browser):
    """ Иконка Телеграма содержит корректную ссылку на соответствующий ресурс.
    """

    page = MainPage(web_browser)

    telegram_url = page.TELEGRAM_LINK.get_attribute('href')

    assert telegram_url == 'https://t.me/tramontana_shop'


def test_search_field_is_clickable(web_browser):
    """ Проверка кликабельности поля ввода текста в шапке сайта.
    """

    page = MainPage(web_browser)

    page.SEARCH_TEXTBOX.is_clickable()

    assert True


def test_check_wrong_search_input(web_browser):
    """ Негативный тест: Появление соответствующего сообщения при неудачном поиске.
    """

    page = MainPage(web_browser)

    page.SEARCH_TEXTBOX.send_keys(TestData.SEARCH_INPUT)
    time.sleep(1)
    page.SEARCH_NOTHING_MESSAGE.is_visible()

    assert True


def test_check_carousel_right_button(web_browser):
    """ Проверка кликабельности кнопки прокрутки карусели вперёд.
    """

    page = MainPage(web_browser)

    page.CAROUSEL_RIGHT.is_clickable()

    assert True


def test_check_carousel_left_button(web_browser):
    """ Проверка кликабельности кнопки прокрутки карусели назад.
    """

    page = MainPage(web_browser)

    page.CAROUSEL_LEFT.is_clickable()

    assert True


def test_check_opt_button(web_browser):
    """ В шапке сайта отображается кнопка Опт.
    """

    page = MainPage(web_browser)

    page.OPT_MENU.is_visible()

    assert True


def test_climbing_center_button_opens_correct_page(web_browser):
    """ Нажатие кнопки Скалодром ведёт на соответствующую страницу.
    """

    page = MainPage(web_browser)

    page.SKALODROM.click()

    assert page.get_current_url() == 'https://climbingcenter.ru/'


def test_check_header_logo(web_browser):
    """ Нажатие на лого Tramontana ведёт на стартовую страницу.
    """

    page = MainPage(web_browser)

    page.CONTACTS.click()
    page.TRAMONTANA_LOGO.click()

    assert page.get_current_url() == TestData.MAIN_URL


def test_cart_button_is_visible(web_browser):
    """ В шапке сайта отображается кнопка Корзина.
    """

    page = MainPage(web_browser)

    page.CART.is_visible()

    assert True


def test_cart_button_opens_correct_page(web_browser):
    """ Нажатие кнопки Корзина ведёт на соответствующую страницу.
    """

    page = MainPage(web_browser)

    page.CART.click()

    assert page.get_current_url() == TestData.MAIN_URL + 'personal/basket/'


def test_dark_theme(web_browser):
    """ Нажатие кнопки Темная сторона изменяет фон сайта со светлого на тёмный.
    """

    page = MainPage(web_browser)

    page.DARK_THEME.click()
    time.sleep(0.4)
    page.screenshot('Tests/Screenshots/test-dark-theme.png')


def test_user_can_send_opt_request(web_browser):
    """ При заполнении всех обязательных полей и отправке запроса в меню Опт
        появляется сообщение с подтверждением заявки.
    """

    page = MainPage(web_browser)

    page.OPT_MENU.click()
    page.wait_page_loaded()
    page.scroll_down(360)
    page.OPT_NAME_TEXTBOX.send_keys('Test')
    page.OPT_EMAIL_TEXTBOX.send_keys('test@test.de')
    page.OPT_PHONE_TEXTBOX.send_keys('88005553535')
    page.OPT_SUBMIT_BTN.click()
    time.sleep(2)
    page.OPT_SUCCESSFUL_MESSAGE.is_visible()

    assert True
