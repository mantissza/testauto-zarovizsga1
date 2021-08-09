#  4 Feladat: Email mező

from selenium import webdriver
#  from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import random
import string
import sys

driver = webdriver.Chrome()
#  driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/mm43.html"

driver.get(URL)

####################################################
#                PYTHON FUNCTIONS
####################################################


def errorMessages(email):
    driver.find_element_by_id('email').send_keys(email)
    driver.find_element_by_id('submit').click()
    if driver.find_elements_by_xpath('//*[contains(text(), "Please")]'):
        return driver.find_element_by_xpath('//*[contains(text(), "Please")]').text
    else:
        return ''

####################################################
#                    WORKBENCH
####################################################


input_TC01_email = 'teszt@elek.hu'
input_TC02_email = 'teszt@'
input_TC03_email = ''

excepted_TC01_errorMessage = ''
excepted_TC02_errorMessage = "Please enter a part following '@'. 'teszt@' is incomplete."
excepted_TC03_errorMessage = 'Please fill in this field.'

input_field = driver.find_element_by_id('email')

result_TC01_errorMessage = errorMessages(input_TC01_email)
input_field.clear()

result_TC02_errorMessage = errorMessages(input_TC02_email)
input_field.clear()

result_TC03_errorMessage = errorMessages(input_TC03_email)
input_field.clear()


####################################################
#                  TEST CASES
####################################################

#  TC01
assert result_TC01_errorMessage == excepted_TC01_errorMessage

#  TC02
assert result_TC02_errorMessage == excepted_TC02_errorMessage

#  TC03
assert result_TC03_errorMessage == excepted_TC03_errorMessage

