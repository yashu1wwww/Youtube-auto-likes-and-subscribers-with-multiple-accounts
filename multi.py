import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

email = 'dontknow@gmail.com\n'    #enter mail
password = 'putpass@#$1\n'         #enter pass

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
url = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
wait.until(EC.visibility_of_element_located((By.NAME,'password'))).send_keys(password)
time.sleep(5)

#upto the above the codes credits goes to https://github.com/xtekky these man

with open("urls.txt") as f: #change url in text file
    for url in f:
        driver.get(url)
        
 time.sleep(8) #i video dont have ads then change 8 to 3 or 4       
driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()       
driver.find_element_by_css_selector('yt-icon.style-scope.ytd-toggle-button-renderer').click()
time.sleep(3)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > tp-yt-paper-button > yt-formatted-string').click()
driver.close()


import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

email = 'nonunkown@gmail.com \n'   #enter mail
password = 'putpass\n'             #enter pass

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
url = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
wait.until(EC.visibility_of_element_located((By.NAME,'password'))).send_keys(password)
time.sleep(5)

with open("urls.txt") as f:
    for url in f:
        driver.get(url)  
        
time.sleep(8) #i video dont have ads then change 8 to 3 or 4         
driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button').click()
driver.find_element_by_css_selector('yt-icon.style-scope.ytd-toggle-button-renderer').click()
time.sleep(3)
driver.find_element_by_css_selector('#subscribe-button > ytd-subscribe-button-renderer > tp-yt-paper-button > yt-formatted-string').click()
driver.close()


#add these script again and again  i added only two you addd how much time like and sub you want and change mail and pass how much time you want in text file url is enough for all new drivers 

#if you only want like and dont want auto subscribers means remove the 29 and 59 line which contain subscribe xpath code same


 


  
  


           
