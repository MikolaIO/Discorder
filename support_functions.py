from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fill_login_field(txt, elem, drv):
    element = WebDriverWait(drv, 20).until(EC.presence_of_element_located
                                           ((By.ID, elem)))
    element.clear()
    element.send_keys(txt)


def click_button(elem, drv):
    element = WebDriverWait(drv, 20).until(EC.presence_of_element_located
                                           ((By.CLASS_NAME, elem)))
    element.click()
