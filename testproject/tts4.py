#  2 Feladat: Pénzfeldobás

from selenium import webdriver
#  from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import random
import string
import sys

driver = webdriver.Chrome()
#  driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/tts4.html"

driver.get(URL)

####################################################
#                PYTHON FUNCTIONS
####################################################


####################################################
#                    WORKBENCH
####################################################

#  Lista, számlálók, elvárt eredmény változói
list_of_coins = []
count_heads = 0
count_tails = 0
excepted_TC01_min_heads = 30

#  Klikkelési folyamat, és listához való hozzáfűzés végrehajtója
for i in range(0, 100):
    submit_btn = driver.find_element_by_id('submit').click()
    list_of_coins.append(driver.find_element_by_id('lastResult').text)

# print(list_of_coins)
# print(len(list_of_coins))

#  Fej és írás számláló
for i in range(0, len(list_of_coins)):
    if list_of_coins[i] == 'fej':
        count_heads += 1
    else:
        count_tails += 1

# print(count_heads)
# print(count_tails)

####################################################
#                  TEST CASES
####################################################

#  TC01
assert excepted_TC01_min_heads <= count_heads
print(excepted_TC01_min_heads <= count_heads)
