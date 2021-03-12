from selenium.webdriver import ActionChains
from Utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.common.by import By


class Test_001_Login:
    baseURL = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
    useremail = 'vectron36@gmail.com'
    password = 'Shadow1975'

    logger = LogGen.loggen()

    def test_Login(self, setup):

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
        self.driver.execute_script("window.scrollBy(0,300)", "")
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[2]/ul/li[1]/div/div[2]/h5/a").click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,300)", "")
        self.driver.find_element_by_id("quantity_wanted").click()
        self.driver.find_element_by_css_selector(".icon-plus").click()
        self.driver.find_element_by_id("group_1").click()
        self.driver.find_element_by_id("color_14").click()
        self.driver.find_element(By.CSS_SELECTOR, ".exclusive > span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart > a").click()


