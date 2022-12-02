import audioMaster
import input
import answer

AudioIO = audioMaster.AudioIO(1, 125) #if on Windows use 0 for voiceIndex | if on linux use 10
# audioInput = input.Input()
obj = input.Input()
answerObj = answer.QNA()

# def main():
#     try:
#         print("start")
#         AudioIO.say("Starting")
#         while True:
#             print("looping")
#             talk = obj.get_audio()
#             answerObj.askQues(talk)
#         # value = AudioIO.hear()
#     except KeyboardInterrupt:
#         pass

if __name__ == "__main__":
    try:
        print("start")
        AudioIO.say("Starting")
        while True:
            print("looping")
            talk = obj.get_audio()
            answerObj.askQues(talk)
        # value = AudioIO.hear()
    except KeyboardInterrupt:
        pass    
