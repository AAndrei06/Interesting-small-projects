from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.headless = False

# Proxy
#'103.39.133.213:3128'
proxy_ip_port = '190.242.181.59:999'

options.add_argument(f"--proxy-server={proxy_ip_port}")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options = options)
driver.get("https://ipinfo.io/json")

print(driver.find_element(By.XPATH,"/html/body").text)

driver.quit()


