import sys
import pyttsx3
import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QProgressBar
from PyQt5.QtCore import Qt, QTimer
import subprocess  # Import subprocess to run external scripts
from PyQt5.QtGui import QFont
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

class JarvisLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('JARVIS Launcher')
        self.setGeometry(500, 200, 500, 400)
        self.setStyleSheet("background-color: #0d0d0d;")  # Dark background

        # Layout
        layout = QVBoxLayout()

        # Title
        self.title = QLabel('J.A.R.V.I.S')
        self.title.setFont(QFont('Orbitron', 32))
        self.title.setStyleSheet('color: cyan')
        self.title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title)

        # Clock
        self.clock = QLabel()
        self.clock.setFont(QFont('Orbitron', 16))
        self.clock.setStyleSheet('color: #00ffff')
        self.clock.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.clock)

        # Power Bar
        self.power = QProgressBar()
        self.power.setValue(100)
        self.power.setTextVisible(True)
        self.power.setStyleSheet(""" 
            QProgressBar {
                border: 2px solid #00ffff;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #00ffff;
                width: 10px;
            }
        """)
        layout.addWidget(self.power)

        # Start Button
        self.button = QPushButton('Start JARVIS')
        self.button.setFont(QFont('Orbitron', 18))
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #0d0d0d;
                color: cyan;
                border: 2px solid cyan;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: cyan;
                color: black;
            }
        """)
        self.button.clicked.connect(self.start_jarvis)
        layout.addWidget(self.button)

        self.setLayout(layout)

        # Timer for updating clock
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)  # every second
        self.update_clock()

    def update_clock(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.clock.setText(current_time)

    def start_jarvis(self):
        speak("Starting Jarvis. All systems online.")
        print("Jarvis Started!")  # Here you can add your main program launch

        # Replace 'other_script.py' with the actual Python script you want to run
        subprocess.Popen(["python", "C:\\Users\\Jatin bagga\\Desktop\\ML\\JARVIS\\jarvis.py"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = JarvisLauncher()
    window.show()
    sys.exit(app.exec_())
