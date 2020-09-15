#importing os module for system command.
import os
#importing pyttsx3 for text to speech
import pyttsx3

print("Hi I am your virtual assistant")
pyttsx3.speak("Hi I am your virtual assistant")
print("\n\nMy name is bob")
pyttsx3.speak("My name is bob")



while True:

    print("\n\nHow can I help? ", end='')
    pyttsx3.speak("How can I help?")
    command = input().lower()


    #atom editor
    if ("atom" in command):

        pyttsx3.speak("launching atom")
        print("\n\nlaunching atom")
        os.system("atom")

    #Notepad

    elif (("run" in command) or ("execute" in command) or ("open" in command) or ("launch" in command)) and (("notepad" in command) or ("editor" in command) or ("notes" in command)):

        pyttsx3.speak("launching notepad")
        print("\n\nlaunching notepad")
        os.system("notepad")

    elif ("take" in command) or ("notes" in command):

        pyttsx3.speak("launching notepad for notes")
        print("\n\nlaunching notepad for notes")
        os.system("notepad")

    #edge
        """
        elif("microsoft" in command) and ("edge" in command):
            pyttsx3.speak("Launching edge")
            os.system("microsoft-edge")"""

    #BROWSER

    elif (("run" in command) or ("execute" in command) or ("open" in command) or ("launch" in command) or ("search" in command)) and  (("chrome" in command) or ("google" in command)):

        print("\n\nDo you want to search anything?", end='')
        print("Can i search for you", end='')
        pyttsx3.speak("Can i search for you ")
        search = input().lower()

        if ("yes" in search) or ("ok" in search):

            print("\n\nWhat do you want to search?")
            pyttsx3.speak("What do you want to search?")
            search = input().lower()

            if ("www." in command) or (".com" in command) or (".in" in command) or (".org" in command) or (".edu" in command):
                search = "chrome " +search
                pyttsx3.speak("launching chrome")
                os.system(search)
            else:
                search = "Chrome  https://www.google.com/search?q=\""+search+"\""
                print(search)
                print("Launching chrome")
                pyttsx3.speak("launching chrome")
                os.system(search)

        else:
            pyttsx3.speak("launching chrome")
            os.system("chrome")


    #youtube

    elif("youtube" in command):
        pyttsx3.speak("launching youtube")
        os.system("Chrome  youtube.com")



    #MOVIES AND TVS
    elif("Play" in command) and ("movie" in command) and ("windows player"):
        pyttsx3.speak("Launching windows player")
        os.system("microsoftvideo D:\Movie")

    #VLC MOVIES

    elif ("play" in command) and ("movie" in command):
        pyttsx3.speak("Playing movie")
        os.system("VLC D:\Movie\minions.mp4")




    #VLCSongs

    elif (("play" in command) or ("vlc" in command)) and (("song" in command) or ("songs" in command) or ("music" in command)):
        pyttsx3.speak("playing songs")
        os.system("vlc D:\Music")




    #Screen Recorder

    elif ("screen" in command) and (("recorder" in command) or ("recording" in command)):
        pyttsx3.speak("launching OBS Screen Recorder")
        os.system("obs-studio")


    #calculator

    elif ("calculator" in command) or ("calculation" in command) or ("maths" in command):
        pyttsx3.speak("launching calculator")
        os.system("calc")


    #alarm and clock

    elif ("alarm" in command) or ("clock" in command):
        pyttsx3.speak("opening clock and alarm")
        os.system("ms-clock")

    #camera

    elif ("camera" in command):
        pyttsx3.speak("opening camera")
        os.system("microsoft.windows.camera")

    #game

    elif ("game" in command) or ("candy crush" in command) or ("candy-crush" in command):
        pyttsx3.speak("opening candy crush")
        os.system("candycrushsodasaga")

    #calander

    elif ("calander" in command):
        pyttsx3.speak("opening calander")
        os.system("outlookcal")

    #mail

    elif ("mail" in command) or ("email" in command):
        print("\n\nlaunching mail")
        pyttsx3.speak("launching mail")
        os.system("	outlookmail")


    #Setting

    elif ("setting" in command) or ("settings" in command):
        print("\n\nlaunching setting")
        pyttsx3.speak("launching setting")
        os.system("start ms-settings:")


    #hi-how are you

    elif ("hi bob" in command) and ("how are you" in command):
        print("\n\nhi Nishant am I fine,How can I help?")
        pyttsx3.speak("hi nishant how can I help?")


    #hi

    elif ("hi" in command) or ("hello" in command):
        print("\n\nHi Nishant, can I help?")
        pyttsx3.speak("Hi Nishant, can I help?")

    #exit

    elif("exit" in command) or ("quit" in command):
        print("\n\nterminating process")
        pyttsx3.speak("terminating process")
        os.system("exit")
        break






    #Command not available

    else:
        print("\n\nThis program is corrently not available we will get back to you after an update")
        pyttsx3.speak("This program is currently not available we will get back to you after an update")
