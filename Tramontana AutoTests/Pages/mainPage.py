from config import TestData

from Pages.base import WebPage
from Pages.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = TestData.MAIN_URL
        super().__init__(web_driver, url)

    # HeaderLocators:
    TRAMONTANA_LOGO = WebElement(css_selector='.logo-block>a')
    DELIVERY = WebElement(xpath='//a[@class="mr-3" and contains(text(), "доставка")]')
    RETURN = WebElement(xpath='//a[@class="mx-3" and contains(text(), "возврат")]')
    OPT_MENU = WebElement(xpath='//a[@class="mx-3" and contains(text(), "опт")]')
    CONTACTS = WebElement(xpath='//a[@class="mx-3" and contains(text(), "контакты")]')
    PROFILE = WebElement(xpath='//*[@id="personal-icons"]/a[1]')
    CART = WebElement(xpath='//*[@id="personal-icons"]/a[4]')
    SKALODROM = WebElement(xpath='//a[@class="mx-3" and contains(text(), "скалодром")]')
    SEARCH_TEXTBOX = WebElement(id='title-search-input')
    SEARCH_NOTHING_MESSAGE = WebElement(
        xpath='//div[@class="py-4" and contains(text(), "Сожалеем, но ничего не найдено")]')  # ?????
    VK_LINK = WebElement(xpath='//*[@id="social-buttons"]/a[1]')
    TWITTER_LINK = WebElement(xpath='//*[@id="social-buttons"]/a[2]')
    YOUTUBE_LINK = WebElement(xpath='//*[@id="social-buttons"]/a[3]')
    TELEGRAM_LINK = WebElement(xpath='//*[@id="social-buttons"]/a[4]')
    CAROUSEL_LEFT = WebElement(class_name='("fas.fa-angle-left")[0]')
    CAROUSEL_RIGHT = WebElement(class_name='("fas.fa-angle-right")[0]')
    DARK_THEME = WebElement(xpath='//a[contains(text(), "темная сторона")]')

    # Opt Menu:
    OPT_NAME_TEXTBOX = WebElement(xpath='//input[@name="form_text_42"]')
    OPT_EMAIL_TEXTBOX = WebElement(xpath='//input[@name="form_email_45"]')
    OPT_PHONE_TEXTBOX = WebElement(xpath='//input[@name="form_text_44"]')
    OPT_SUBMIT_BTN = WebElement(name='web_form_submit')
    OPT_SUCCESSFUL_MESSAGE = WebElement(xpath='//font[@class="notetext" and contains(text(), "Ваша заявка принята!")')
