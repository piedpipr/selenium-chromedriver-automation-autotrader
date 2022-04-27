# Salenium WebDriver Autotrader for Binary Options of CG

import selenium
from selenium import webdriver
# from getpass import getpass
# import pyautogui
import time

# create webdriver object
PATH = "./chromedriver"
driver = webdriver.Chrome(PATH)

# username = input("Enter your username: ")
# password = getpass("Enter your password: ")
username = 'WEB_SITE_USERNAME'
password = 'WEB_SITE_PASSWORD'

# previous_price = 0.1

def Login():
    driver.get("LOGIN_PAGE_URL_i_ommited_for_security")
    time.sleep(3)
    country_seclector = driver.find_element_by_xpath(
        "/html/body/div/article/main/section[2]/div[1]/i").click()
    time.sleep(2)
    code_selector = driver.find_element_by_xpath(
        "/html/body/div/article/main/section[2]/div[1]/article/section/main/div[2]/ul/li[17]/div[2]").click()
    username_field = driver.find_element_by_xpath(
        "/html/body/div/article/main/section[2]/div[1]/input")
    username_field.send_keys(username)
    password_field = driver.find_element_by_xpath(
        "/html/body/div/article/main/section[2]/div[2]/input")
    password_field.send_keys(password)
    login_button = driver.find_element_by_xpath(
        "/html/body/div/article/main/section[3]/button").click()
    time.sleep(3)
    # SELECT BETWEEN REAL OR DEMO SIMULATION
    
    # REAL TRADE START
    # trade_tab = driver.find_element_by_xpath(
    #     "/html/body/div/article/footer/nav/a[2]")
    # trade_tab.click()
    # time.sleep(5)
    # one_min_trade = driver.find_element_by_xpath(
    #     "/html/body/div/article[1]/main/section[2]/ul/li[2]")
    # one_min_trade.click()
    # REAL TRADE END

    # DEMO TRADE(Simulation)
    home_tab = driver.find_element_by_xpath(
        "/html/body/div/article/footer/nav/a[1]").click()
    time.sleep(3)
    simulation = driver.find_element_by_xpath(
        "/html/body/div/article/main/section[4]/ul/li[2]/ul/li/div").click()
    time.sleep(3)
    one_min_trade = driver.find_element_by_xpath(
        "/html/body/div/article[1]/main/section[2]/ul/li[2]")
    one_min_trade.click()
    time.sleep(5)
    # DEMO END
    

def Time_Remaining():
    current_time = driver.find_element_by_xpath(
        "/html/body/div/article[1]/main/section[5]/header[3]/div[3]/span").get_attribute('innerHTML')
    time_sliced = current_time[3:]
    time_int = int(time_sliced)
    return time_int


def Page_Refresh():
    driver.refresh()
    time.sleep(4)
    one_min_trade = driver.find_element_by_xpath(
        "/html/body/div/article[1]/main/section[2]/ul/li[2]")
    one_min_trade.click()
    time.sleep(4)
    # refresh = driver.find_element_by_xpath(
    #     "/html/body/div/article[1]/main/section[5]/header[2]/div[3]").click()
    #time.sleep(2)


def Check_Status():
    Page_Refresh()
    records = driver.find_element_by_xpath(
        "/html/body/div/article[1]/main/section[5]/header[1]/div[3]")
    if records:
        records.click()
        time.sleep(3)
        myrecords = driver.find_element_by_xpath(
            "/html/body/div/article[4]/section/main/div/div[1]/header/div/b[2]")
        if myrecords:
            myrecords.click()
            time.sleep(3)
            last_record = driver.find_element_by_xpath(
                "/html/body/div/article[4]/section/main/div/div[2]/main/section[2]/ul/li[1]")
            if last_record:
                last_record.click()
                time.sleep(2)
                record_color = driver.find_element_by_xpath(
                    "/html/body/div/article[4]/section/main/div/div[2]/main/section[2]/ul/li[1]/div").get_attribute("style")
                # Check last pricwe
                # last_transection = driver.find_element_by_xpath(
                #     "/html/body/div/article[4]/section/main/div/div[2]/main/section[2]/ul/li[1]/div[2]/ul/li[3]/div/span[2]").get_attribute('innerHTML')
                # previous_price = float(last_transection)
                close_records = driver.find_element_by_xpath(
                    "/html/body/div/article[4]/section/footer/div")
                close_records.click()
                if record_color == "color: red;":
                    return 'red'
                elif record_color == "color: rgb(76, 168, 75);":
                    return 'green'
                else:
                    time.sleep(3)
                    Check_Status()
            else:
                Check_Status()
        else:
            Check_Status()
    else:
        Check_Status()

def rise_start():
    rise_button = driver.find_element_by_xpath(
        "/html/body/div/article[1]/main/section[6]/button[1]").click()
    time.sleep(2)
    price_input = driver.find_element_by_xpath(
        "/html/body/div/article[4]/section/main/section/section/main/section[1]/header[4]/div/div/input")
    price_input.clear()
    price_input.send_keys('0.1')
    confirm_button = driver.find_element_by_xpath(
        "/html/body/div/article[4]/section/main/section/section/main/section[2]/button[2]").click()
    time.sleep(2)
    transaction_button = driver.find_element_by_xpath(
        "/html/body/div/article[5]/section/footer/button[2]").click()
    time.sleep(2)

