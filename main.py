import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# TODO
# make form presntaion availble
# add menu
# build cli interface

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
    select_chat()


def select_chat():
    chat_id = input('Enter chat id from top: ')
    chat_path = "/html//app-root//rb-chats/div[@class='im_dialogs_col_wrap noselect']/div[@class='im_dialogs_col']/div/div[@class='im_dialogs_scrollable_wrap nano-content']/ul[2]/li["+chat_id+"]//div[@class='im_dialog_peer']"
    driver.find_element_by_xpath(chat_path).click()
    send_present_msg()


def send_present_msg():
    send_hour = input('Enter the hour you want to send message: ') # ask for time that user want to send message
    send_min = input('Enter the min you want to send message: ')
    user_message = input('Enter the message you want to send: ') # message user want to send
    
    while True:
        current_time = datetime.now()
        current_hour = current_time.strftime('%H')
        current_min = current_time.strftime('%M')
        current_sec = current_time.strftime('%S')

        print(f"{current_hour} : {current_min} : {current_sec}") # print current time
        time.sleep(0.5)
        os.system('clear')

        if current_hour == send_hour and current_min == send_min:
            message_box = driver.find_element_by_xpath("/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[3]/div/div/div/form/div[3]/div[5]") # textarea path for input text

            message_box.clear()
            message_box.send_keys(user_message)
            message_box.send_keys(Keys.ENTER)

            # driver.find_element_by_xpath("//html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[2]/tab-conversation/div/div[3]/div/div/div/form/div[4]/button").click() # send message button path

            time.sleep(4)
            print('Message send.')
            select_chat()
    print('send_present_msg done')
            

login()
