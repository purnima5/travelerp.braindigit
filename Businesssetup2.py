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
#For manage of promo code
Managepromocode=driver.find_element_by_xpath("/html/body/div/div[1]/div/ul/li[4]/ul/li[2]/a/span").click()
Addnew=driver.find_element_by_xpath("/html/body/div/div[2]/div/div[5]/div[1]/div/a").click()
Defineproduct=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/form/div/div[2]/div/div[1]/div[2]/div/div/div[2]/select").click()
promocodecriteria=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/form/div/div[2]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/select/option[5]").click()
Addnew1=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/form/div/div[2]/div/div[2]/div[2]/div[4]").click()
Fordeletion=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/form/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/span").click()
#For Define promo code and discount
selfpromo=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/form/div/div[3]/div/div/div[2]/div[1]/div/div/div/label").get_attribute("checked")