import os
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def login_byEmail(driver, email, password):
    WebDriverWait(driver,10000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))
    
    driver.find_element_by_xpath("//*[@id='email']").send_keys(email)
    driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
    driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/div/div[1]/button').click()

def login_byGoogle(driver):
    WebDriverWait(driver,10000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))
    driver.find_element_by_xpath('//*[@id="login"]/div/div[3]/div/div[4]/a[2]').click()
    time.sleep(5)
    print("Hello")
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('raghavprabhakar66@gmail.com')
    time.sleep(5)
    nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
    nextButton[0].click()
    # if already logged in to Google which is very unlikely
    driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[2]/div').click()
    time.sleep(5)

def join_meeting():
    pass

def start_browser(driver):
    driver.get(zoom_home_url)
    WebDriverWait(driver,10000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))

    # check if you are logged in
    if driver.find_element_by_xpath('//*[@id="navbar"]/ul[2]/li[5]/a').text == 'SIGN IN':
        driver.find_element_by_xpath('//*[@id="navbar"]/ul[2]/li[5]/a').click()
        login_byGoogle(driver)
    else:
        print("Already Logged In.")
    
    join_meeting()
    time.sleep(5)
    driver.quit()

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path=os.path.abspath(r'chromedriver.exe'))
    zoom_home_url = "https://zoom.us/"
    
    start_browser(driver)