import time
from app import EPR


User = EPR("rs6695","S7cM4Mp0A#")
CaptchaImageFileName =  User.SetCredentials()

User.GetCaptcha()
time.sleep(0.5)
CaptchaImageTask = User.GetCaptchaTask()
CaptchaImageTaskAnswer = input(CaptchaImageTask+" : ")
User.SetCaptchaAndLogin(CaptchaImageTaskAnswer)
time.sleep(2)
User.GetAttendencePage()