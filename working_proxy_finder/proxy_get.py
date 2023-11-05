from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.options import Options
import requests
import queue
import threading

options = Options()
options.headless = False
Q = queue.Queue()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options = options)

driver.get("https://hidemy.io/en/proxy-list/")

parent = driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div[4]/table/tbody")
children = parent.find_elements(By.TAG_NAME, "tr")

for child in children:
	elements = child.find_elements(By.TAG_NAME,"td")
	Q.put(elements[0].text+":"+elements[1].text)

def check_proxies():

	global Q
	while not Q.empty():
		proxy = Q.get()
		proxies = {
			"http" :proxy, 
			"https":proxy, 
		}
		try:
			res = requests.get("https://ipinfo.io/json",proxies = proxies)
		except:
			continue

		if res.status_code == 200:
			print(proxy)


for thread in range(3000):
	threading.Thread(target = check_proxies).start()
driver.close()