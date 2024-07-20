import gemini_ai_api
import pyautogui as py
import pyperclip
from datetime import datetime
import time

# Constants
BREVE_CLICK_COORDS = (1318, 1051)
DRAG_START_COORDS = (594, 210)
DRAG_END_COORDS = (1862, 893)
CHECK_HOUR = 3
CHECK_MINUTE = 30

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

def write_in_file(new_data) :
    try :
        messages = new_data.strip().split('\n')
        if "friend2 BCA" in messages[-1] :
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

while True :
    now = datetime.now()
    hour, minute = now.hour, now.minute
    
    if (hour, minute) == (CHECK_HOUR, CHECK_MINUTE):
        print("THE TIME IS OVER!")
        exit(1)
    else:
        honor = run()
        print(f"run Function Call == checked! Time = {hour},{minute}")
        write_in_file(honor)
        print(f"write_in_file Function Call == checked! Time = {hour},{minute}")
    # break
