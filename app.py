from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, string , random



class EPR:
    Username = ""
    Password = ""
    driver = webdriver.Firefox()
    driver.set_window_size(600, 600)
    

    def __init__(self,Username,Password):
        self.Username = Username
        self.Password = Password
    
    def SetCredentials(self):
        self.driver.get("https://evarsity.srmist.edu.in/srmsip/")

        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_all_elements_located((By.XPATH,"//input[@value='Submit']"))
                )
        finally:
            self.driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter Student ID / Registration Number /Net ID*']").send_keys(self.Username)
            self.driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys(self.Password)
    
    
    def GenerateFileName(self):
        return ''.join(random.choices(string.ascii_letters, k=5))
        
    
    def GetCaptcha(self):
        ImageFileName = self.GenerateFileName()+".png"
        with open(ImageFileName, 'wb') as file:
            file.write(self.driver.find_element(By.ID,"cpimg1").screenshot_as_png)
            file.close()
        return ImageFileName
    
    def GetCaptchaTask(self):
        return self.driver.execute_script('return document.getElementById("sdivcolor").innerHTML')
    
    def SetCaptchaAndLogin(self,Answer):
        self.driver.find_element(By.XPATH,"/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/form/div[1]/table/tbody/tr[6]/td/input").send_keys(Answer)
        self.driver.execute_script("loginform()")
    
    def GetAttendencePage(self):
        self.driver.execute_script("AjaxPostMethod('smhid=ZjQwZjdhYzdmMTkzNjdlMjBkZTFhYWJkN2RkNGI1NzNhZmQxMTFmMWVjMmQ1NzkzMDdiOWEzODcyMTA4NDdlNjAxNDA5ODZiNzgzNDhlMzMxZjgwNjJiZGQwY2U2OWRkMGJlMGQ1OGI4ZDE2OTliOWIwMzAwYTlkM2M0MjRkNjgwMzZhMTg4MTgxOTIwYWQ4MDkzNDdlZWI3MzBlZjk4OTEzODUwNTU4MzMyNzYxMGFlYmQ1MDQ2M2NhNjcyNmQ5NzFmMTdmNTFkYWFkMTZlOWUzY2FmMzlkNjM5MjE5NmZhYzBmZjE0MjQyYTBlYjdkOTc3MzM1NWEzNjViOGQ1ZjAxOTUzYjQ4MjQ5ZmVmNmM4NjNhOGFlMDhlZGU5OGQzODkyMGRjNWQ0ZTg1M2Q4NzJlNmU4MTYyNWFmNTFkYmI4MjlhZjM3ZTg2NDM5OTViNTAwMzUyZmYyNTA5MDE0NmFhNjVmYzQzZWY1Y2Y1YWFjNzJlNTg0OGIzZDE3MTc3ZDI1OWU5YmM1MWExNWEwZDYxYjY4NzgxNWI2MmRjZWNmMzZkYzdkMTgxY2VjYzNjNDExMTI2YzdhZWQyMjdjNjE2NGZiYzk0ZjJhZjU1NGM1MTliNzFjYjFmMTZhNGQwMzU2Y2Q3OWE3NzQxOWJhNGYwMThmMzdiYWQwMzc4ODQ5MmZkODQ3MDkzZTNiZjk2MzViZjQ2NDRkNjVmYTQ1Mzc2NmEzMDcyYmI0MDZiYzYyOTJiY2M3Zjc1NjcwNDc0Yzg4MDU3MjJhZDk3ZmYyOWRhZGExYWI0NmYyZmQxMmY=')")








        


        



