import speech_recognition as sr
import pyttsx3 as px3
import wikipedia

def speak(text):
    tts = px3.init()
    tts.say(text)
    tts.runAndWait()

def user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak now!')
        print('Listening..................')
        audio = r.listen(source)
        query = r.recognize_google(audio)
    return query

def run():
    query = user_input().lower()
    print(f'You asked to search {query}')
    results = wikipedia.summary(query, sentences=3)
    speak('Wikipedia said: ')
    speak(results)

def trigger():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say Babushka to activate')
        audio = r.listen(source)
        query = r.recognize_google(audio)
    return query

def chat():
    speak('Welcome!')
    speak('Do you want me to ask something?')
    response = user_input()
    negation = ['no','nope','nah']
    while(response.lower() not in negation):
        speak('What do you want to know about?')
        run()
        speak('Do you want to know anything else?')
        response = user_input()
    speak('It was nice talking to you')

start=trigger()
while(start.lower() != 'babushka'):
    start=trigger()

chat()
