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
Business=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[4]/a").click()
consolidationswitch=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[4]/ul/li[1]/a").click()
Sabre=driver.find_element_by_xpath("/html/body/div/div[2]/div/div[5]/div[4]/div/div/form/div[1]/div/div[1]/div[4]/span[2]/input").click()
Sabrebackoff=driver.find_element_by_xpath("/html/body/div/div[2]/div/div[5]/div[4]/div/div/form/div[1]/div/div[2]/div/input").get_attribute("checked")
Plasma=driver.find_element_by_xpath("/html/body/div/div[2]/div/div[5]/div[4]/div/div/form/div[2]/div/div[1]/div[4]/span[2]/input").click()
Yetiairlines=driver.find_element_by_xpath("/html/body/div/div[2]/div/div[5]/div[4]/div/div/form/div[3]/div/div[1]/div[4]/span[2]/input").click()