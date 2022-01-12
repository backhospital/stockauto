from pywinauto import application
import time
import os

# 파이썬으로 크레온플러스 자동연결하기

os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('taskkill /IM DibServer* /F /T')
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
os.system('wmic process where "name like \'%DibServer%\'" call terminate')
time.sleep(5)        

app = application.Application()
app.start('C:\CREON\STARTER\coStarter.exe /prj:cp /id:**** /pwd:**** /pwdcert:****** /autostart') #아이디 / 비번 / 공인인증서 비번
time.sleep(60)
