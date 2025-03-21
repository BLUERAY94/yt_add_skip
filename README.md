# yt_add_skip
How I used AI to "Skip Ad" in YouTube

Steps to run this script:

Step 1) Git clone this repository.

Step 2) Create Virtual Environement.

Step 3) run pip install -r requiremenets.txt

Step 4) run 'cursor_position_caliberation.py' script.

        * Set 'CURSOR_LOC_FINDER = 1' and run the script.
        
        * While the script is running, move the cursor to any desired location (skip-ad button) and wait for few seconds.
        
        * After 10 seconds, script will stop running. Come to terminal and check the readings.
        
        * You will get the desired cursor position (x, y) coordinates of Youtube-skip-Ad button for your Device.
        
Step 5) Create account in picovoice website (https://picovoice.ai/platform/porcupine/)

        * Generate a Access KEY to use the Hotword Detection library in python.
        
Step 6) Open 'main.py' script.

        * You need to fill the "ACCESS_KEY" from picovoice in the mentioned variable.
        
        * You need to fill the (x, y) coordinates of Youtube-skip-ad button into this varialbe "skip_button_location", that you determined using the 'cursor_position_caliberation.py' script.
        
Step 7) run the 'main.py' script.

Step 8) For easy deployment, create a shortcut of the "add_skip.bat" file and place it in desktop. You can double click on the bat file to instantly launch the script.
