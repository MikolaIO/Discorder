import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from support_functions import fill_login_field, click_button


def account_login(mail, passwd, drv):
    click_button("login-button-js", drv)
    fill_login_field(mail, "uid_7", drv)
    fill_login_field(passwd, "uid_9", drv)
    click_button("button__5573c", drv)
    time.sleep(5)


def open_chat(usr, drv):
    element = WebDriverWait(drv, 20).until(EC.presence_of_element_located
                                           ((By.CSS_SELECTOR, "a[aria-label*='" + usr + "']")))
    element.click()


def send_message(msg, drv):

    element = WebDriverWait(drv, 20).until(EC.presence_of_element_located
                                           ((By.CSS_SELECTOR, ".editor__66464")))
    element.send_keys(msg, Keys.ENTER)


driver = webdriver.Firefox()
message = "Discorder greets you :)"
email = "abc@gmail.com"
password = "xyz"
target_user = "qwerty"

driver.get("https://discord.com/")
account_login(email, password, driver)
open_chat(target_user, driver)
send_message(message, driver)

time.sleep(5)
driver.close()
