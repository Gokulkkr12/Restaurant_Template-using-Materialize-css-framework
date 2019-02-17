import time
from selenium import webdriver
#My login credintials
user='16bcs219' 
pwd='0000'
#driver Path
driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe')
#Target Address
driver.get('http://portal.saveetha.com/deptweb/home/Login.aspx')
#finding the username and password fields by id
Uname=driver.find_element_by_id('m_loginid')
Uname.send_keys(user)
Pass=driver.find_element_by_id('m_password')
Pass.send_keys(pwd)
time.sleep(3)
#submit button
driver.find_element_by_xpath('//*[@id="m_signin"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="m_panel1"]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/a[1]').click()
time.sleep(3)
#Python code
pres=0
abse=0
for link in driver.find_elements_by_tag_name('a'):
    x=link.text
    if(x=='A'):
        abse+=1
print("No of periods you were absent")
print(abse)
print("No of days you were absent")
abse=abse/6
print(abse)
for link in driver.find_elements_by_tag_name('a'):
    x=link.text
    if(x=='/'):
        pres+=1
print("No of periods you were present")
print(pres)
print("NO of days you were present")
pres=pres/6
print(pres)
tot=pres+abse
per= (pres / tot)*100
print("Your Attendence percentage")
print(per)
driver.close()

