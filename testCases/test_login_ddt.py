import time

from utilities import XLUtils
from selenium import webdriver

driver=webdriver.Chrome(executable_path="/home/snehal/Downloads/chromedriver_linux64/chromedriver")

path="/home/snehal/PycharmProjects/login_ddt_framework/testData/myexcel.xlsx"

rows = XLUtils.getRowCount(path, 'Sheet1')

for r in range(2,rows+1):
    driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    driver.maximize_window()

    username = XLUtils.readData(path, "Sheet1", r, 1)
    password = XLUtils.readData(path, "Sheet1", r, 2)

    driver.find_element_by_xpath('//input[@id="ap_email"]').send_keys(username)
    time.sleep(2)
    driver.find_element_by_xpath('//input[@id="continue"]').click()
    time.sleep(2)
    if username != "snehalahire107@gmail.com":
        time.sleep(2)
        print("test failed")
        XLUtils.writeData(path, "Sheet1", r, 3, "test failed")
        continue
    else:
        driver.find_element_by_xpath('//input[@id="ap_password"]').send_keys(password)
        time.sleep(2)
        if password != "snehal1993":
            print("test failed")
            XLUtils.writeData(path, "Sheet1", r, 3, "test failed")
            continue
        else:
            driver.find_element_by_xpath('//input[@id="signInSubmit"]').click()
            time.sleep(3)
            driver.find_element_by_id("nav-logo-sprites").click()
            time.sleep(5)

            if driver.title == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in":
                print("test is passed")
                XLUtils.writeData(path, "Sheet1", r, 3, "test passed")
            else:
                print("test failed")
                XLUtils.writeData(path, "Sheet1", r, 3, "test failed")










        time.sleep(5)

    #driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
#driver.close()