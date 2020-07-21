from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r"C:\Users\Purnima Sah\PycharmProjects\firstseleniumtest\Driver\chromedriver.exe")
driver.maximize_window()
driver.get("http://travelerp.braindigit.com/")
print(driver.title)
print(driver.current_url)
email_ele = driver.find_element_by_name("Email")
pass_ele = driver.find_element_by_name("Password")
email_ele.send_keys("sgodar34@yopmail.com")
pass_ele.send_keys("000000")
driver.find_element_by_tag_name("button").click()
mcw=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[5]/a").click()
mcww = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[5]/ul/li[1]").click()