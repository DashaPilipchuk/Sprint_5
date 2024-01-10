from selenium.webdriver.common.by import By


class Locators:
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx "
                                         "button_button_size_large__G21Vg']")
    REGISTRATION_TO_ACCOUNT_BUTTON = (By.XPATH, '//p[@class="undefined text text_type_main-default '
                                                'text_color_inactive mb-4"]/a[@class="Auth_link__1fOlj"]')
    NAME_FIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    INVALID_PASSWORD_MESSAGE = (By.XPATH, "//p[@class='input__error text_type_main-default']")
    ENTER = (By.XPATH, "//h2[text()='Вход']")
    REGISTRATION = (By.XPATH, "//h2[text()='Регистрация']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    CHECKOUT_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                                 "button_button_size_large__G21Vg']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGIN_LINK = (By.XPATH, "//a[@class='Auth_link__1fOlj']")
    RECOVER_THE_PASSWORD_BUTTON = (By.XPATH, "//p[@class='undefined text text_type_main-default "
                                             "text_color_inactive']/a[@class='Auth_link__1fOlj']")
    RECOVER_THE_PASSWORD = (By.XPATH, "//h2[text()='Восстановление пароля']")
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()= 'Личный Кабинет']")
    PERSONAL_ACCOUNT_TEXT = (By.XPATH, "//p[@class='Account_text__fZAIn text text_type_main-default']")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()= 'Конструктор']")
    BURGER_TEXT = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")
    LOGOUT_BUTTON = (By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")
    LOGO_BUTTON = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    ROLLS = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_BUTTON = (By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 "
                               "noselect']")
    SAUCES = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS = (By.XPATH, "//h2[text()='Начинки']")






