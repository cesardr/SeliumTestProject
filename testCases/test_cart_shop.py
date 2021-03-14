from Utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
import pytest


class Test_002_Cart:
    baseURL = "http://automationpractice.com/index.php"
    useremail = 'vectron36@gmail.com'
    password = 'Shadow1975'

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_Cart(self, setup):

        self.logger.info("************** Verifying Login Test *********** ")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        ActionChains(self.driver)
        self.driver.find_element_by_id("search_query_top").click()
        self.driver.find_element_by_id("search_query_top").send_keys("dress")
        self.driver.find_element_by_name('submit_search').click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,300)", "")
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[2]/ul/li[1]/div/div[2]/h5/a").click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,300)", "")
        self.driver.find_element_by_id("quantity_wanted").click()
        self.driver.find_element_by_css_selector(".icon-plus").click()
        self.driver.find_element_by_id("group_1").click()
        self.driver.find_element_by_id("color_14").click()
        self.driver.find_element(By.CSS_SELECTOR, ".exclusive > span").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart > a").click()
        time.sleep(3)
        act_title = self.driver.find_element_by_name = 'Proceed to checkout'
        if act_title == 'Proceed to checkout':
            assert True
            self.logger.info("************** Cart Test  is Passed *********** ")
            time.sleep(3)
        else:
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_cart.png')
            self.logger.error("************** Cart Test Failed *********** ")
            assert False
