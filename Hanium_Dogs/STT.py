import speech_recognition as sr


class STT():
        def __init__(self):
            self = self
        def stt(self):
            r = sr.Recognizer()
            mic = sr.Microphone()

            with mic as source:
                audio = r.listen(source)
            return r.recognize_google(audio, language='ko-KR')
