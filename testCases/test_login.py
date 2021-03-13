from Utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
import pytest
from selenium.webdriver.common.by import By
import time


class Test_001_Login:
    baseURL = "http://automationpractice.com/index.php"
    useremail = 'vectron36@gmail.com'
    password = 'Shadow1975'

    logger = LogGen.loggen()

    def test_homePageTile(self, setup):

        self.logger.info(" ************** Test_001_login *********** ")
        self.logger.info(" ************** verifying home page title *********** ")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "My Store":
            assert True
            time.sleep(5)
            self.driver.close()
            self.logger.info("************** Home Page title test is Passed **********")
        else:
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_homepageTitle.png')
            self.driver.close()
            self.logger.error("************** Home Page Title is Failed *********** ")
            assert False

    @pytest.mark.regression
    def test_Login(self, setup):

        self.logger.info("************** Verifying Login Test *********** ")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.driver.find_element(By.LINK_TEXT, "Sign in").click()
        self.lp = LoginPage(self.driver)
        self.lp.setUsermail(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == 'My account - My Store':
            assert True
            self.logger.info("************** Login Test  is Passed *********** ")
            time.sleep(3)
            self.driver.close()
        else:
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_Login.png')
            self.driver.close()
            self.logger.error("************** Login Test Failed *********** ")
            self.driver.close()
            assert False
