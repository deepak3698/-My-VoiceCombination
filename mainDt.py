import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

finalData=[]

path=os.curdir

def avaiableData():
    dt=os.listdir(f"{path}\\availabeVoice")
    listOfAvailabeDataByVoice=[i[:-4] for i in dt if i.endswith(".mp3")]
    return listOfAvailabeDataByVoice


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(f"{path}\\availabeVoice\\{filename}")
    


def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(f"{path}\\availabeVoice\\{audio}")
    return combined

def generateAnnouncement(filename):
    listOfAvailabeData=["me","ra","am"]
    listOfPresentData=[]
    listOfMakeVoice=[]
    listOfSingleData=[]

    listOfItem=filename.split(" ")
    for item in listOfItem:
        char=""
        j=0
        for index,val in enumerate(item):
            char=char+val
            j=j+1
            if(j==2 and char in listOfAvailabeData):
                listOfPresentData.append(char)
                textToSpeech(char,f"{char}.mp3")
                finalData.append(char)
                char=""
                j=0
            if(j==2 and char not in listOfAvailabeData):
                listOfMakeVoice.append(char)
                textToSpeech(char,f"{char}.mp3")
                finalData.append(char)
                char=""
                j=0
            if(index==len(item)-1 and j==1):
                listOfSingleData.append(char)
                textToSpeech(char,f"{char}.mp3")
                finalData.append(char)

        char=""
        j=0
    print(finalData)
        # dt1=["1s","1d","2s","2d","3s","3d","4s"]
        # audios = [f"{i}.mp3" for i in dt1]

        # announcement = mergeAudios(audios)
        # announcement.export("final.mp3", format="mp3")


if __name__ == "__main__":
    print("Generating Voices...")
    # generateSkeleton()
    print("Final Song...")
    generateAnnouncement("my name is deepak tiwari")
    # for item in finalData:
    #     textToSpeech(item,f"{item}.mp3")
    audios = [f"{i}.mp3" for i in finalData]
    announcement = mergeAudios(audios)
    announcement.export("finalDT142.mp3", format="mp3")

