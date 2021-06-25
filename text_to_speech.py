from playsound import playsound
from gtts import gTTS
def playaudio(audio):
    plasound(audio)
def convert(text):
    audio=gTTS(text)
    audio.save("audio_file.mp3")
    playsound("audio_file.mp3")

if __name__=="__main__":
    convert("Hey chandu, please put on your mask")