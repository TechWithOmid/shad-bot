"""
Shad Bot Version 1.0

Blog: TechWithOmid.ir
Email: TechWithOmid.gmail.com

feel free to use this script and report bug and or feature
"""
import os
import sys
import platform
import time
import pyfiglet
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# TODO
# make multiple class selection available => Done!
# clear the output depends on os (clear for linux, cls for windows)  => Done!
# make select_chat cleaner
# make send_present_msg cleaner
# define check time
# make the code better and cleaner

# browser setting
PATH = "/usr/bin/chromedriver"
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')  # ignore chrome ssl error
options.add_argument('--ignore-certificate-errors')  # ignore chrome certification error
driver = webdriver.Chrome(PATH, options=options)  # chrome driver settings
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
    user_param = input("Press Enter to continue ")

    if user_param == "":
        login()
    else:
        sys.exit()  # exit the program


def login():
    clear()
    print(pyfiglet.figlet_format("Shad Bot!!"))  # print banner

    user_phone_number = input('Enter Your Phone Number: ')  # user phone number
    number_field = driver.find_element_by_xpath("/html//app-root/tab-login/div[@class='login_page_wrap']//form["
                                                "@name='mySendCodeForm']//input[@name='phone_number']")  # number
    # input field in login page
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


def login_confirm():
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
    clear()
    print(pyfiglet.figlet_format("Shad Bot!!"))  # print banner

    first_chat_id = input('Enter 1st chat id from top: ')
    first_class_time = input(
        'Enter the 1st class time(e.g. 12:10): ').split(':')  # time that user want to send message

    second_chat_id = input('Enter 2nd chat id from top: ')
    second_class_time = input(
        'Enter the 2nd class time(e.g. 12:30): ').split(':')  # used split to save the hour and min in a list

    third_chat_id = input('Enter 3rd chat id from top: ')
    third_class_time = input('Enter the 3rd class time(e.g. 12:30): ').split(':')

    fourth_chat_id = input('Enter 4th chat id from top: ')
    fourth_class_time = input('Enter the 4th class time(e.g. 12:30): ').split(':')

    first_chat_path = "/html//app-root//rb-chats/div[@class='im_dialogs_col_wrap noselect']/div[" \
                      "@class='im_dialogs_col']/div/div[@class='im_dialogs_scrollable_wrap nano-content']/ul[2]/li[" \
                      "" + first_chat_id + "]//div[@class='im_dialog_peer'] "

    second_chat_path = "/html//app-root//rb-chats/div[@class='im_dialogs_col_wrap noselect']/div[" \
                       "@class='im_dialogs_col']/div/div[@class='im_dialogs_scrollable_wrap nano-content']/ul[2]/li[" \
                       "" + second_chat_id + "]//div[@class='im_dialog_peer'] "

    third_chat_path = "/html//app-root//rb-chats/div[@class='im_dialogs_col_wrap noselect']/div[" \
                      "@class='im_dialogs_col']/div/div[@class='im_dialogs_scrollable_wrap nano-content']/ul[2]/li[" \
                      "" + third_chat_id + "]//div[@class='im_dialog_peer'] "

    fourth_chat_path = "/html//app-root//rb-chats/div[@class='im_dialogs_col_wrap noselect']/div[" \
                       "@class='im_dialogs_col']/div/div[@class='im_dialogs_scrollable_wrap nano-content']/ul[2]/li[" \
                       "" + fourth_chat_id + "]//div[@class='im_dialog_peer'] "
    send_present_msg(first_chat_path, second_chat_path, first_class_time, second_class_time, third_class_time,
                     fourth_class_time, third_chat_path, fourth_chat_path)


def send_present_msg(first_chat_path, second_chat_path, first_class_time, second_class_time, third_class_time,
                     fourth_class_time, third_chat_path, fourth_chat_path):
    clear()
    print(pyfiglet.figlet_format("Shad Bot!!"))  # print banner

    user_message = input('Enter the message you want to send: ')  # message user want to send
    message_box_path = "/html/body/div[1]/app-root/span/div[1]/div/div/app-tab-container/app-tab-view/div[" \
                       "2]/tab-conversation/div/div[3]/div/div/div/form/div[3]/div[5]"  # textarea path for input text

    while True:
        current_time = datetime.now()
        current_hour = current_time.strftime('%H')
        current_min = current_time.strftime('%M')
        current_sec = current_time.strftime('%S')

        print(pyfiglet.figlet_format("Shad Bot!!"))  # print banner
        print(f"{current_hour} : {current_min} : {current_sec}")  # print current time
        time.sleep(0.5)
        clear()

        if first_class_time[0] == current_hour and first_class_time[1] == current_min:
            driver.find_element_by_xpath(first_chat_path).click()
            message_box = driver.find_element_by_xpath(message_box_path)
            message_box.clear()
            message_box.send_keys(user_message)
            message_box.send_keys(Keys.ENTER)
            time.sleep(60)

        if second_class_time[0] == current_hour and second_class_time[1] == current_min:
            driver.find_element_by_xpath(second_chat_path).click()
            message_box = driver.find_element_by_xpath(message_box_path)
            message_box.clear()
            message_box.send_keys(user_message)
            message_box.send_keys(Keys.ENTER)
            time.sleep(60)

        if third_class_time[0] == current_hour and third_class_time[1] == current_min:
            driver.find_element_by_xpath(third_chat_path).click()
            message_box = driver.find_element_by_xpath(message_box_path)
            message_box.clear()
            message_box.send_keys(user_message)
            message_box.send_keys(Keys.ENTER)
            time.sleep(60)

        if fourth_class_time[0] == current_hour and fourth_class_time[1] == current_min:
            driver.find_element_by_xpath(fourth_chat_path).click()
            message_box = driver.find_element_by_xpath(message_box_path)
            message_box.clear()
            message_box.send_keys(user_message)
            message_box.send_keys(Keys.ENTER)
            break


main()
