import speech_recognition as sr
# import audioMaster

# audioObj = audioMaster.AudioIO(0, 125)

class Input:
    
    # audioObj = audioMaster.AudioIO(0, 125)

    def __init__(self) -> None:
        pass
    @staticmethod
    def get_audio():
        r = sr.Recognizer()
        m = sr.Microphone()

        try:
            with m as source: r.adjust_for_ambient_noise(source)
            print("Set minimum energy threshold to {}".format(r.energy_threshold))
            print("Say something!")
            with m as source: audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:                    # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)
                print("{}".format(value))
                return value

            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
                # value = "Can't recognise what you said"
                # return value


            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        except KeyboardInterrupt:
            pass
        # return value