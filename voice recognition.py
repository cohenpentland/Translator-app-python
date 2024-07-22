import customtkinter as ctk
from customtkinter import CTk, CTkEntry, CTkButton, CTkTextbox
import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to convert speech to text
def speech_to_text():
    with sr.Microphone() as source:
        try:
            scroll_text.insert(ctk.END, 'Now Listening  \n')
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            scroll_text.insert(ctk.END, 'spoken: ' + text + '\n'+ '\n')
        except sr.UnknownValueError:
            scroll_text.insert(ctk.END, "Sorry, I did not understand that.\n"+ '\n')
        except sr.RequestError:
            scroll_text.insert(ctk.END, "Sorry, my speech service is down.\n"+ '\n')

# Function to convert text to speech
def text_to_speech():
    text = entry_text.get()
    tts_engine.say(text)
    tts_engine.runAndWait()
    scroll_text.insert(ctk.END, 'written: ' + text + "\n"+ '\n')

# Create the main window
app = CTk()
app.geometry("500x500")

# Create the scrolled text widget
scroll_text = CTkTextbox(master=app)
scroll_text.pack(pady=20, padx=20, fill='both', expand=True)

# Create the text entry widget
entry_text = CTkEntry(master=app, placeholder_text= 'Enter text...')
entry_text.pack(pady=10, padx=20,side='right', fill='x')

# Create the buttons
btn_speech_to_text = CTkButton(master=app, text="Speech to Text", command=speech_to_text)
btn_speech_to_text.pack(pady=10, padx=20,side='left', fill='x')

btn_text_to_speech = CTkButton(master=app, text="Text to Speech", command=text_to_speech)
btn_text_to_speech.pack(pady=10)

# Run the GUI loop
app.mainloop()
