from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox(executable_path=r"C:\Users\Ievgen.Korsun\AppData\Local\Programs\Python\Python36-32\selenium\webdriver\geckodriver-v0.16.1-win64\geckodriver.exe")
main_page = "http://www.google.com"

def assertIn(d, s):
    title = d.title
    if s in title and len(s) == len(title):
        assert s in title
        print("OK")
        print("Actual result is: '%s';\nExpected result is: '%s'" % (title, s))
    else:
        exit("ERROR: Actual result is: '%s';\nExpected result is: '%s'" % (title, s))

driver.get(main_page)
input_field = driver.find_element_by_id('lst-ib')
input_field.click()
input_field.send_keys('weather')
input_field.submit()
WebDriverWait(driver, 10).until(expected_conditions.title_is('weather - Пошук Google'))
driver.implicitly_wait(10)
str = 'weather - Пошук Google'
assertIn(driver, str)
driver.quit()




