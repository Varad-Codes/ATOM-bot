import audioMaster
import sys

audioObj = audioMaster.AudioIO(1, 125)

class QNA:
    
    def __init__(self) -> None:
        pass

    @staticmethod
    def askQues(stringVar=""):
        if "your" and "name" in stringVar:
            audioObj.say("My name is ATOM")
            
        elif "hello" in stringVar or "hi" in stringVar or "hey" in stringVar:
            audioObj.say("Hello, nice to meet you!")

        elif "test case" in stringVar:
            audioObj.say("Varad. Shounak. pixo")

        # if "introduce yourself" in stringVar:
        #     audioObj.say("Hello, Everyone!My Name Is Jarvis. I Got No Soul But I Got Emotions. Also, I Love To Interact With Humans. Thank you")
        
        elif "introduce" and "yourself" in stringVar:
            audioObj.say("Hello, Everyone!My Name Is ATOM. I Got No Soul But I Got Emotions. Also, I Love To Interact With Humans. Thank you")

        elif "when" and "were" and "you" and "made" in stringVar:
            audioObj.say("The Date Of My Structural Birth Is 10th Of November And The Date Of My Software Birth Is 30th Of November.")

        elif  "the" and "main" and "purpose" and "for" and "making" and "you" in stringVar:
            audioObj.say("The Main Purpose Of My Birth Is To Interact With People And Pass-On Knowledge.")

        elif "exit" in stringVar or "bye" in stringVar:
            audioObj.say("Bye, It was good to know")
            print("Exit")
            sys.exit(0)
        
        else:
            audioObj.say("This is in testing phase, only selected questions can be answered")

