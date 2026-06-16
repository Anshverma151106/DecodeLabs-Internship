import datetime
import webbrowser
import pywhatkit as kit
import os
import ctypes
while True:
    query=input("You : ")
    query=query.lower()
    if("hello" in query or "helo" in query or "hlo" in query or "hallo" in query or "hii" in query or "hey" in query):
        print("Bot : hey ,I am Jarvis ,how can i help you")
    elif("bye" in query or "by" in query):
        print("Bot : Sir ,you can talk to me later")
        break
    elif("date" in query):
        print("Bot : Sir ,Todays date is ",datetime.datetime.now().strftime("%Y - %m - %d"))
    elif("time" in query):
        print("Bot : Sir ,time is ",datetime.datetime.now().strftime("%H : %M : %S"))
    elif("solve" in query or "slve" in query):
        try:
            print("Bot : Sir ,result is ",eval(query[5:]))
        except:
            print("Bot : Not correct Expression")
    elif("name" in query or "who" in query):
        print("Bot : I am Jarvis ,ready to help you what can i help you")
    elif("play" in query or "ply" in query):
        kit.playonyt(query)
    elif("search" in query):
        search=query.replace("search","")
        webbrowser.open(f"https://www.google.com/search?q={search}")
        print("Bot : Searching",search)
    elif("shutdown" in query):
        os.system("shutdown /s /t 10")
    elif("restart" in query):
        os.system("shutdown /r /t 10")
    elif("lock" in query):
        ctypes.windll.user32.LockWorkStation()
    else:
        print("Bot : I don't recognize can you rephrase the query")