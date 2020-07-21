from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r"C:\Users\Family\PycharmProjects\Firstseleniumtest\Driver\chromedriver.exe")

driver.get("http://travelerp.braindigit.com/")
print(driver.title)
print(driver.current_url)
email_ele =driver.find_element_by_name("Email")
pass_ele =driver.find_element_by_name("Password")
email_ele.send_keys("sgodar34@yopmail.com")
pass_ele.send_keys("000000")
driver.find_element_by_tag_name("button").click()

#For flight module
Flight=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[2]").click()
#submodule of flight
#RetrievePNRrequest = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[2]/ul/li[1]").click()
Domestic= driver.find_element_by_xpath("/html/body/div/div[1]/div/ul/li[2]/ul/li[2]").click()

Radiobutton = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/form/div/div/div/div/div[2]/div[1]/div[2]").click()

From = driver.find_element_by_id("txtSrhFromLocation").click()

forselection= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/form/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[3]/ul/li[3]/div").click()

To = driver.find_element_by_name("Destination").click()
Toselectthelocation= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/form/div/div/div/div/div[2]/div[2]/div[1]/div[3]/div[3]/ul/li[5]").click()

driver.implicitly_wait(5)
driver.find_element_by_name("DepartureDate").click()
Ddate= driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr[3]/td[5]").click()

driver.implicitly_wait(5)
driver.find_element_by_name("ReturnDate").click()
Returndate= driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr[4]/td[3]").click()

passenger= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/form/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[2]").click()

adult= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/form/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div/div[3]/div/div[1]/div[2]/button[2]").click()

baby= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/form/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div/div[3]/div/div[2]/div[2]/button[2]").send_keys("2")

Nationality= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/form/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[2]").click()

search= driver.find_element_by_id("btnSerchFlight1").click()


#Filterresult= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[2]/form/div[1]/div[1]/div").click()

# driver.close()


