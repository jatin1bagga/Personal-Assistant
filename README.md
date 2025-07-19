Certainly! Here’s a professional and informative **README** file for your JARVIS project, summarizing its features, usage, and technical highlights based on the provided code and project context:

# JARVIS – AI-Based Personal Desktop Assistant

## Overview

**JARVIS** is a voice-activated Python desktop assistant designed to automate daily tasks, perform web searches, manage files, control hardware, and interact with applications on your computer. With integrations for speech recognition, natural language processing, and a user-friendly GUI, JARVIS brings intelligent automation and productivity right to your desktop.

## Features

- **Voice Commands:** Supports robust speech recognition for natural communication.
- **Task Automation:** Open/close Notepad, command prompt, control applications, play music, take screenshots, switch windows, and more.
- **Web Interaction:** Search Google, Wikipedia, YouTube, or launch websites and play videos/songs by command.
- **Messaging & Email:** Send WhatsApp messages and emails directly via your voice.
- **News Update:** Get latest news headlines with the integrated news API.
- **Location Services:** Identify your current city and country with IP lookup.
- **Jokes & Entertainment:** Listen to AI-curated jokes and control music playback.
- **Custom GUI:** Stylish PyQt5 interface to launch and monitor JARVIS.
- **PDF Reading & File Management:** Read PDF content aloud and hide/show folders as needed.
- **Intent Prediction:** Uses an ML model (trained with Logistic Regression) and command dataset to recognize and classify user intents.
- **Extensible Modules:** Modular codebase for easy addition of new features or command sets.

## Technologies Used

- **Python 3**
- **Libraries:**  
  - pyttsx3, speech_recognition, datetime, os, cv2, wikipedia, webbrowser, pywhatkit, pyautogui, openai, PyQt5, PyPDF2, requests, smtplib, torch, joblib, pyjokes
- **Machine Learning:**  
  - scikit-learn, Logistic Regression for intent recognition
- **GUI:**  
  - PyQt5
- **File & System Automation:**  
  - os, pyautogui

## Getting Started

1. **Clone/download** this repository.
2. **Install dependencies:**  
   ```
   pip install -r requirements.txt
   ```
3. **Train the intent recognition model** (run `intent_rec.py` if needed, or use provided `.pkl` files).
4. **Launch JARVIS** via the PyQt-based GUI:
   ```
   python gui.py
   ```

## Usage

- Click **Start JARVIS** in the GUI to activate.
- Interact via **voice commands** (e.g., "Open Notepad", "Play music", "Send email", "Tell me a joke", "Search Wikipedia for Python").
- Use the GUI power bar for status and the digital clock for utility.
- All modules (e.g., Notepad, WhatsApp, PDF, Instagram, Hide Files) are available via simple spoken commands.

## Directory Structure

```
JARVIS/
│
├── jarvis.py               # Main assistant logic
├── gui.py                  # PyQt5-based launcher GUI
├── notepad.py              # Notepad automation functions
├── pdf.py                  # PDF reading functions
├── hide_files.py           # File/folder visibility functions
├── instagram.py            # Instagram profile utility
├── intent_rec.py           # ML model training for intent recognition
├── jarvis_model.pkl        # Trained intent recognition model
├── jarvis_vectorizer.pkl   # Vectorizer for NLP
├── jarvis_commands_full.csv# Command-intent dataset
├── requirements.txt        # Python dependencies
```

## Sample Voice Commands

- “Open Notepad”
- “Play music”
- “Search Wikipedia for machine learning”
- “Send a WhatsApp message to Ansh”
- “Take screenshot”
- “Tell me the news”
- “Read pdf”
- “Hide folder”

## Credits

Developed by **Jatin Bagga**  
B.E. Computer Engineering, Thapar University

## License

This project is for educational and personal portfolio use.  
Adapt and extend as needed!

*For any issues or contributions, please contact [aloc1345@gmail.com](mailto:aloc1345@gmail.com).*
