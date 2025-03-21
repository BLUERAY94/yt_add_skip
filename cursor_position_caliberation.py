import pyautogui, collections
import time
skip_ad_wait_time = 0.5  # in seconds


CURSOR_LOC_FINDER = 1           #To know the Cursor Location, Keep this as 1. To Move the cursor to location, Keep this as 0.
TEST              = not(CURSON_LOC_FINDER = 1)

for i in range(20):
    time.sleep(skip_ad_wait_time)
        
    if CURSOR_LOC_FINDER == 1:
        # Get the current position of the cursor
        skip_button_location    = pyautogui.position()
        print(f"The current cursor position is: {skip_button_location}")
        
    if TEST == 1:
        # Go to (x=822, y=530) and click
        Point                   = collections.namedtuple("Point", "x y")
        skip_button_location    = Point(x=830, y=531)
        print(f"Skipping add at: {skip_button_location}")
        time.sleep(skip_ad_wait_time)
        pyautogui.click(skip_button_location)
