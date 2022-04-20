from config import TestData

from Pages.base import WebPage
from Pages.elements import WebElement


class LoginPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = TestData.MAIN_URL
        super().__init__(web_driver, url)

    # Login Locators
    LOG_IN_BTN = WebElement(xpath='//*[@id="personal-icons"]/a[1]')
    LOGIN_TEXTBOX = WebElement(name='USER_LOGIN')
    LOGIN_PASSWORD_TEXTBOX = WebElement(name='USER_PASSWORD')
    LOGIN_SUBMIT_BTN = WebElement(name='Login')
    LOGIN_SUCCESS_START_PAGE = WebElement(xpath=f'//td[contains(text(), {TestData.VALID_MAIL})]')
    LOGIN_ERROR_MESSAGE = WebElement(xpath='//font[contains(text(), "Неверный логин или пароль.")]')  # ???????
    LOGIN_FORGOT_PASSWORD = WebElement(xpath='//a[contains(text(), "Забыли свой пароль?")]')
    LOGIN_REMIND_PASSWORD_BTN = WebElement(name='send_account_info')
    AUTH_FORM = WebElement(name='regform')
    AUTH_FIRSTNAME = WebElement(name='REGISTER[NAME]')
    AUTH_LASTNAME = WebElement(name='REGISTER[LAST_NAME]')
    AUTH_EMAIL = WebElement(name='REGISTER[EMAIL]')
    AUTH_PASSWORD = WebElement(name='REGISTER[PASSWORD]')
    AUTH_CONFIRM_PASSWORD = WebElement(name='REGISTER[CONFIRM_PASSWORD]')
    AUTH_SUBMIT_BTN = WebElement(name='register_submit_button')
    AUTH_SUCCESS_MESSAGE = WebElement(xpath='//*[@id="registration-succeeded"]/h1')
    AUTH_NOT_SAME_PASSWORDS_MESSAGE = WebElement(class_name='("validate-response")[1]')
    AUTH_NOT_UNIQUE_EMAIL_MESSAGE = WebElement(class_name='errortext')
