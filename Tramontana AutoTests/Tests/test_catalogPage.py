#  Запуск всех тестов из этой категории осуществляется по команде:
#  pytest -v --driver Chrome --driver-path /Driver/chromedriver.exe Tests/test_catalogPage.py

from Pages.catalogPage import CatalogPage
from config import TestData
import time


def test_clothes_button_sends_to_correct_catalog_page(web_browser):
    """ Нажатие кнопки Одежда открывает соответствующее окно каталога.
    """

    page = CatalogPage(web_browser)

    page.ODEZHDA.click()

    assert page.get_current_url() == TestData.MAIN_URL + 'catalog/odezhda_1/'


def test_shoes_button_sends_to_correct_catalog_page(web_browser):
    """ Нажатие кнопки Обувь открывает соответствующее окно каталога.
    """

    page = CatalogPage(web_browser)

    page.OBUV.click()

    assert page.get_current_url() == TestData.MAIN_URL + 'catalog/obuv/'


def test_hiking_equipment_button_sends_to_correct_catalog_page(web_browser):
    """ Нажатие кнопки Походное снаряжение открывает соответствующее окно каталога.
    """

    page = CatalogPage(web_browser)

    page.POKHODNOE_SNARYAZHENIE.click()

    assert page.get_current_url() == TestData.MAIN_URL + 'catalog/pokhodnoe_snaryazhenie_1/'


def test_alpinism_button_sends_to_correct_catalog_page(web_browser):
    """ Нажатие кнопки Альпинизм открывает соответствующее окно каталога.
    """

    page = CatalogPage(web_browser)

    page.ALPINIZM.click()

    assert page.get_current_url() == TestData.MAIN_URL + 'catalog/alpinistskoe_i_skalolaznoe_snaryazhenie/'


def test_promalp_button_sends_to_correct_catalog_page(web_browser):
    """ Нажатие кнопки Промальп открывает соответствующее окно каталога.
    """

    page = CatalogPage(web_browser)

    page.PROMALP.click()

    assert page.get_current_url() == TestData.MAIN_URL + 'catalog/promyshlennyy_alpinizm/'


def test_scrolling_catalog_page_forward(web_browser):
    """ Кнопка Вперёд пролистывает каталог на одну страницу вперёд.
    """

    page = CatalogPage(web_browser)

    page.ODEZHDA.click()
    page.INVENTORY_FORWARD.scroll_to_element()
    page.INVENTORY_FORWARD.click()

    assert 'PAGEN_2=2' in page.get_current_url()


def test_scrolling_catalog_page_back(web_browser):
    """ Кнопка Назад пролистывает каталог на одну страницу назад.
    """

    page = CatalogPage(web_browser)

    page.ODEZHDA.click()
    page.INVENTORY_FOURTH_PAGE.scroll_to_element()
    page.INVENTORY_FOURTH_PAGE.click()
    page.INVENTORY_BACK.scroll_to_element()
    page.INVENTORY_BACK.click()

    assert 'PAGEN_2=3' in page.get_current_url()


def test_filter_by_gender_male(web_browser):
    """ Фильтрация товаров по Пол-Мужской с созданием скриншота (категория Обувь).
    """

    page = CatalogPage(web_browser)

    page.OBUV.click()
    page.FILTER_GENDER.click()
    page.FILTER_MALE_CHECKBOX.click()
    page.FILTER_SUBMIT_CHANGES_BTN.scroll_to_element()
    page.FILTER_SUBMIT_CHANGES_BTN.click()
    page.scroll_down(600)
    time.sleep(0.4)
    page.screenshot('Tests/Screenshots/test-filter-by-gender-male.png')


def test_filter_by_gender_female(web_browser):
    """ Фильтрация товаров по Пол-Женский с созданием скриншота (категория Обувь).
    """

    page = CatalogPage(web_browser)

    page.OBUV.click()
    page.FILTER_GENDER.click()
    page.FILTER_FEMALE_CHECKBOX.click()
    page.FILTER_SUBMIT_CHANGES_BTN.scroll_to_element()
    page.FILTER_SUBMIT_CHANGES_BTN.click()
    page.scroll_down(600)
    time.sleep(0.4)
    page.screenshot('Tests/Screenshots/test-filter-by-gender-female.png')


def test_filter_reset_settings(web_browser):
    """ Проверка кнопки сброса всех фильтров с созданием скриншота.
    """

    page = CatalogPage(web_browser)

    page.OBUV.click()
    page.FILTER_GENDER.click()
    page.FILTER_MALE_CHECKBOX.click()
    page.FILTER_SUBMIT_CHANGES_BTN.scroll_to_element()
    page.FILTER_SUBMIT_CHANGES_BTN.click()
    page.FILTER_DEFAULT_BTN.scroll_to_element()
    page.FILTER_DEFAULT_BTN.click()
    page.scroll_down(600)
    time.sleep(0.4)
    page.screenshot('Tests/Screenshots/test-filter-reset-settings-default.png')
