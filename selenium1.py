from selenium import webdriver
browser = webdriver.Chrome()
browser.get ('https://www.facebook.com')
browser.find_element_by_name("email").send_keys("kashishshah8500@yahoo.com")
browser.find_element_by_name("pass").send_keys("kashish0805")
browser.find_element_by_name("login").click()