#  3 Feladat: Összeadó

from selenium import webdriver
#  from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import random
import string
import sys
import operator

driver = webdriver.Chrome()
#  driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html"

driver.get(URL)


####################################################
#                PYTHON FUNCTIONS
####################################################


#  in JS code: var ops = ['+', '-', '*']
ops = {"+": operator.add, "-": operator.sub, '*': operator.mul}


def calculator():
    num1 = int(driver.find_element_by_id('num1').text)
    op = driver.find_element_by_id('op').text
    num2 = int(driver.find_element_by_id('num2').text)
    return ops[op](num1, num2)


####################################################
#                    WORKBENCH
####################################################


driver.find_element_by_id('submit').click()

#  Az weboldalon megjelent eredményt kiírjuk egy változóba
final_result = int(driver.find_element_by_id('result').text)

# print(final_result)
# print(calculator())

####################################################
#                   TEST CASES
####################################################

#  TC01
assert calculator() == final_result
