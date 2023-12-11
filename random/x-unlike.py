import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException as E

import time


account = 'username'
pwd = 'password'

#set the driver options
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)

#login twitter
url = 'https://twitter.com/i/flow/login'
driver.get(url)
time.sleep(2)

#fill login form
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='text']")))
username.clear() #incase there's already account name but it's not account u want to login
username.send_keys(account)
WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-ywje51 r-usiww2 r-13qz1uu r-2yi16 r-1qi8awa r-ymttw5 r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l"]'))).click()

password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
password.clear()
password.send_keys(pwd)
WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='LoginForm_Login_Button']"))).click()


time.sleep(2)

#go to likes page
likes_page = f'https://twitter.com/{account}/likes'
driver.get(likes_page)
time.sleep(3)

#scroll down likes page
scroll_count = 0
scroll_limit =2
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    time.sleep(2)
    
    try:
        elements = driver.find_elements(By.XPATH, '//div[@data-testid="unlike"]')
        for e in elements:
            try:
                e.click()
                time.sleep(3) 
            except:
                pass

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        if new_height == last_height:
            break
        
        last_height = new_height
        scroll_count += 1
    except E:
        continue

driver.quit()