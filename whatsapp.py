from selenium import webdriver
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome(executable_path="C:/Users/Advitya/Downloads/c.exe")
driver.get('http://web.whatsapp.com')

print("Enter group or contact names saparated by commas\n")

name = input('enter names: ')
name = name.split(",")

msg = input("enter message: ")

input('press enter after entering QR code')
for i in name:
	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(i))
	user.click()
	msg_box = driver.find_element_by_class_name('_13mgZ')
	msg_box.send_keys(msg)
	driver.find_element_by_class_name('_3M-N-').click()
