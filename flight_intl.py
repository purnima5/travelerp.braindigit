from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
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

driver.implicitly_wait(5)
International= driver.find_element_by_xpath("/html/body/div/div[1]/div/ul/li[2]/ul/li[3]").click()

From = driver.find_element_by_name("FromLocation").click()

forselection= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/div[1]/form/div/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[3]/ul/li[10]/div").click()

To = driver.find_element_by_name("ToLocation").click()
Toselectthelocation= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/div[1]/form/div/div/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div[3]/ul/li[27]").click()

driver.implicitly_wait(5)
driver.find_element_by_name("DepartureDate").click()
Ddate= driver.find_element_by_xpath("/html/body/div[4]/div[1]/table/tbody/tr[4]/td[6]").click()

driver.implicitly_wait(5)

passenger= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/div[1]/form/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/input[1]").click()

# adult= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/div[1]/form/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[1]/div[3]/div/div[1]/div[2]/button[2]").click()

baby= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/div[1]/form/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[1]/div[3]/div/div[2]/div[2]/button[2]").click()
#
# infant= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]aq/div[1]/div[1]/form/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[1]/div[3]/div/div[3]/div[2]/button[2]").click()

fclass= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/div[1]/form/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[3]/div/div[3]").click()

Nationality= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/div[1]/form/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/select/option[6]").click()

flexidate= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/div[1]/form/div/div/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/select/option[3]").click()

search= driver.find_element_by_id("btnSerchFlight").click()

driver.implicitly_wait(20)
#nowsedndingmail #no permission can't work
# sendqueote= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/div[2]/div[1]/div[3]/div/div/div[2]/div/div[2]/div/div[2]/button[1]").click()
# sendmail= driver.find_element_by_id("btnSend").click()
#
# driver.implicitly_wait(20)
# mailinput= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[3]/div[2]/div/div[1]/div[2]/div[1]/div[2]/input").send_keys("devilgaming79@gmail.com")
# sendqutoe= driver.find_element_by_id("sendPriceQuote").click()
#
# #modifying price
# #sendqueote= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/div[2]/div[1]/div[3]/div/div/div[2]/div/div[2]/div/div[2]/button[1]").click()
# modifyprice= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[3]/div[1]/div[2]/button[2]").click()
# inputtax= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[2]/input").send_keys("1350")
# basefare= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div[2]/input").send_keys("2333")
# discount= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/input").send_keys("12")
# apply= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[3]/div[2]/div/div[2]/div[3]/div/button").click()

driver.implicitly_wait(20)
booknow= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/div[2]/div[1]/div[3]/div/div/div[2]/div/div[2]/div/div[2]/button[2]").click()

driver.implicitly_wait(30)
#filling form slcContTit
# titles= Select(driver.find_element_by_xpath('//*[@id="slcContTit"]'))
# titles.select_by_value("M")

firstname= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[2]/div[4]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[2]/input").send_keys("Purnima sah")
middlename= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[2]/div[4]/div[1]/div[1]/div[1]/div/div[2]/div[3]/div[2]/input").send_keys("kri")
lastname= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[2]/div[4]/div[1]/div[1]/div[1]/div/div[2]/div[4]/div[2]/input").send_keys("sah")
contact= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[2]/div[4]/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/input").send_keys(9817836063)
emaill= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[2]/div[4]/div[1]/div[1]/div[1]/div/div[3]/div[2]/div[2]/input").send_keys("purnima.sah2345@gmail.com")
checkbox= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[2]/div[4]/div[1]/div[1]/div[1]/div/div[4]/div/div/input").click()
DOB= driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[2]/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[4]/div[2]/input").send_keys("2010-01-05")