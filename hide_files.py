import os

def hide(takecommand, speak):
    file_path = input("Give the path of folder you want to hide")
    speak("Sir please tell me you want to hide this folder or make it visible to everyone")
    condition = input()
    if "hide" in condition:
        os.system(f'attrib +h "{file_path}"')
        speak("Sir all of your files are now hidden")
        
    elif "visible" in condition:
        os.system(f'attrib -h "{file_path}"')
        speak("Sir, all the files in this folder are now visible to everyone")
    
    elif "leave it" in condition or "leave for now" in condition:
        speak("ok sir")