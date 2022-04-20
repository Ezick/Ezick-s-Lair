from config import TestData

from Pages.base import WebPage
from Pages.elements import WebElement


class CatalogPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = TestData.MAIN_URL
        super().__init__(web_driver, url)

    # Catalog Locators
    ODEZHDA = WebElement(xpath='//*[@id="navbarSupportedContent"]/div/div/ul/li[1]/a')
    OBUV = WebElement(xpath='//*[@id="navbarSupportedContent"]/div/div/ul/li[2]/a')
    POKHODNOE_SNARYAZHENIE = WebElement(xpath='//*[@id="navbarSupportedContent"]/div/div/ul/li[3]/a')
    ALPINIZM = WebElement(xpath='//*[@id="navbarSupportedContent"]/div/div/ul/li[4]/a')
    PROMALP = WebElement(xpath='//*[@id="navbarSupportedContent"]/div/div/ul/li[5]/a')
    FILTER_GENDER = WebElement(css_selector='a[data-target="#filterCollapse100"]')
    FILTER_MALE_CHECKBOX = WebElement(xpath='//*[@id="filterCollapse100"]/label[1]/span[1]')
    FILTER_FEMALE_CHECKBOX = WebElement(xpath='//*[@id="filterCollapse100"]/label[2]/span[1]')
    FILTER_SUBMIT_CHANGES_BTN = WebElement(id='set_filter')
    FILTER_DEFAULT_BTN = WebElement(xpath='//a[contains(text(), "Сбросить")]')
    INVENTORY_FORWARD = WebElement(
        xpath='/html/body/main/div/div/div/div/section/div/div/div[2]/div[2]/div/div/ul/li[7]/a')
    INVENTORY_BACK = WebElement(
        xpath='/html/body/main/div/div/div/div/section/div/div/div[2]/div[2]/div/div/ul/li[1]/a')
    INVENTORY_FOURTH_PAGE = WebElement(
        xpath='/html/body/main/div/div/div/div/section/div/div/div[2]/div[2]/div/div/ul/li[5]/a')
