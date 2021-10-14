from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import string
import time
inputName=input()
inputPass=input()
options1 = webdriver.ChromeOptions()
options1.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options1)
driver.get("https://www.the-west.ro/")
driver.find_element_by_xpath('//*[@id="inputUsername"]/input').send_keys(inputName)
driver.find_element_by_xpath('//*[@id="inputPassword"]/input').send_keys(inputPass)
driver.find_element_by_xpath('//*[@id="loginButton"]').click()
a = ActionChains(driver)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="world_16"]/a').click()
time.sleep(6)
driver.find_element_by_xpath('//*[@id="map"]/div[387]').click()
time.sleep(2)
energy=driver.find_element_by_xpath('//*[@id="ui_character_container"]/div[4]').text
energy=int(energy.split('/')[0])
print(energy)
q=False
try:
    driver.find_element_by_xpath('//*[@id="queuedTasks"]/span[4]')
    q=True
except:
    q=False

if(energy>=12 and q==False):
    #Work Work q=false means i have space in queue
    driver.find_element_by_xpath('//*[@id="ui_bottombar"]/div/div[2]/div[2]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="map_town_27604_11467"]/area[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="windows"]/div[3]/div[12]/div[1]/div/div[5]/div[2]/div[4]/div[1]/div/div[10]/div[1]/span/a').click()
    time.sleep(2)
    while(energy>=12 and q==False):
        driver.find_element_by_xpath('//*[@id="windows"]/div[4]/div[12]/div[3]/div[3]/div[5]/div[4]').click()
        time.sleep(2)
        try:
            driver.find_element_by_xpath('//*[@id="queuedTasks"]/span[3]')
            q=True
        except:
            q=False
else:
    #Sleepy sleepy q=false means i have space in queue
    if(energy<12 and q==False):
        driver.find_element_by_xpath('//*[@id="ui_bottombar"]/div/div[2]/div[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="map_town_27604_11467"]/area[4]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="hotel-content-3644"]/div[2]/div/div[10]/div[2]/div[2]/div[4]').click()

