import time
import webbrowser

from gtts import gTTS
from mutagen.mp3 import MP3
import miniaudio
import requests
import speech_recognition as sr

listener = sr.Recognizer()


def say(text):
    try:
        print("    ")
        print("-------------------")
        print("    ")
        print(f"Vera: {text}")
        print("    ")
        print("-------------------")
        print("    ")
        tts = gTTS(text=text, lang='sk', slow=False)
        tts.save("1.mp3")
        file = '1.mp3'
        audio = MP3(file)
        length = audio.info.length
        stream = miniaudio.stream_file(file)

        with miniaudio.PlaybackDevice() as device:
            device.start(stream)
            time.sleep(length)
    except:
        pass


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, 0, 15)

        try:
            query = r.recognize_google(audio, language='sk-sk')  # en-in
            print(f"povedal si: {query}\n")  # User query will be printed.

        except Exception as e:
            return "None"
    return query


say("Ahoj som vera a rada ti pomôžem nájsť čo potrebuješ.")

if __name__ == "__main__":
    while True:
        message = takeCommand()
        r = requests.get(f'http://192.168.1.38:5000/?text={message}')
        if "http" in r.text:
            webbrowser.open(r.text)
        else:
            say(r.text)
