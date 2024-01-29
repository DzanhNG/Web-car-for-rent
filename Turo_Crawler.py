from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import datetime
import tkinter as tk
from tkinter import messagebox


def call_Tutor(url):
    print(' Initialise the webdriver')
    firefox_options = Options()
    firefox_options.headless = True
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(url)
    actions = ActionChains(driver)

    sleep(20) 

    ##Close Accept cookie:
    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/button[2]").click()
    sleep(1)

    List_Vehicle = []

    Pathx_1= "/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/a/div/div[2]/div[1]/div[1]/div[1]"
    List_Vehicle.append(driver.find_element(By.XPATH,Pathx_1).text)
    sleep(1)

    Pathx_2= "/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div/a/div/div[2]/div[1]/div[1]/div[1]"
    List_Vehicle.append(driver.find_element(By.XPATH,Pathx_2).text)
    sleep(1)

    Pathx_Step1 = '/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[1]'
    driver.find_element(By.XPATH,Pathx_Step1).click()
    sleep(1)
    print('Click')

    actions.send_keys(Keys.PAGE_DOWN).perform()
    print('PAGE_DOWN')

    Pathx_3= "/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div[3]/div/div/a/div/div[2]/div[1]/div[1]/div[1]"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Pathx_3)))
    List_Vehicle.append(driver.find_element(By.XPATH,Pathx_3).text)
    sleep(1)

    Pathx_4= "/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div[2]/div/a/div/div[2]/div[1]/div[1]/div[1]"
    List_Vehicle.append(driver.find_element(By.XPATH,Pathx_4).text)
    sleep(1)

    Pathx_5 = '/html/body/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div/a/div/div[2]/div[1]/div[1]/div[1]'
    List_Vehicle.append(driver.find_element(By.XPATH,Pathx_5).text)
    sleep(1)

    flag = True
    while flag:
        try:
            ###GET TEXT
            print('Render the dynamic content to static HTML')
            html = driver.page_source       
            print(' Parse the static HTML')
            soup = BeautifulSoup(html, "html.parser")
            divs = soup.find_all("div", {"class": "css-hvsi0k-StyledText"})
            print(divs)
            ###

            if len(divs) == 1:
                flag = False
            else:
                for item in divs:
                    List_Vehicle.append(item.text)
            actions.send_keys(Keys.PAGE_DOWN).perform()
            print('PAGE_DOWN')
        except:
            print('False > Exit')
            flag = False
    # Close the webdriver
    driver.close()

    mylist = list(dict.fromkeys(List_Vehicle))
    print('List_Vehicle: ', mylist)

    list_return = []
    for ymme in mylist:
        year = ymme[-4:]
        Make = ymme.split(" ",1)[0]
        Model = ymme.split(" ",1)[1][:-5]
        list_return.append([year, Make, Model])

    # Define column names
    columns = ['Year', 'Make', 'Model']
    # Create DataFrame
    df = pd.DataFrame(list_return, columns=columns)
    return df


###MAIN CODE####
month_dict = {'01':'Jan', '02':'Feb', '03':'Mar', '04':'Apr', '05':'May', '06':'Jun','07':'Jul', '08':'Aug', '09':'Sep', '10':'Oct', '11':'Nov', '12':'Dec'}

Day_Start = '01'
Month_Start = '02'
Year_Start = '2024'
Start = 'startDate=' +str(Month_Start) + '%2F' + str(Day_Start) +   '%2F' + str(Year_Start)  ###  month%2F   day%2F    year
Savetime_start = month_dict.get(Month_Start) + Day_Start + Year_Start

Day_End= '28'
Month_End = '02'
Year_End = '2024'
End = 'endDate=' +str(Month_End) + '%2F' + str(Day_End)+   '%2F' + str(Year_End)   ###  month%2F   day%2F    year
Savetime_end = month_dict.get(Month_End) + Day_End + Year_End

Savetime = '_' + Savetime_start + '_' + Savetime_end

part1 = 'https://turo.com/us/en/search?country=US&defaultZoomLevel=13&deliveryLocationType=city&'
part2 = '&endTime=12%3A00&isMapSearch=false&itemsPerPage=200&latitude=33.6832497&location=Irvine%2C%20CA%2092614%2C%20USA&locationType=CITY&longitude=-117.83407349999999&pickupType=ALL&placeId=ChIJGWp61inc3IARB84fEAnUP0U&region=CA&sortType=RELEVANCE&'
part3 = '&startTime=11%3A00&useDefaultMaximumDistance=true'

url = str(part1) + End + part2 + Start + part3
print(url)
df_return = call_Tutor(url)
df_return.to_excel('Output data/Tutor_'+ Savetime + '.xlsx', index=False)
