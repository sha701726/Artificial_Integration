import gemini_ai_api gemini_ai
import pyautogui as py
import pyperclip
from datetime import datetime
import time

# Constants
BREVE_CLICK_COORDS = (1318, 1051)
DRAG_START_COORDS = (594, 210)
DRAG_END_COORDS = (1862, 893)

# Click on the Breve button
py.click(*BREVE_CLICK_COORDS)
print("Breve Clicked == Checked!")

def run():
    time.sleep(2)
    py.moveTo(*DRAG_START_COORDS)
    time.sleep(2)
    py.dragTo(*DRAG_END_COORDS,duration=2.0,button="left")
    py.hotkey('ctrl', 'c')
    print("DATA IS COPYED == Checked!")
    time.sleep(2)
    py.click(*DRAG_END_COORDS)
    time.sleep(2)
    data_val = pyperclip.paste()
    return data_val

def Function_call(new_data,name) :
    try :
        messages = new_data.strip().split('\n')
        if f"{name}" in messages[-1] :
            py.click(995,960)
            response = gemini_ai.get_gemini_response(new_data)
            pyperclip.copy(response)
            time.sleep(1)
            py.hotkey('ctl','v')
            print("DATA IS PASTED == Checked!")
            time.sleep(2)
            py.click((1848,952))
            print("DATA IS SENT SUCCESSFULLY.")
    except Exception as E :
         print(f"Error: {E}")

name = input("Enter The What's app User Name: ")
red = '\033[91m'  # ANSI escape code for red text
reset = '\033[0m'  # ANSI escape code to reset color
message = f"{red}                   WHEN YOU ENTER THE HOUR AND MINUTS PLEASE ENSURE THAT BOTH HOUR AND MINUTS SHOULD NOT BE ZERO{reset}"
CHECK_HOUR = int("Enter The Hour, Till You Would Like To Run The Script: ")
CHECK_MINUTE = int("Enter The Minuts, Till You Would Like To Run The Script: ")
while True :
    now = datetime.now()
    hour, minute = now.hour, now.minute
    
    if (hour, minute) == (CHECK_HOUR, CHECK_MINUTE):
        print("THE TIME IS OVER!")
        exit(1)
    else:
        honor = run()
        print(f"run Function Call == checked! Time = {hour},{minute}")
        Function_call(honor,name)
        print(f"Function_call function call == checked! Time = {hour},{minute}")
    # break
