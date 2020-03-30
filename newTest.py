import os

from gtts import gTTS

path=os.curdir
dt=os.listdir(f"{path}\\availabeVoice")

ist2=[i[:-4] for i in dt if i.endswith(".mp3")]

print(ist2)


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(f"{path}\\availabeVoice\\{filename}")


textToSpeech("heo","name.mp3")