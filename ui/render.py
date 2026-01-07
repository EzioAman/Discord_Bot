from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.set_window_size(950, 600)

driver.get("file://" + __file__.replace("render.py", "hud.html"))
time.sleep(2)

driver.save_screenshot("panel.png")
driver.quit()
