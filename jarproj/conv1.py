import pyttsx3
import webbrowser
import random
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
from lispk import speak
from lispk import takeCommand
import os
import wmi
import smtplib
from datetime import date


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 16:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis, how may i help you.")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vpnvairohi@gmail.com', 'vchampkanayya5763')
    server.sendmail("vaishurohi2001@gmail.com", to, content)
    server.close()


def conver(query):
    query = query
    print(query)
    if query == "hello":
        answer = "hi am jarvis"
        speak(answer)
        return(answer)

    elif "what is my name" in query:
        name1 = "sulaksha"
        speak(name1)
        print("Hello, " + name1 + '.')
        return(name1)

    elif "your name" in query:
        answer = "My name is Jarvis, at your service"
        speak(answer)
        return(answer)

    elif 'what\'s up' in query or 'how are you' in query:
        answer = "I am fine thankyou"
        speak(answer)
        return(answer)

    elif 'something about you' in query:
        answer = "In the Marvel Cinematic Universe  i was an AI developed by Tony Stark first primarily as being and artificial assistant in his house, and later modified to perform a lot of functions in the Mark 2 and now presently implemented by my group"
        speak(answer)
        return(answer)

    elif 'how will be my day' in query:
        answer = "wish that it will be good"
        speak(answer)
        return(answer)

    elif 'hangout jarvis' in query:
        answer = "Sorry  i would love to but i cant"
        speak(answer)
        return(answer)

    elif 'who am i jarvis' in query:
        answer = "you are my master"
        speak(answer)
        return(answer)

    elif 'can you be my friend' in query:
        answer = "Its my pleasure to be"
        speak(answer)
        return(answer)

    elif 'are you tired' in query:
        answer = "no master full of energy...."
        speak(answer)
        return(answer)

    elif 'goodbye jarvis' in query:
        answer = "goodbye have a nice day......"
        speak(answer)
        return(answer)

    # elif 'date' in query:
    #     today = date.today()
    #     speak("Today's date is :", today)
    #     print("Today's date is :", today)

    elif 'find location' in query:
        speak(print("What loaction you want to find"))
        location = takeCommand()
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak(f'Here are the result of location'+location)

    elif 'hibernate' in query:
        speak("good night master")
        os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

    elif 'open explorer' in query:
        va = "opening  master....."
        speak(va)
        print("opening  master.....")
        os.system("explorer.exe")
        return(va)

    elif 'brightness' in query:
        speak("please value to increase or decrease brightness")
        brightness = takeCommand()  # percentage [0-100]
        print(brightness)
        c = wmi.WMI(namespace='wmi')

        methods = c.WmiMonitorBrightnessMethods()[0]
        methods.WmiSetBrightness(brightness, 0)

    elif 'shutdown' in query:
        answer = "Do you want to shutdown your system? (yes/no)"
        speak(answer)
        a = takeCommand()
        if 'yes' in a:
            os.system("shutdown /s /t 1")
        elif 'no' in a:
            exit()
        return(answer)

    elif 'restart' in query:
        answer = "Do you want to shutdown your system? (yes/no)"
        speak(answer)
        a = takeCommand()
        if 'yes' in a:
            os.system("shutdown /r /t 1")
        elif 'no' in a:
            exit()
        return(answer)

    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        answer = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        # print(results)
        speak(answer)
        return answer

    elif 'music' in query:
        music_dir = 'C:\\Users\\Sayeesh Padti\\Music'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
        answer = "Ya sure starting........"
        speak(answer)
        return(answer)

    elif 'open gmail' in query:
        answer = "okay right on the way"
        webbrowser.open('www.gmail.com')
        speak(answer)
        return(answer)

    elif 'send an email' in query:
        try:
            speak("what should i send")
            print("what should i send")
            content = takeCommand()
            to = "vaishurohi2001@gmail.com"
            sendEmail(to, content)
            speak("email sent master")
            print("email sent master")
        except Exception as e:
            print(e)

    elif 'notepad' in query or 'open notepad' in query:
        answer = "opening notepad..."
        os.system("notepad.exe")
        speak(answer)
        return(answer)

    elif 'open recent activities' in query or 'recent activities' in query:
        answer = "letting you to recent activities....."
        os.startfile("C:\\Users\\Vaishnavi\\Recent")
        speak(answer)
        return(answer)

    elif 'firefox' in query or 'open firefox' in query:
        answer = "opening firefox..."
        os.startfile('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
        speak(answer)
        return(answer)

    elif 'chrome' in query or 'open chrome' in query:
        answer = "opening google chrome"
        os.startfile(
            'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
        speak(answer)
        return(answer)

    elif 'adobe photoshop' in query or 'open adope photoshop' in query:
        answer = "opening adobe photoshop"
        os.startfile(
            'C:\\Program Files (x86)\\Adobe\\Photoshop 7.0\\Photoshop.exe')
        speak(answer)
        return(answer)

    elif 'brackets' in query or 'open brackets' in query:
        val7 = "opening brackets"
        os.startfile('C:\\Program Files (x86)\\Brackets\\Brackets.exe')
        speak(val7)
        return(val7)

    elif 'wampserver' in query or 'open wamp64' in query:
        val8 = "opening wamp"
        speak(val8)
        os.startfile('C:\\wamp\\wampmanager.exe')
        return(val8)

    elif 'vmware' in query or 'open vmware' in query:
        val9 = "opening vmware"
        speak(val9)
        os.startfile(
            'C:\\Program Files (x86)\\VMware\\VMware Player\\vmplayer.exe')
        return(val9)

    elif 'character map' in query or 'open cmap' in query:
        val10 = "opening charctermap"
        speak(val10)
        os.startfile("charmap.exe")
        return(val10)

    elif 'paint' in query or 'open mspaint' in query:
        val11 = "opening paint"
        speak(val11)
        os.startfile("mspaint.exe")
        return(val11)

    elif 'steps recorder' in query or 'open steps recorder' in query:
        val12 = "opening step recorder"
        speak(val12)
        os.startfile("psr.exe")
        return(val12)

    elif 'player' in query or 'open wmplayer' in query:
        val13 = "opening widows media player"
        speak(val13)
        os.startfile('wmplayer.exe')
        return(val13)

    elif 'wordpad' in query or 'open wordpad ' in query:
        val14 = "opening wordpad"
        speak(val14)
        os.startfile('wordpad.exe')
        return(val14)

    elif 'quick assist' in query or 'open quick assist' in query:
        val15 = "opening quickassist"
        speak(val15)
        os.startfile('quickassist.exe')
        return(val15)

    elif 'component service' in query or 'open component service' in query:
        val16 = "opening component service"
        speak(val16)
        os.system("comexp.msc")
        return(val16)

    elif 'schedule' in query or 'open task scheduler' in query:
        val17 = "opening task scheduler"
        speak(val17)
        os.startfile("taskschd.msc ")
        return(val17)

    elif 'component management' in query or 'open component management' in query:
        val18 = "opening component management"
        speak(val18)
        os.startfile("compmgmt.msc")
        return(val18)

    elif 'system information' in query or 'open system information' in query:
        val19 = "opening system information"
        speak(val19)
        os.startfile("msinfo32.exe")
        return(val19)

    elif 'firewall' in query or 'open windows defender firewall' in query:
        val20 = "opening firewall settings"
        speak(val20)
        os.startfile("WF.msc")
        return(val20)

    elif 'calculator' in query or 'open calcy' in query:
        val21 = "opening calculator"
        speak(val21)
        os.startfile("C:\\Windows\\System32\\calc.exe")
        return(val21)

    elif 'volume mixer' in query or 'open sound settings' in query:
        val22 = "opening volume mixer"
        speak(val22)
        os.system("C:\\Windows\\System32\\SndVol.exe")
        return(val22)

    elif 'tell me about system performance' in query or 'open performance monitor' in query:
        val23 = "on the way to monitor performance"
        speak(val23)
        os.startfile("perfmon.msc")
        return(val23)

    elif 'control panel' in query or 'open control panel' in query:
        val24 = "opening control panel"
        speak(val24)
        os.system("Control.exe")
        return(val24)

    elif 'services' in query or 'services of my system' in query:
        val25 = "opening services"
        speak(val25)
        os.startfile("services.msc")
        return(val25)

    elif 'what time is it' or 'whats the time now' or 'time' in query:
        val26 = (datetime.datetime.now().strftime("%H:%M:%S"))
        speak(val26)
        return(val26)

    else:
        exit()
