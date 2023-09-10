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
import subprocess
from sound import Sound
import keyboard


def return_value(ans):
    return ans


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
    query = query.lower()
    print(query)
    if query == 'hello' or query == 'hi':
        answer = "hi am jarvis"
        speak(answer)
        return answer

    elif 'your name' in query or 'who are you' in query:
        answer = "My name is Jarvis, at your service"
        speak(answer)
        return answer

    elif 'whats up' in query or 'how are you' in query:
        answer = "I am fine  thankyou"
        # speak(answer)
        return answer

    elif 'something about you' in query:
        answer = "In the Marvel Cinematic Universe  i was an AI developed by Tony Stark first primarily as being and artificial assistant in his house, and later modified to perform a lot of functions in the Mark 2 and now presently implemented by my group"
        speak(answer)
        return answer

    elif 'how will be my day' in query:
        answer = "wish that it will be good"
        speak(answer)
        return answer

    elif 'hangout jarvis' in query:
        answer = "Sorry  i would love to but i cant"
        speak(answer)
        return answer

    elif 'who am i jarvis' in query:
        answer = "you are my master"
        speak(answer)
        return answer

    elif 'can you be my friend' in query:
        answer = "Its my pleasure to be"
        speak(answer)
        return answer

    elif 'are you tired' in query:
        answer = "no master full of energy...."
        speak(answer)
        return answer

    elif 'goodbye jarvis' in query:
        answer = "goodbye have a nice day......"
        speak(answer)
        return answer

    elif 'HOD of cs department' in query:
        answer = "vinay bhat is the hod of cs department"
        speak(answer)
        return answer

    elif 'about gpt karwar' in query:
        answer = "government polytechnic college is a polytechnic college in uttar kannada district of karnatka,india situated in karwar "
        speak(answer)
        return answer

    elif 'mechanical department HOD' in query or 'HOD of mechanical department' in query:
        answer = "shantaram is the HOD of mechanical department"
        speak(answer)
        return answer

    elif 'branches in gpt karwar' in query:
        answer = "there are seven branches in gpt karwar they are computer  science and  engineering,  civil  engineering, mechanical  engineering,  automobile  engineering,  commercial  pratice  and  electrical engineering"
        speak(answer)
        return answer

    elif 'sayyan shaikh' in query or 'saiyan shaikh' in query:
        answer = "sayyan shaikh is a lecturer of computer science department"
        speak(answer)
        return answer

    elif 'rashmi vernekar' in query:
        answer = "rashmi vernekar is a lecturer of computer science department"
        speak(answer)
        return answer

    elif 'subjects in computer science department?' in query:
        answer = "there are six subjects in first and second semester, eight subjects in third fourth and fifth semester, seven subjects in sixth semester"
        speak(answer)
        return answer

    elif 'subjects are there in first semester?' in query:
        answer = "Engineering mathematics 1, applied science,concepts of electrical and electronics engineering,applied science lab,basic electronic lab,basic computer skills lab"
        speak(answer)
        return answer

    elif 'subjects are there in second semester?' in query:
        answer = "Engineering mathematics 2,Communication skills in English,Digital computer fundamentals,Multimedia lab,Basic web designing lab,Digital electronics lab"
        speak(answer)
        return answer

    elif 'subjects are there in third semester?' in query:
        answer = "Programming with c,Computer Organization,Database Management System ,computer network,network administration lab,dbms and GUI lab,Programming with c lab"
        speak(answer)
        return answer

    elif 'subjects are there in fourth semester?' in query:
        answer = "Data structure,Programming with Java,Operating system,Professional ethics and Indian Constitution,Tantrika Kannada and Kannada Kali,OOP with Java lab,Linux lab,Data structure lab"
        speak(answer)
        return answer

    elif 'subjects are there in fifth semester?' in query:
        answer = "Software engineering,Web programming,Design and analysis of algorithm,Green computing,Web programming lab,Design and analysis of algorithm lab,Professional practices,Project work one"
        speak(answer)
        return answer

    elif 'subjects are there in sixth semester?' in query:
        answer = "Software testing,Network security,Internet of things,Software testing lab,Implant training,Project work two"
        speak(answer)
        return answer

    elif '.com' in query:
        os.startfile(
            "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
        webbrowser.open('http://www.'+query)
        op = f'opening  '+query
        return(op)

    elif 'open cmd' in query or 'open command prompt' in query:
        os.system("start cmd")
        answer = "opening command prompt"
        speak(answer)
        return(answer)

    elif 'camera' in query:
        answer = "opening camera"
        speak("opening camera")
        subprocess.run('start microsoft.windows.camera:', shell=True)
        return(answer)

    elif 'date' in query:
        today = date.today()
        ans = f"Today's date is :, {today}"
        speak(ans)
        return ans

    elif 'find location' in query:
        speak(print("What loaction you want to find"))
        location = takeCommand()
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        ans = f'Here are the result of location '+location
        speak(ans)
        return ans

    elif 'hibernate' in query:
        speak("good night master")
        answer = "good night master"
        os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
        return(answer)

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
        answer = "adjusting brightness...."
        return(answer)

    elif 'shutdown' in query:
        answer = "Do you want to shutdown your system? (yes/no)"
        speak(answer)
        a = takeCommand()
        if 'yes' in a:
            os.system("shutdown /s /t 1")
            shut = "shuttind down...."
            return(shut)
        elif 'no' in a:
            exit()
        return(answer)

    elif 'restart' in query:
        answer = "Do you want to shutdown your system? (yes/no)"
        speak(answer)
        a = takeCommand()
        if 'yes' in a:
            os.system("shutdown /r /t 1")
            rest = "restarting pc"
            return(rest)
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
        music_dir = 'C:\\Users\\Vaishnavi\\Music'
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

    elif 'send' in query:
        try:
            speak("what should i send")
            print("what should i send")
            content = takeCommand()
            to = 'anupadti@gmail.com'
            sendEmail(to, content)
            speak("email sent master")
            print("email sent master")
        except Exception as e:
            print(e)

    elif 'notepad' in query or 'open notepad' in query:
        answer = "opening notepad..."
        return_value(answer)
        speak(answer)
        os.system("notepad.exe")
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
        answer = "opening brackets"
        os.startfile('C:\\Program Files (x86)\\Brackets\\Brackets.exe')
        speak(answer)
        return(answer)

    elif 'wamp' in query or 'open wamp64' in query:
        answer = "opening wampserver"
        speak(answer)
        os.startfile(
            'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Wampserver64\\Wampserver64.lnk')
        return(answer)

    elif 'vmware' in query or 'open vmware' in query:
        answer = "opening vmware"
        speak(answer)
        os.startfile(
            'C:\\Program Files (x86)\\VMware\\VMware Player\\vmplayer.exe')
        return(answer)

    elif 'character map' in query or 'open cmap' in query:
        answer = "opening charctermap"
        speak(answer)
        os.startfile("charmap.exe")
        return(answer)

    elif 'paint' in query or 'open paint' in query or 'open paint' in query:
        answer = "opening paint"
        speak(answer)
        os.startfile("mspaint.exe")
        return(answer)

    elif 'steps recorder' in query or 'open steps recorder' in query:
        answer = "opening step recorder"
        speak(answer)
        os.startfile("psr.exe")
        return(answer)

    elif 'player' in query or 'open wmplayer' in query:
        answer = "opening windows media player"
        speak(answer)
        os.startfile('wmplayer.exe')
        return(answer)

    elif 'wordpad' in query or 'open wordpad ' in query:
        answer = "opening wordpad"
        speak(answer)
        os.startfile('wordpad.exe')
        return(answer)

    elif 'quick assist' in query or 'open quick assist' in query:
        answer = "opening quickassist"
        speak(answer)
        os.startfile('quickassist.exe')
        return(answer)

    elif 'component services' in query or 'open component services' in query:
        answer = "opening component service"
        speak(answer)
        os.system("comexp.msc")
        return(answer)

    elif 'scheduler' in query or 'open task scheduler' in query:
        answer = "opening task scheduler"
        speak(answer)
        os.startfile("taskschd.msc ")
        return(answer)

    elif 'component management' in query or 'open component management' in query:
        answer = "opening component management"
        speak(answer)
        os.startfile("compmgmt.msc")
        return(answer)

    elif 'system information' in query or 'open system information' in query:
        answer = "opening system information"
        speak(answer)
        os.startfile("msinfo32.exe")
        return(answer)

    elif 'firewall' in query or 'open windows defender firewall' in query:
        answer = "opening firewall settings"
        speak(answer)
        os.startfile("WF.msc")
        return(answer)

    elif 'calculator' in query or 'open calcy' in query:
        answer = "opening calculator"
        speak(answer)
        os.startfile("C:\\Windows\\System32\\calc.exe")
        return(answer)

    elif 'tell me about system performance' in query or 'open performance monitor' in query:
        answer = "on the way to monitor performance"
        speak(answer)
        os.startfile("perfmon.msc")
        return(answer)

    elif 'control panel' in query or 'open control panel' in query:
        answer = "opening control panel"
        speak(answer)
        os.system("Control.exe")
        return(answer)

    elif 'services' in query or 'services of my system' in query:
        answer = "opening services"
        speak(answer)
        os.startfile("services.msc")
        return(answer)

    elif 'time' in query:
        answer = (datetime.datetime.now().strftime("%H:%M:%S"))
        speak(answer)
        return(answer)

    elif 'Microsoft word' in query or 'word' in query:
        answer = "Opening Microsoft Word"
        os.startfile(
            'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007.lnk')
        speak(answer)
        return answer

    elif 'Microsoft access' in query or 'access' in query:
        answer = "Opening Microsoft Access"
        os.startfile(
            'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Access 2007.lnk')
        speak(answer)
        return(answer)

    elif 'Microsoft powerpoint' in query or 'powerpoint' in query:
        answer = "Opening Microsoft Powerpoint"
        os.startfile(
            'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office PowerPoint 2007.lnk')
        speak(answer)
        return(answer)

    elif 'Microsoft excel' in query or 'excel' in query:
        answer = "Opening Microsoft Excel"
        os.startfile(
            'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007.lnk')
        speak(answer)
        return(answer)

    elif 'adobe' in query:
        os.startfile(
            "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Acrobat Reader DC.lnk")
        answer = "opening adobe acrobat reader dc...."
        speak(answer)
        return(answer)

    elif 'exit' in query or 'stop' in query:
        ans = 'good bye'
        speak(ans)
        exit()
        return ans

    else:
        ans = "sorry i didn't get that     say that again     or try typing the command    "
        speak(ans)
        return ans
