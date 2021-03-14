from Utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest
from selenium.webdriver.common.by import By


class Test_003_Search:
    baseURL = "http://automationpractice.com/index.php"
    useremail = 'vectron36@gmail.com'
    password = 'Shadow1975'

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_search(self, setup):

        self.logger.info("************** Verifying search Test *********** ")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.driver.find_element(By.LINK_TEXT, "Sign in").click()
        self.lp = LoginPage(self.driver)
        self.lp.setUsermail(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        ActionChains(self.driver)
        self.driver.find_element_by_id("search_query_top").click()
        self.driver.find_element_by_id("search_query_top").send_keys("dress")
        self.driver.find_element_by_name("submit_search").click()
        time.sleep(5)
        element = self.driver.find_element_by_class_name("heading-counter").text
        print(element)


