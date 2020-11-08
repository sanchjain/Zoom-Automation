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
		if subj.text == subj_code:
			subj.click()
			break
	
def start_browser(driver, lms_username, lms_password):
	driver.get(lms_url)

	WebDriverWait(driver,10000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))

	if driver.current_url == "https://archimedes-lms.thapar.edu/moodle/login/":
		lms_login(driver, lms_username, lms_password)

if __name__ == '__main__':
	driver = webdriver.Chrome(executable_path=os.path.abspath(r'chromedriver.exe'))
	#driver = webdriver.Chrome()
	lms_url = "https://archimedes-lms.thapar.edu/moodle/login/"
	
	lms_username = 'rprabhakar_be19@thapar.edu'
	#lms_password = 'ENTER YOUR PASSWORD'

	start_browser(driver, lms_username, lms_password)
	get_subject(driver, 'UCS405')