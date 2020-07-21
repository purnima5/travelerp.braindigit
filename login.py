from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r"C:\Users\Purnima Sah\PycharmProjects\firstseleniumtest\Driver\chromedriver.exe")

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://travelerp.braindigit.com/")
print(driver.title)
email_ele =driver.find_element_by_name("Email")
pass_ele =driver.find_element_by_name("Password")
email_ele.send_keys("sgodar34@yopmail.com")
pass_ele.send_keys("000000")
#driver.find_element_by_tag_name("button").click()
driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/div/div/p/a").click()
Forgetpass_ele =driver.find_element_by_name("Email")
Forgetpass_ele.send_keys("sgodar34@yopmail.com")
# driver.find_element_by_xpath(("/html/body/div[1]/div/main/div[2]/div/div/form/div[2]")).send_keys(
# "sgodar34@yopmail.com")
#driver.find_element_by_xpath("/html/body/div[1]/div/main/div[2]/div/div/form/div[2]/div[2]/button").click()
submit=driver.find_element_by_tag_name("button").click()

driver.close()#for closing the page
driver.quit()
print("test completed")
