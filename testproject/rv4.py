#  5 Feladat: Kakukktojás - városok

from selenium import webdriver
#  from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import random
import string
import sys

driver = webdriver.Chrome()
#  driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/rv4.html"

driver.get(URL)

####################################################
#                PYTHON FUNCTIONS
####################################################


####################################################
#                    WORKBENCH
####################################################

cities_txt = driver.find_element_by_xpath('//textarea').text
print(cities_txt)
#  Leválasztom az első és utolsó idézőjelet (kivételkezelés um)
cities_txt = cities_txt[1:len(cities_txt)-1]
#  Előállítok egy szeparátort, amely egyben a fölös idézőjeleket is leszedi
list_of_cities = cities_txt.split('", "')
print(list_of_cities)
result = driver.find_element_by_id('result').text
index = 0
while result == 'Nem találtad el.' or result == '':
    driver.find_element_by_id('missingCity').send_keys(list_of_cities[index])
    driver.find_element_by_id('submit').click()
    driver.find_element_by_id('missingCity').clear()
    index += 1
    # time.sleep(1)

####################################################
#                  TEST CASES
####################################################



