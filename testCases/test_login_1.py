
import pytest
from selenium import webdriver
import json
import time
from ddt import ddt, data, file_data, idata, unpack
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(executable_path="/home/snehal/Downloads/chromedriver_linux64/chromedriver")


class Test_001_Login:
    with open('/home/snehal/PycharmProjects/login_ddt_framework/testData/testData.json',"r") as f1:
        data = json.load(f1)
    print("__________________")
    print(data)
    print("__________________")


    def test_login(self, setup):
        with open('/home/snehal/PycharmProjects/login_ddt_framework/testData/testData.json', "r") as f1:
            data = json.load(f1)
            print("*****************")
            print(data)
            print("****************")

            for i in data["test"]:
                print(i)
                print(i["useremail"])
                driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
                driver.find_element_by_id("ap_email").send_keys(i["useremail"])
                driver.find_element_by_id("continue").click()
                driver.find_element_by_id("ap_password").send_keys(i["password1"])
                driver.find_element_by_id("signInSubmit").click()
                driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")































