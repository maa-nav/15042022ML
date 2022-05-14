####### Speech Synthesis (text to speech) #####

#pip install pyttsx3

import pyttsx3
ssynth = pyttsx3.init()


ssynth.setProperty('rate',150) #Rate/ speed of voice in  WPM
ssynth.setProperty('volume',1) # volume for the voice in float

voices = ssynth.getProperty('voices')    # 
ssynth.setProperty('voice',voices[1].id)
##
##
##ssynth.say('Welcome to python course')
## 
##ssynth.runAndWait()

####### Speech Recognition (Speech to Text) #######

import speech_recognition as sr

r = sr.Recognizer()
## 
##
##with sr.Microphone() as source:
##    r.adjust_for_ambient_noise(source)
##    print('kuch bollo')
##    audio = r.listen(source)
##    text = r.recognize_google(audio)
##    print('ye bola aapne>>',text)

#########  Chatbot ##########

import nltk
from nltk.chat.util import Chat, reflections


qa_pair = [ [ r'(.*)help(.*)'   ,['This is chatbot at your service']],
            [r'(.*)name(.*)'    ,['my name is Chitti!!!2.0']],
            [r'(.*)chatbot(.*)'  ,['I am here to solve your queries']],
            [r'(.*)buy(.*)'     ,['you can visit amazon.com']],
            [r'(.*)color(.*)'   ,['there are three main colors, RGB']],
            ['(.*)(father|creater||made||Inventor)(.*)' ,['NLTK!!!!!']]]


cb = Chat(qa_pair,reflections)
##cb.converse()
##cb.respond()

############ Personal Assistant ###########

import webbrowser as wb

while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Kuch puch be!!')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            if 'buy' in text.lower():
                wb.open_new_tab('https://www.amazon.in')
            elif text.lower() == 'ruk ja':
                break
            result = cb.respond(text)
            ssynth.say(result)
            ssynth.runAndWait()
        except Exception as e:
            print(e)
            
                
        