def rise_double():
    global previous_price
    double_price = previous_price * 2
    previous_price = double_price
    rise_button = driver.find_element_by_xpath(
        "/html/body/div/article[1]/main/section[6]/button[1]").click()
    time.sleep(2)
    price_input = driver.find_element_by_xpath(
        "/html/body/div/article[4]/section/main/section/section/main/section[1]/header[4]/div/div/input")
    price_input.clear()
    price_input.send_keys(double_price)
    confirm_button = driver.find_element_by_xpath(
        "/html/body/div/article[4]/section/main/section/section/main/section[2]/button[2]").click()
    time.sleep(2)
    transaction_button = driver.find_element_by_xpath(
        "/html/body/div/article[5]/section/footer/button[2]").click()
    time.sleep(2)
    return previous_price


def fall_start():
    fall_button = driver.find_element_by_xpath(
        "/html/body/div/article[1]/main/section[6]/button[2]").click()
    time.sleep(2)
    price_input = driver.find_element_by_xpath(
        "/html/body/div/article[4]/section/main/section/section/main/section[1]/header[4]/div/div/input")
    price_input.clear()
    price_input.send_keys('0.1')
    confirm_button = driver.find_element_by_xpath(
        "/html/body/div/article[4]/section/main/section/section/main/section[2]/button[2]").click()
    time.sleep(2)
    transaction_button = driver.find_element_by_xpath(
        "/html/body/div/article[5]/section/footer/button[2]").click()
    time.sleep(2)

def fall_double():
    global previous_price
    double_price = previous_price * 2
    previous_price = double_price
    fall_button = driver.find_element_by_xpath(
        "/html/body/div/article[1]/main/section[6]/button[2]").click()
    time.sleep(2)
    price_input = driver.find_element_by_xpath(
        "/html/body/div/article[4]/section/main/section/section/main/section[1]/header[4]/div/div/input")
    price_input.clear()
    price_input.send_keys(double_price)
    confirm_button = driver.find_element_by_xpath(
        "/html/body/div/article[4]/section/main/section/section/main/section[2]/button[2]").click()
    time.sleep(2)
    transaction_button = driver.find_element_by_xpath(
        "/html/body/div/article[5]/section/footer/button[2]").click()
    time.sleep(2)
    return previous_price


def Rise():
    global previous_price
    previous_price = 0.1

    time_remaining = Time_Remaining()
    if time_remaining > 17 and time_remaining < 50:
        rise_start()
        time_remaining = Time_Remaining()
        time.sleep(time_remaining - 5)
        check_status = Check_Status()
        if check_status == 'green':
            Rise()
        elif check_status == 'red':
            def rise_double_recursive():
                pre_price = rise_double()
                global previous_price
                previous_price = pre_price
                time_remaining = Time_Remaining()
                time.sleep(time_remaining - 5)
                check_status = Check_Status()
                if check_status == 'green':
                    Rise()
                elif check_status == 'red':
                    rise_double_recursive()
            rise_double_recursive()

    elif time_remaining > 50:
        time.sleep(time_remaining - 51)
        Rise()
    else:
        time.sleep(time_remaining + 10)
        Rise()


def Fall():
    global previous_price
    previous_price = 0.1

    time_remaining = Time_Remaining()
    if time_remaining > 17 and time_remaining < 50:
        fall_start()
        time_remaining = Time_Remaining()
        time.sleep(time_remaining - 5)
        check_status = Check_Status()
        if check_status == 'green':
            Fall()
        elif check_status == 'red':
            def fall_double_recursive():
                pre_price = fall_double()
                global previous_price
                previous_price = pre_price
                time_remaining = Time_Remaining()
                time.sleep(time_remaining - 5)
                check_status = Check_Status()
                if check_status == 'green':
                    Fall()
                elif check_status == 'red':
                    fall_double_recursive()
            fall_double_recursive()

    elif time_remaining > 50:
        time.sleep(time_remaining - 51)
        Fall()
    else:
        time.sleep(time_remaining + 10)
        Fall()


def Alternate():
    global previous_price
    previous_price = 0.1
    
    time_remaining = Time_Remaining()
    if time_remaining > 17 and time_remaining < 50:
        rise_start()
        time_remaining = Time_Remaining()
        time.sleep(time_remaining - 5)
        check_status = Check_Status()
        if check_status == 'green':
            Alternate()
        elif check_status == 'red':
            def alternate_double_recursive():
                pre_price = fall_double()
                global previous_price
                previous_price = pre_price
                time_remaining = Time_Remaining()
                time.sleep(time_remaining - 5)
                check_status = Check_Status()
                if check_status == 'green':
                    Alternate()
                elif check_status == 'red':
                    pre_price = rise_double()
                    previous_price = pre_price
                    time_remaining = Time_Remaining()
                    time.sleep(time_remaining - 5)
                    check_status = Check_Status()
                    if check_status == 'green':
                        Alternate()
                    elif check_status == 'red':
                        alternate_double_recursive()
            alternate_double_recursive()

    elif time_remaining > 50:
        time.sleep(time_remaining - 51)
        Alternate()
    else:
        time.sleep(time_remaining + 10)
        Alternate()

# Check_Status()
Login()
# Rise()
# Fall()
Alternate()
