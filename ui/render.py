from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, os, imageio

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "hud.html")
OUT = os.path.join(BASE, "hud.gif")

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.set_window_size(900, 550)
driver.get("file://" + HTML)

frames = []
for i in range(30):
    p = os.path.join(BASE, f"frame_{i}.png")
    driver.save_screenshot(p)
    frames.append(imageio.imread(p))
    time.sleep(0.1)

driver.quit()

imageio.mimsave(OUT, frames, duration=0.1)

for f in os.listdir(BASE):
    if f.startswith("frame_"):
        os.remove(os.path.join(BASE, f))

print(OUT)
