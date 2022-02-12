import pandas as pd
import pyautogui
import time
import subprocess
from datetime import datetime


def sign_in(meeting_link):
    subprocess.call("C:\\Users\\91798\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    time.sleep(2)
# to click on join button
    join1 = pyautogui.locateCenterOnScreen('j1.png')
    pyautogui.moveTo(join1)
    pyautogui.click()
# to input the meeting id
    meeting_id_btn=pyautogui.locateCenterOnScreen('meeting.png')
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.click()
    pyautogui.write(meeting_link)

# disabling the media buttons
    media_btn=pyautogui.locateAllOnScreen('media.png')
    for btn in media_btn:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(1)

# click on join btn
    join_btn=pyautogui.locateCenterOnScreen('join.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    time.sleep(4)

data=pd.read_csv(r"C:\Users\91798\Desktop\nw\classes.csv")
print(data)

#sign_in('eied12')

while True:
    now_date_time=datetime.now().strftime("%H:%M")
    #day = datetime.now().strftime("%A")eied3
    if now_date_time in str(data['timings']):
       row=data.loc[data['timings']==now_date_time]
       #row_1=data.loc[data['day']==now_date_time]
       meeting_id=str(row.iloc[0,1])

       sign_in(meeting_id)
       time.sleep(3)
       print('Signed In')


