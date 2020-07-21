
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r"C:\Users\Purnima Sah\PycharmProjects\firstseleniumtest\Driver\chromedriver.exe")

driver.get("http://travelerp.braindigit.com/")
print(driver.title)
print(driver.current_url)
email_ele = driver.find_element_by_name("Email")
pass_ele = driver.find_element_by_name("Password")
email_ele.send_keys("sgodar34@yopmail.com")
pass_ele.send_keys("000000")
driver.find_element_by_tag_name("button").click()
report = driver.find_element_by_xpath("html/body/div/div[1]/div/ul/li[8]/a").click()
salesreport = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[8]/ul/li[2]").click()
reportdata= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[2]/div[1]/button[2]").click()
exportxl= driver.find_element_by_id("exportToExcel").click()
advsrch = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/div/div[1]").click()