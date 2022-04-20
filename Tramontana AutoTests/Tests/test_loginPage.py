#  Запуск всех тестов из этой категории осуществляется по команде:
#  pytest -v --driver Chrome --driver-path /Driver/chromedriver.exe Tests/test_loginPage.py

from Pages.loginPage import LoginPage
from config import TestData


def test_login_btn_opens_registration_form(web_browser):
    """ При нажатии кнопки Войти появляется форма регистрации.
    """

    page = LoginPage(web_browser)

    page.LOG_IN_BTN.click()
    page.AUTH_FORM.is_visible()

    assert True


def test_successful_registration_for_new_user(web_browser):
    """ Успешная регистрация нового пользователя при заполнении
        всех полей с появлением подтверждающего сообщения.
    """

    page = LoginPage(web_browser)

    page.LOG_IN_BTN.click()
    page.AUTH_FIRSTNAME.send_keys('Donald')
    page.AUTH_LASTNAME.send_keys('Duck')
    page.AUTH_EMAIL.send_keys(TestData.NEW_MAIL)
    page.AUTH_PASSWORD.send_keys(TestData.VALID_PASSWORD)
    page.AUTH_CONFIRM_PASSWORD.send_keys(TestData.VALID_PASSWORD)
    page.AUTH_SUBMIT_BTN.click()
    page.AUTH_SUCCESS_MESSAGE.is_visible()

    assert True


def test_registration_is_not_correct_while_user_dont_repeat_password(web_browser):
    """ Негативный тест: появление сообщения об ошибке, если при регистрации
        новый пользователь неверно ввёл повторный пароль.
    """

    page = LoginPage(web_browser)

    page.LOG_IN_BTN.click()
    page.AUTH_FIRSTNAME.send_keys('Donald')
    page.AUTH_LASTNAME.send_keys('Duck')
    page.AUTH_EMAIL.send_keys(TestData.VALID_MAIL)
    page.AUTH_PASSWORD.send_keys(TestData.VALID_PASSWORD)
    page.AUTH_CONFIRM_PASSWORD.send_keys(TestData.WRONG_PASSWORD)
    page.AUTH_SUBMIT_BTN.click()
    page.AUTH_NOT_SAME_PASSWORDS_MESSAGE.is_visible()

    assert True


def test_new_user_cant_authorized_with_usable_email(web_browser):
    """ Негативный тест: появление сообщения об ошибке, если при регистрации
        новый пользователь ввёл эл.адрес, уже использующийся в базе.
    """

    page = LoginPage(web_browser)

    page.LOG_IN_BTN.click()
    page.AUTH_FIRSTNAME.send_keys('Donald')
    page.AUTH_LASTNAME.send_keys('Duck')
    page.AUTH_EMAIL.send_keys(TestData.VALID_MAIL)
    page.AUTH_PASSWORD.send_keys(TestData.WRONG_PASSWORD)
    page.AUTH_CONFIRM_PASSWORD.send_keys(TestData.WRONG_PASSWORD)
    page.AUTH_SUBMIT_BTN.click()
    page.AUTH_NOT_UNIQUE_EMAIL_MESSAGE.is_visible()

    assert True


def test_successful_login(web_browser):
    """ Успешный вход в аккаунт по логину(эл.почте) и паролю.
    """

    page = LoginPage(web_browser)

    page.LOG_IN_BTN.click()
    page.LOGIN_TEXTBOX.send_keys(TestData.VALID_MAIL)
    page.LOGIN_PASSWORD_TEXTBOX.send_keys(TestData.VALID_PASSWORD)
    page.LOGIN_SUBMIT_BTN.click()
    page.LOGIN_SUCCESS_START_PAGE.is_visible()

    assert True


def test_unsuccessful_login_with_wrong_email(web_browser):
    """ Негативный тест: появление сообщения об ошибке, если при попытке авторизации
        пользователь неверно указал эл.адрес.
    """

    page = LoginPage(web_browser)

    page.LOG_IN_BTN.click()
    page.LOGIN_TEXTBOX.send_keys(TestData.WRONG_MAIL)
    page.LOGIN_PASSWORD_TEXTBOX.send_keys(TestData.VALID_PASSWORD)
    page.LOGIN_SUBMIT_BTN.click()
    page.LOGIN_ERROR_MESSAGE.is_visible()

    assert True


def test_unsuccessful_login_with_wrong_password(web_browser):
    """ Негативный тест: появление сообщения об ошибке, если при попытке авторизации
        пользователь неверно указал пароль.
    """

    page = LoginPage(web_browser)

    page.LOG_IN_BTN.click()
    page.LOGIN_TEXTBOX.send_keys(TestData.VALID_MAIL)
    page.LOGIN_PASSWORD_TEXTBOX.send_keys(TestData.WRONG_PASSWORD)
    page.LOGIN_SUBMIT_BTN.click()
    page.LOGIN_ERROR_MESSAGE.is_visible()

    assert True


def test_check_forgot_password_button(web_browser):
    """ В окне авторизации можно нажать кнопку для напоминания пароля.
    """

    page = LoginPage(web_browser)

    page.LOG_IN_BTN.click()
    page.LOGIN_FORGOT_PASSWORD.click()
    page.LOGIN_TEXTBOX.send_keys(TestData.VALID_MAIL)
    page.LOGIN_REMIND_PASSWORD_BTN.is_clickable()

    assert True
