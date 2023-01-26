from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

 

driver = webdriver.Firefox()
driver.set_window_size(600, 600)

driver.get("https://evarsity.srmist.edu.in/srmsip/")
WebDriverWait(driver,10).until(EC.presence_of_all_elements_located(
    (By.XPATH,"//input[@value='Submit']")))
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter Student ID / Registration Number /Net ID*']").send_keys("rs6695")
driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("S7cM4Mp0A#")

with open('filename.png', 'wb') as file:
    file.write(driver.find_element(By.ID,"cpimg1").screenshot_as_png)


time.sleep(0.5)

captchaTask = driver.execute_script('return document.getElementById("sdivcolor").innerHTML')
text = input(captchaTask+" : ")

driver.find_element(By.XPATH,"/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/form/div[1]/table/tbody/tr[6]/td/input").send_keys(text)
driver.execute_script("loginform()")

#CHECK FOR FORCE LOGIN by having 2 active sessions
#maxlength="6"
#document.getElementById("sdivcolor").innerHTML
