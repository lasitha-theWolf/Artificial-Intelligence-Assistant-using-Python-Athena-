import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import pywhatkit as kt


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   #voice array


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:

            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'athena' in command:
                command = command.replace('athena', '')
                print(command)
    except:
        pass
    return command


def run_athena():
    command = take_command()
    print(command)

    if 'who are you' in command:
        print('Hi! My name is Athena! And i am lasithas first artifical intelligence assistant.')
        talk('Hi! My name is Athena!')
        talk('And i am lasithas first artifical intelligence assistant ')


    elif 'create' in command:
        talk('Mr. lasitha heenkenda is my creator and my master')


    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        print(song)
        pywhatkit.playonyt(song)

    elif 'thank' in command:
        talk('You are Welcome Sir')

    elif 'virus' in command:

        talk('We are Anonymous. We do not forgive. We do not forget. Expect us!')




    elif 'search' in command:
        search = command.replace('search', '')
        talk('searching' + search)
        kt.search(search)

    elif 'send' in command:
        pywhatkit.sendwhatmsg('+94715906668', 'Hello Sir!', 1, 15)
        pywhatkit.search('')


    elif 'good morning' in command:
        talk('Good morning Sir!')


        talk('Have a nice day Sir')

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Current time is ' + time)


    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'where is' in command:
        place = command.replace('where is', '')
        info = wikipedia.summary(place, 1)
        print(info)
        talk(info)


    elif 'are you single' in command:
        talk('No i am in relationship with wifi')


    elif 'good night' in command:
        talk('Good night and Sweet dreams Sir! ')


    else:
        talk('Please say the command again.')


while True:
    run_athena()
