from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#driver = webdriver.Chrome(r"C:\Users\Purnima Sah\PycharmProjects\firstseleniumtest\Driver\chromedriver.exe")

#driver = webdriver.ie(r"C:\Users\Purnima Sah\PycharmProjects\firstseleniumtest\Driver\IEDriverServer.exe")

driver.get("http://travelerp.braindigit.com/")
email_ele =driver.find_element_by_name("Email")
pass_ele =driver.find_element_by_name("Password")
email_ele.send_keys("sgodar34@yopmail.com")
pass_ele.send_keys("000000")
driver.find_element_by_tag_name("button").click()
Administration =driver.find_element_by_xpath("/html/body/div/div[1]/div/ul/li[1]/a").click()
Manageagency =driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[1]/ul/li[4]").click()
searchagency=driver.find_element_by_id("txtSearchkeywords").send_keys("Purnima2")
search=driver.find_element_by_tag_name("button").click()

#driver.close()
