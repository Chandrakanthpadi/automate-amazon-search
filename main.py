import sys
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"C:\Users\chand\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("http://amazon.in")
search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
search.send_keys(sys.argv[1])
# driver.get("http://flipkart.com")
button = driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')
button.click()