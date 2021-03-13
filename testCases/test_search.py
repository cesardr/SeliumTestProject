from Utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest


class Test_003_Search:
    baseURL = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
    useremail = 'vectron36@gmail.com'
    password = 'Shadow1975'

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_search(self, setup):

        self.logger.info("************** Verifying Login Test *********** ")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsermail(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == 'My account - My Store':
            assert True
            self.logger.info("************** Login Test  is Passed *********** ")
            time.sleep(5)
        else:
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_Login.png')
            self.logger.error("************** Login Test Failed *********** ")
            assert False

        ActionChains(self.driver)
        self.driver.find_element_by_id("search_query_top").click()
        self.driver.find_element_by_id("search_query_top").send_keys("dress")
        self.driver.find_element_by_name("submit_search").click()
        time.sleep(2)


        act_title= self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div[2]/h1/span[2]')
        if act_title == 'found':
            assert True
            self.logger.info("************** Login Test  is Passed *********** ")
            time.sleep(5)
        else:
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_Login.png')
            self.logger.error("************** Login Test Failed *********** ")
            assert False
            self.driver.close()
