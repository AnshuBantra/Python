import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input('Say something: ')
cowsay.cow(this)
engine.say(this)
engine.runAndWait()