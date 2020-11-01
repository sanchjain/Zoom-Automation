from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome()
lms_url = "https://archimedes-lms.thapar.edu/moodle/login/"

lms_username = input("LMS username: ")
lms_password = input("LMS password: ")

def lms_login(lms_username, lms_password):
    global driver
    print("logging in")


def start_browser():

	global driver
	driver = webdriver.Chrome(executable_path=r'C:\Users\sanch\Documents\Zoom-Automation\chromedriver.exe')

	driver.get(lms_url)

	WebDriverWait(driver,10000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))

	if driver.current_url == "https://archimedes-lms.thapar.edu/moodle/login/":
		login()