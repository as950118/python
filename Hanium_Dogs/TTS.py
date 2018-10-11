import os
import sys
import pyttsx3

engine = pyttsx3.init()
engine.say("이상이 감지되었습니다")
engine.runAndWait()
