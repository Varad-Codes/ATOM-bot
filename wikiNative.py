import wikipedia
import audioMaster

audio = audioMaster.AudioIO(0, 125)

class Wiki:
    length = 4
    query = ""
    def __init__(self) -> None:
        self.length = 4
        self.query = "ChatBot"

    @staticmethod
    def askWiki(querie, length):
        try:
            summary = wikipedia.summary(querie, length)
            print(summary)
            audio.say(summary)
        except wikipedia.exceptions.PageError:
            print("Can't find the page on wikipedia")
            audio.say("Can't find the page on wikipedia")

