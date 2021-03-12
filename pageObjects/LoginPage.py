class LoginPage:
    textbox_username_id = "email"
    textbox_password_id = "passwd"
    button_login_xpath = "/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/p[2]/button"
    link_logout_linktext = "Sign out"

    def __init__(self, driver):
        self.driver = driver

    def setUsermail(self, useremail):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(useremail)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
