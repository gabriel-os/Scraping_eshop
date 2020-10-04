import time
import platform
import pandas as pd
import numpy as np

from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

todayBar = date.today().strftime("%d/%m/%Y")
todayTrace = date.today().strftime("%d-%m-%Y")

opt = webdriver.ChromeOptions()

if platform.system() == "Windows":
    opt.add_argument("--start-maximized")
else:
    opt.add_argument("--kiosk")

browser = webdriver.Chrome(options=opt)

browser.get('https://eshop-prices.com/prices')

time.sleep(1)

print(len(browser.find_elements_by_class_name('_3MHjalmXoOuOl6ai2zcgJ3')))

height = browser.execute_script("return document.body.scrollHeight")
print(height)

actions = ActionChains(browser)

actions.perform()
ls_games = []
for j in range(1, 300, 1):
    time.sleep(0.3)
    for row in browser.find_elements_by_class_name('b7zrtp2_l5h-0vlrBHmf3'):
        ls_games.append(row.text.splitlines())
    actions.perform()
    elem = browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)

ls_columns = ['name_game', 'ARG',
              ' AUT',
              ' AUS',
              ' BEL',
              ' BGR',
              ' BRA',
              ' CAN',
              ' CHE',
              ' CHL',
              ' COL',
              ' CYP',
              ' CZE',
              ' DEU',
              ' DNK',
              ' EST',
              ' ESP',
              ' FIN',
              ' FRA',
              ' GBR',
              ' GRC',
              ' HKG',
              ' HRV',
              ' HUN',
              ' IRL',
              ' ISR',
              ' ITA',
              ' JPN',
              ' KOR',
              ' LTU',
              ' LUX',
              ' LVA',
              ' MLT',
              ' MEX',
              ' NLD',
              ' NOR',
              ' NZL',
              ' PER',
              ' POL',
              ' PRT',
              ' ROU',
              ' RUS',
              ' SWE',
              ' SVN',
              ' SVK',
              ' USA',
              ' ZAF']
df = pd.DataFrame(data=ls_games, columns=ls_columns)

df.drop_duplicates(subset="name_game", keep='first', inplace=True)

df.reset_index(drop=True, inplace=True)

df['date_extract'] = todayBar


df.to_csv('../db/value_' + todayTrace + '.csv', encoding = 'utf-8-sig')

browser.get('https://eshop-prices.com/prices?currency=BRL')
time.sleep(1)
cash_price = browser.execute_script("return window.currencies")
df2 = pd.DataFrame(data=cash_price)

df2.to_csv('../db/currency_' + todayTrace + '.csv', encoding = 'utf-8-sig')

browser.quit()