import os
import sys
import pyttsx3

class TTS():
        def __init__(self):
            self = self
        def tts(self, code):
            engine = pyttsx3.init()
            engine.say("이상이 감지되었습니다")
            engine.say("오류 코드는" + code + "입니다")
            engine.runAndWait()
            return -1
