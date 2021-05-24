"""
Shad Bot Version 1.1

Blog: TechWithOmid.ir
Email: TechWithOmid.gmail.com

feel free to use this script and report bug or add features
"""
import os
import sys
import re
import platform
import time
import pyfiglet
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# browser setting
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_window_position(-10000, 0)
driver.get("https://web.shad.ir")  # shad url


def clear():
    """
    clear the output depends on os
    """
    s = platform.system()
    if s == "Linux":
        os.system('clear')
    if s == "Windows":
        os.system('cls')


def main():
    """
    Script start point
    """
    clear()
    start_banner = pyfiglet.figlet_format("Shad Bot!!")
    print(start_banner)
    input("Press any key to continue...")
    login()


def login():
    """
    login to shad web application
    """
    clear()
    print(pyfiglet.figlet_format("Shad Bot!!"))  # print banner

    try:
        user_phone_number = input('Enter Your Phone Number: ')  # user phone number
        phone_regex = re.compile('^(\\+98|0)?9\\d{9}$') # regex for validate phone number
        if re.fullmatch(phone_regex, user_phone_number):

             number_field = driver.find_element_by_xpath("/html//app-root/tab-login/div[@class='login_page_wrap']//form["
             "@name='mySendCodeForm']//input[@name='phone_number']")  # number input field in login page
             number_field.clear()  # clear number field
             number_field.send_keys(user_phone_number)  # input number to number field

             driver.find_element_by_xpath("/html/body//app-root/tab-login/div[@class='login_page_wrap']//span[.='بعدی']").click()
             number_check = input(f"Are you sure you want to login with '{user_phone_number}' (y/n): ")
             if number_check == 'y':
                 driver.find_element_by_xpath("/html//app-root/app-modal-container//app-modal-view/div//div["
                                              "@class='modal-content modal-content-animated']/app-confirm-custom//span["
                                              ".='بله']").click()
                 login_confirm()
             else:
                 driver.find_element_by_xpath("/html//app-root/app-modal-container//app-modal-view/div//div["
                                              "@class='modal-content modal-content-animated']/app-confirm-custom//span["
                                              ".='لغو']").click()
                 login()
        else:
            raise ValueError
    except ValueError:
        print('Phone Number Is Not Valid, try again.')
        time.sleep(2)
        login()


def login_confirm():
    """
    confirm the login by sending SMS
    """
    clear()
    print(pyfiglet.figlet_format("Shad Bot!!"))  # print banner

    confirm_code = input('enter the code that we send: ')  # Shad login confirm code
    confirm_field = driver.find_element_by_xpath("/html//app-root/tab-login/div[@class='login_page_wrap']//form["
                                                 "@name='myLoginForm']//input[@name='phone_code']")  # the confirm
    # code input field
    confirm_field.clear()
    confirm_field.send_keys(confirm_code)
    select_chat()


def select_chat():
    """
    select chat and time for sending message
    """
    clear()
    print(pyfiglet.figlet_format("Shad Bot!!"))  # print banner

    chat_id = [] # store the chat id in list
    class_time = [] # store class times in list
    class_number = int(input('Eneter how much class do you have: ')) # ask for how many time user has class
    for c_id in range(class_number):
        chat_id.append(input(f'{c_id+1} chat id: '))
        class_time.append(input('time: ').split(':'))
        print('*'*30)

    check_time(class_time, chat_id, class_number)


def check_time(class_time, chat_id, class_number):
    """
    check for time and call send_present_msg()
    """
    user_message = input('Enter the message you want to send: ')  # message user want to send

    while True:
        current_time = datetime.now()
        current_hour = current_time.strftime('%H')
        current_min = current_time.strftime('%M')
        current_sec = current_time.strftime('%S')

        print(f'{current_hour} : {current_min} : {current_sec}')
        time.sleep(0.5)
        clear()

        for i in range(class_number):
            if class_time[i][0] == current_hour and class_time[i][1] == current_min:
                print('yay i start')
                send_present_msg(chat_id[i], user_message)
                time.sleep(60)


def send_present_msg(chat_id, user_message ):
    """
    send message to chat
    """
    clear()
    print(pyfiglet.figlet_format("Shad Bot!!"))  # print banner

    message_box_path = "/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[" \
                       "2]/tab-conversation/div/div[3]/div/div/div/form/div[3]/div[5]"  # textarea path for input text

    chat_path = "/html//app-root//rb-chats/div[@class='im_dialogs_col_wrap noselect']/div[" \
                      "@class='im_dialogs_col']/div/div[@class='im_dialogs_scrollable_wrap nano-content']/ul[2]/li[" \
                      "" + chat_id + "]//div[@class='im_dialog_peer'] "

    driver.find_element_by_xpath(chat_path).click() # click on chat
    message_box = driver.find_element_by_xpath(message_box_path) # find chat box
    message_box.clear()
    message_box.send_keys(user_message) # insert message to message box
    message_box.send_keys(Keys.ENTER) # hit enter and send message
    print("yay message send :)")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        driver.quite()
        clear()
        print("May We Meet Again :)")
        time.sleep(2)

