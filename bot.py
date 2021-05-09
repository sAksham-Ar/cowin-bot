from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(os.getcwd()+r"\chromedriver.exe")
driver.get("https://selfregistration.cowin.gov.in/")
input("done?")
i=0
while 1:
    links=driver.find_elements_by_tag_name("a")
    appointments=[link for link in links if link.get_attribute("href")!=None and "appointment" in link.get_attribute("href")]
    available=[appointment for appointment in appointments if appointment.text not in ["Booked","NA",""] and "May" not in appointment.text]
    if len(available)>0:
        available[0].send_keys(Keys.ENTER)
        available[0].click()
        c=input('Done?')
        if c=='y':
            exit()
    if i%2==0:
        try:
            right=driver.find_element_by_class_name('right')
            right.click()
        except:
            input("done?")
    else:
        try:
            left=driver.find_element_by_class_name('left')
            left.click()
        except:
            input("done?")
    i+=1
    sleep(2)
    
