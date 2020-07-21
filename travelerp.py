from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://travelerp.braindigit.com/")
email ="abcdep@gmail.com"
password = "123@3"
email_xpath ='//*[@id="Email"]'
password_xpath = '//*[@id="Password"]'
Login_button_xpath ='/html/body/div/div/main/div[2]/div/div/form/div/div[3]/button'
email_element = driver.find_element_by_xpath(email_xpath)
password_element = driver.find_element_by_xpath(password_xpath)
login_button_element = driver.find_element_by_xpath(login_button_xpath)
email_element.send_keys(email)
password_element.send_keys(password)
login_button_element.click()