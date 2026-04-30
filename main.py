# Chappie AI Voice Assistant

This is the main entry point for the Chappie AI voice assistant. The functionality includes:

- Voice recognition
- Natural language processing
- Responses to user queries

## Requirements
Make sure to have the following packages installed:
- SpeechRecognition
- pyttsx3
- numpy

## Running the Assistant
Run this script to start the Chappie AI voice assistant.

```python
import speech_recognition as sr
import pyttsx3

class ChappieAI:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.speaker = pyttsx3.init()

    def speak(self, text):
        self.speaker.say(text)
        self.speaker.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio)
                return command
            except sr.UnknownValueError:
                return 'Sorry, I did not understand that.'
            except sr.RequestError:
                return 'Could not request results from Google Speech Recognition service.'

    def run(self):
        while True:
            command = self.listen()
            print(f'You said: {command}')
            self.speak('You said: ' + command)

if __name__ == '__main__':
    assistant = ChappieAI()
    assistant.run()