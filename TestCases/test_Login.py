import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig



class Test_001_Login:
    pravid_login_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @step()
    def test_HomePage_title(self, setup):
        self.driver = setup
        self.driver.get(self.pravid_login_url)
        actual_title = self.driver.title
        if actual_title == "Pravid | AI-led Debt Collections. Reliable, Affordable and Personalized":
            print(actual_title)
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_HomePage_title.png")
            assert False

    @step()
    def test_Login(self, setup):
        self.driver = setup
        self.driver.get(self.pravid_login_url)
        self.LoginPg = Login(self.driver)
        self.LoginPg.Set_User(self.username)
        self.LoginPg.Set_pass(self.password)
        self.LoginPg.Click_login()

