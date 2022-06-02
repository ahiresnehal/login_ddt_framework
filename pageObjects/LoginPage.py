class LoginPage:
    textbox_username_id="ap_email"
    button_continue_id ="continue"
    textbox_password_id="ap_password"
    button_login_id="signInSubmit"

    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def clickContinue(self):
        self.driver.find_element_by_id(self.button_continue_id).click()

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.button_login_id).click()

