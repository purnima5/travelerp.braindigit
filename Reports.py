from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r"C:\Users\Purnima Sah\PycharmProjects\firstseleniumtest\Driver\chromedriver.exe")

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://travelerp.braindigit.com/")
email_ele = driver.find_element_by_name("Email").send_keys("sgodar34@yopmail.com")
pass_ele = driver.find_element_by_name("Password")
#email_ele.send_keys("sgodar34@yopmail.com")
pass_ele.send_keys("000000")
driver.find_element_by_tag_name("button").click()
report = driver.find_element_by_xpath("html/body/div/div[1]/div/ul/li[8]/a").click()
bookingreport = driver.find_element_by_xpath("/html/body/div/div[1]/div/ul/li[8]/ul/li[1]").click()
#chart
#chart=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[2]/div[1]/button[1]").click()
driver.find_element_by_id("btnFilterFlight").click()
#data = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[2]/div[1]/button[2]").click()
#Exportsheet
#exportxl= driver.find_element_by_id("exportToExcel").click()
#advsrch = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[5]/div[1]/div/div[1]").click()
