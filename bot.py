from selenium import webdriver
import os
from time import sleep

driver=webdriver.Chrome(os.getcwd()+r"\chromedriver.exe")
driver.get("https://selfregistration.cowin.gov.in/");
input("done?")
i=0
while 1:
    links=driver.find_elements_by_tag_name("a")
    appointments=[link for link in links if link.get_attribute("href")!=None and "appointment" in link.get_attribute("href")]
    available=[appointment for appointment in appointments if appointment.text not in ["Booked","NA",""] and "May" not in appointment.text]
    if len(available)>0:
        for a in available:
            a.click()
            c=input()
            if c=='y':
                exit()
    if i%2==0:
        right=driver.find_element_by_class_name('right')
        right.click()
    else:
        left=driver.find_element_by_class_name('left')
        left.click()
    i+=1
    sleep(2)
    
