from selenium import webdriver


class Login:
    text_username_xpath = "//input[@type='email']"
    text_password_xpath = "//input[@type='password']"
    btn_login_xpath = "//input[@value='Login']"

    def __init__(self, driver):
        self.driver = driver

    def Set_User(self, username):
        self.driver.find_element_by_xpath(self.text_username_xpath).clear()
        self.driver.find_element_by_xpath(self.text_username_xpath).send_keys(username)

    def Set_pass(self, password):
        self.driver.find_element_by_xpath(self.text_password_xpath).clear()
        self.driver.find_element_by_xpath(self.text_password_xpath).send_keys(password)

    def Click_login(self):
        self.driver.find_element_by_xpath(self.btn_login_xpath).click()
