#!/usr/bin/python3

from selenium import webdriver
import time

def InitEnv():
    import os

    pathNow = os.getcwd()
    chromeDriverPath=pathNow+"/dependence/chromedriver"

    opt=webdriver.ChromeOptions()
    opt.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"')

    driver=webdriver.Chrome(chromeDriverPath, chrome_options=opt)

    return driver

def CheckLoginSuccess(driver):
    while 1:
        try:
            data = driver.find_element_by_id('J_ItemList_s_725677994_0')
        except:
            time.sleep(1)
            continue
        else:
            data.click()
            break

def SubmitPay(sussFlag):
    while 1:
        try:
            sussFlag.click()
            aliPayLink = driver.find_element_by_xpath("//div[@class='sixDigitPassword']")
        except:
            continue
        else:
            break

def RepeatClickPay(driver):
    while 1:
        try:
            payLink = driver.find_element_by_id("J_Go")
            payLink.click()
            sussFlag = driver.find_element_by_xpath("//a[@class='go-btn']")
        except:
            continue
        else:
            SubmitPay(sussFlag)
            break

def ChooseDataAndpay(driver):
    while 1:
        try:
            #测试:J_CheckBox_3076108598773
            #茅台:J_CheckBox_2571400189756
            target = driver.find_element_by_xpath("//label[@for='J_CheckBox_3076108598773']")
        except:
            time.sleep(1)
            continue
        else:
            target.click()
            RepeatClickPay(driver)
            print("click")
            break

def GoToShopPage(driver):
    # 此处需要手动登陆 #
    driver.get('https://cart.tmall.com/cart.htm')
    CheckLoginSuccess(driver)

def DoRefreshPargTillTime(driver):
    import datetime

    diff = 0.1 #min
    targetTime = datetime.datetime.now()
    beforeSec=0
    while 1:
        if (targetTime.second % (diff * 60) == 0 and
            beforeSec != targetTime.second):
            beforeSec = targetTime.second
            driver.refresh()

        if (targetTime.hour == 19 and
            targetTime.minute==59 and
            targetTime.second==59):
            break
        targetTime = datetime.datetime.now()

def main():
    driver=InitEnv()
    GoToShopPage(driver)
    DoRefreshPargTillTime(driver)
    ChooseDataAndpay(driver)
    time.sleep(3600)
    driver.close()

main();