#  1 Feladat: Keressük a téglalap kerületét

from selenium import webdriver
#  from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import random
import string
import sys

driver = webdriver.Chrome()
#  driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/x234.html"

driver.get(URL)

####################################################
#                PYTHON FUNCTIONS
####################################################


def creator(a, b):
    driver.find_element_by_id('a').send_keys(a)
    driver.find_element_by_id('b').send_keys(b)
    driver.find_element_by_id('submit').click()
    #  Mezők ürítése a folyamat végrehajtását követően
    driver.find_element_by_id('a').clear()
    driver.find_element_by_id('b').clear()
    return driver.find_element_by_id('result').text

####################################################
#                    WORKBENCH
####################################################

# a = driver.find_element_by_id('a').send_keys('99')
# b = driver.find_element_by_id('b').send_keys('12')
# calc_btn = driver.find_element_by_id('submit').click()
# result = driver.find_element_by_id('result').text
# print(result)

#  Elvárt eredmények változói


excepted_TC1_result = 222
excepted_TC2_result = 'NaN'
excepted_TC3_result = 'NaN'


#  Függvény futtatása
# print(creator(99, 12))
# print(creator('kiskutya', 12))
# print(creator('', ''))


####################################################
#                  TEST CASES
####################################################

#  TC01
assert excepted_TC1_result == int(creator(99, 12))

#  TC02
assert excepted_TC2_result == creator('kiskutya', 12)

#  TC03
assert excepted_TC3_result == creator('', '')
