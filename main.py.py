import pyautogui, collections
import pvporcupine
import struct
import pyttsx3, pyaudio
from pydub import AudioSegment
from pydub.playback import play
import time

Point                   = collections.namedtuple("Point", "x y")

############################# INPUTs needed #############################
ACCESS_KEY              = ""                    #Get Access Key from porcupine site
skip_button_location    = Point(x=821, y=533)   #Location of Skip-Ad button gathered from cursor_position_caliberation.py script for YOUR DEVICE
#########################################################################

skip_ad_wait_time       = 0.5  # in seconds

def play_sound(file):
    song = AudioSegment.from_mp3(file)
    print('playing sound')
    play(song)

def speak(text):
    text    = str(text)
    engine  = pyttsx3.init('sapi5')
    voices  = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()

# Goes to Skip-add button location and clicks
def skip_add_func():
    print(f"The Ad position is: {skip_button_location} & Ad skipped")
    pyautogui.click(skip_button_location)
    time.sleep(skip_ad_wait_time)
    
# Detects My call to Jarvis
def hotword():
    porcupine       =   None
    paud            =   None
    audio_stream    =   None
    
    # pre trained keywords    
    porcupine       =   pvporcupine.create(keywords=["jarvis", "alexa"], access_key=ACCESS_KEY) 
    paud            =   pyaudio.PyAudio()
    audio_stream    =   paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
    print("Audio Recognition ON")
    speak("Audio Recognition ON")
    
    # loop for streaming
    while True:
            
        keyword=audio_stream.read(porcupine.frame_length)
        keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

        # processing keyword comes from mic 
        keyword_index=porcupine.process(keyword)

        # checking first keyword detetcted for not
        if keyword_index>=0:
            print("hotword detected, skipping Ad")
            play_sound("start_sound.mp3")
            skip_add_func()

# Start application
hotword()
