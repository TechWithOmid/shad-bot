import os
from selenium import webdriver

PATH = "/usr/bin/chromedriver"
driver = webdriver.Chrome(PATH)
driver.set_window_position(-10000,0)
driver.get("https://web.shad.ir")


def login():
    os.system('clear')
    user_phone_number = input('Enter Your Phone Number: ') # user phone number
    number_field = driver.find_element_by_xpath("/html//app-root/tab-login/div[@class='login_page_wrap']//form[@name='mySendCodeForm']//input[@name='phone_number']") # number input field in login page
    number_field.clear() # clear number field
    number_field.send_keys(user_phone_number) # input number to number field
    
    driver.find_element_by_xpath("/html/body//app-root/tab-login/div[@class='login_page_wrap']//span[.='بعدی']").click()
    number_check = input('Are you sure (y/n): ')
    if number_check == 'y':
        driver.find_element_by_xpath("/html//app-root/app-modal-container//app-modal-view/div//div[@class='modal-content modal-content-animated']/app-confirm-custom//span[.='بله']").click()
        login_confirm()
    else:
        driver.find_element_by_xpath("/html//app-root/app-modal-container//app-modal-view/div//div[@class='modal-content modal-content-animated']/app-confirm-custom//span[.='لغو']").click()
        login()


def login_confirm():
    confirm_code = input('enter the code that we send: ') # Shad login confirm code
    confirm_field = driver.find_element_by_xpath("/html//app-root/tab-login/div[@class='login_page_wrap']//form[@name='myLoginForm']//input[@name='phone_code']") # the confirm code input field
    confirm_field.clear()
    confirm_field.send_keys(confirm_code)

login()
