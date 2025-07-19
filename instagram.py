import webbrowser
import time
from instadownloader import instaloader
def instagram(speak, query, takecommand):
    if "instagram profile" in query:
        speak("please enter the username")
        name = input("enter the username here: ")
        webbrowser.open(f"www.indtagram.com/{name}")
        time.sleep(5)
        speak("Sir, do you want to download the profile pic? ")
        condition = takecommand().lower()
        if "yes" in condition:
            mod = input
            mod.download_profile(name, profile_pic_only=True)
        else:
            pass