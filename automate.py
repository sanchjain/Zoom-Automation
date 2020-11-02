import schedule
import pandas as pd
import os

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from password import lms_password

def lms_login(driver, lms_username, lms_password):
	print("logging in")
	driver.find_element_by_xpath("//input[@name = 'username']").send_keys(lms_username)
	driver.find_element_by_xpath("//*[@id='password']").send_keys(lms_password)
	driver.find_element_by_xpath("//*[@id='loginbtn']").click()

def get_subject(driver, subj_code):
	for i in range(6, 12):
		subj = driver.find_element_by_xpath(f"//*[@id='nav-drawer']/nav/ul/li[{i}]/a")
		print(subj.text)
		if subj.text == subj_code:
			subj.click()
			break
	
def start_browser(classCode):
    lms_url = "https://archimedes-lms.thapar.edu/moodle/login/"
    driver = webdriver.Chrome(executable_path=os.path.abspath(r'chromedriver.exe'))
    driver.get(lms_url)
    lms_username = 'rprabhakar_be19@thapar.edu'
    WebDriverWait(driver,10000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))
    
    if driver.current_url == "https://archimedes-lms.thapar.edu/moodle/login/":
        lms_login(driver, lms_username, lms_password)
    
    get_subject(driver, classCode)

def join_class(classCode, start_time, end_time, driver):
    start_browser(classCode)
    
if __name__ == '__main__':
    timeTable = pd.read_csv('schedule.csv')
    timeTable.columns = ["Day", "Code", "Start Time", "End Time"]

    while True:
        for i in timeTable.index:
            day  = timeTable['Day'][i][0]
            classCode = timeTable['Code'][i]
            start_time = str(timeTable['Start Time'][i])
            end_time = str(timeTable['End Time'][i])

            if day.lower()=="monday":
                schedule.every().monday.at(start_time).do(join_class, classCode, start_time, end_time)
                print(f"Scheduled class {classCode} on {day} at {start_time} and ending at {end_time}")
        
            if day.lower()=="tuesday":
                schedule.every().tuesday.at(start_time).do(join_class, classCode, start_time, end_time)
                print(f"Scheduled class {classCode} on {day} at {start_time} and ending at {end_time}")
        
            if day.lower()=="wednesday":
                schedule.every().wednesday.at(start_time).do(join_class, classCode, start_time, end_time)
                print(f"Scheduled class {classCode} on {day} at {start_time} and ending at {end_time}")
        
            if day.lower()=="thursday":
                schedule.every().thursday.at(start_time).do(join_class, classCode, start_time, end_time)
                print(f"Scheduled class {classCode} on {day} at {start_time} and ending at {end_time}")
        
            if day.lower()=="friday":
                schedule.every().friday.at(start_time).do(join_class, classCode, start_time, end_time)
                print(f"Scheduled class {classCode} on {day} at {start_time} and ending at {end_time}")
        
            if day.lower()=="saturday":
                schedule.every().saturday.at(start_time).do(join_class, classCode, start_time, end_time)
                print(f"Scheduled class {classCode} on {day} at {start_time} and ending at {end_time}")
        
            if day.lower()=="sunday":
                schedule.every().sunday.at(start_time).do(join_class, classCode, start_time, end_time)
                print(f"Scheduled class {classCode} on {day} at {start_time} and ending at {end_time}")