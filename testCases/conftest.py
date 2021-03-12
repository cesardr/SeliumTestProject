from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(
        executable_path=r"C:/Users/DELL/PycharmProjects/SeliumTestProject/Drivers/chromedriver.exe")
    return driver
