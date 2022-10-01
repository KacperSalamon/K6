#before start coding you need install 2 things:
# - pyttsx3 --> open your cmd and write this code -- pip install pyttsx3
# wikipedia --> the same step like above but with change commend -- pip install wikipedia
# happy coding :)

import pyttsx3
import wikipedia

silvia = pyttsx3.init()

Inside = input("Search sth on Wikipedia/Google: ")
lines = input("In how many lines reslut should be appear: ")
result = wikipedia.summary(Inside, sentences = lines)
print(result)
silvia.say(result)
silvia.say("Thank for use me")
silvia.runAndWait()