import os
from pydub import AudioSegment

from gtts import gTTS

path=os.curdir




def generateSkeleton():
    audio = AudioSegment.from_mp3('dt.mp3')
    # First_Part #1
    start = 2000
    finish = 2150
    audioProcessed = audio[start:finish]
    audioProcessed.export(f"{path}\\VoiceScrached\\dt2.mp3", format="mp3")



generateSkeleton()


def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(f"{path}\\VoiceScrached\\{audio}")
    return combined

audios = ["dt2.mp3","dt1342.mp3"]
announcement = mergeAudios(audios)
announcement.export("dtVoice1.mp3", format="mp3")