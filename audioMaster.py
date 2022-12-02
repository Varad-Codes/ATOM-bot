import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
class AudioIO:
    def __init__(self, voiceIndex, voiceRate) -> None:

        voices = engine.getProperty('voices')
        voice_options = voiceIndex #If on windows leave it to 0 | if on linux/unix use 10
        engine.setProperty('voice', voices[voice_options].id)

        rate = engine.getProperty('rate')   # getting details of current speaking rate
        # print (rate)                        #printing current voice rate
        engine.setProperty('rate', voiceRate) 

    @staticmethod
    def say(audio):
        engine.say(audio)
        engine.runAndWait()
    

#DEPRICATED
    @staticmethod
    def hear():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            result = r.recognize_sphinx(audio)
            print("Sphinx thinks you said: " + result)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))

