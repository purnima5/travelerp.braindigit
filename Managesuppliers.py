from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r"C:\Users\Purnima Sah\PycharmProjects\firstseleniumtest\Driver\chromedriver.exe")
driver.get("http://travelerp.braindigit.com/")
driver.implicitly_wait(10)
#assert "Dashboard" in driver.title
email_ele =driver.find_element_by_name("Email")
pass_ele =driver.find_element_by_name("Password")
email_ele.send_keys("sgodar34@yopmail.com")
pass_ele.send_keys("000000")
driver.find_element_by_tag_name("button").click()
Administration=driver.find_element_by_xpath("/html/body/div/div[1]/div/ul/li[1]/a").click()
Managesuppliers=driver.find_element_by_xpath("/html/body/div/div[1]/div/ul/li[1]/ul/li[3]").click()
searchsuppliers=driver.find_element_by_id("txtSearchkeywords").send_keys("plasma")
search=driver.find_element_by_tag_name("button").click()
#driver.close()
