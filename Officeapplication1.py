from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r"C:\Users\Purnima Sah\PycharmProjects\firstseleniumtest\Driver\chromedriver.exe")
#driver = webdriver.Firefox(r"C:\Users\Purnima Sah\PycharmProjects\firstseleniumtest\Driver\geckosdriver.exe")
#driver = webdriver.Ie(r"C:\Users\Purnima Sah\PycharmProjects\firstseleniumtest\Driver\IEDriverServer.exe")
#driver.implicitly_wait(10)
driver.get("http://travelerp.braindigit.com/")
print(driver.title)
print(driver.current_url)
email_ele =driver.find_element_by_name("Email")
pass_ele =driver.find_element_by_name("Password")
email_ele.send_keys("sgodar34@yopmail.com")
pass_ele.send_keys("000000")
driver.find_element_by_tag_name("button").click()
OfficeApplication =driver.find_element_by_xpath("/html/body/div/div[1]/div/ul/li[3]").click()
#submodule1
Managedepartment=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[3]/ul/li[1]/a/span").click()
Addone=driver.find_element_by_xpath("/html/body/div/div[2]/div/div[5]/div[1]/div/a").click()
#DepartmentName=driver.find_element_by_xpath("/html/body/div/div[2]/div/div[5]/div/div/div/div[2]/form/div[1]/div[2]/input").click()
driver.close()