from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import webbrowser, os, math, time
import pyautogui as pa
from word2number import w2n
from random import choice
from definitions import *

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

tts = gTTS('Welcome Hawk, here Alexa performing to you')
tts.save('saludo.mp3')
playsound('saludo.mp3')
os.remove('saludo.mp3')

def get_audio_from_microphone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = None
        try:
            text = r.recognize_google(audio)
        except:
            pass

        if text is not None:
            if "Alexa" in text:
                text = text.replace("Alexa", "")
                text = text.lower()
                print(text)
                try:
                    if "open" in text:
                        if "youtube" in text:
                            webbrowser.get('chrome').open(youtube)
                        elif "netflix" in text:
                            webbrowser.get('chrome').open(netflix)
                        elif "google" in text:
                            webbrowser.get('chrome').open(google)
                        elif "eva" in text:
                            webbrowser.get('chrome').open(eva)
                        elif "train mode" in text:
                            webbrowser.get('chrome').open(train)
                    elif "new tab" in text:
                        pa.hotkey('ctrl', 'n')
                    elif "combinations of" in text:
                        numbs = text.split("in")
                        a = numbs[1].strip()
                        b = numbs[2].strip()
                        a = a[10:len(a)+1]
                        answer = math.comb(int(a), int(b))
                        print(answer)
                        ttsfail = gTTS(f"Combination of {str(a)}, in {str(b)} its {answer}")
                        ttsfail.save('answer.mp3')
                        playsound('answer.mp3')
                        os.remove('answer.mp3')
                    elif "draw a circle" in text:
                        R = 400
                        (x,y) = pa.size()
                        (X,Y) = pa.position(x/2, y/2)
                        pa.moveTo(X+R,Y)

                        for i in range(360):
                            if i % 6 == 0:
                                pa.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
                    elif "say hi to" in text:
                        name = text.split(" ")
                        name = name[len(name)-1]
                        ttshi = gTTS(f"Hi {name}, I'm Alexa, nice to meet you")
                        ttshi.save("hi.mp3")
                        playsound("hi.mp3")
                        os.remove("hi.mp3")
                    elif "tell me a joke" in text:
                        joke = choice(jokes)
                        ttsjoke = gTTS(joke)
                        ttsjoke.save("joke.mp3")
                        playsound("joke.mp3")
                        time.sleep(2)
                        playsound("xd.mp3")
                        os.remove("joke.mp3")
                    elif "search" in text:
                        query = text.replace(" ", "+")
                        query = query.replace("search", "")
                        webbrowser.get('chrome').open(browse+query)
                    else:
                        ttsfail = gTTS("What the fuck you've just said?")
                        ttsfail.save('error.mp3')
                        playsound('error.mp3')
                        os.remove('error.mp3')
                except Exception as ex:
                    print(ex)
                    ttsfail = gTTS("There was an error, I couldn't complete your request")
                    ttsfail.save('error.mp3')
                    playsound('error.mp3')
                    os.remove('error.mp3')
        return audio


while True:
    get_audio_from_microphone()