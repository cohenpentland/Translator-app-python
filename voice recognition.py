import customtkinter as ctk
from customtkinter import CTk, CTkEntry, CTkButton, CTkTextbox
import speech_recognition as sr
import pyttsx3
import tkinter as tk  # Import tkinter for IntVar

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Initialize tkinter variable for translate switch


# Function to convert speech to text
def speech_to_text():
    with sr.Microphone() as source:
        if translate_var.get() == 0:  # Use the get method for IntVar
            try:
                scroll_text.insert(ctk.END, 'Now Listening...\n')
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                scroll_text.insert(ctk.END, 'Spoken: ' + text + '\n\n')
            except sr.UnknownValueError:
                scroll_text.insert(ctk.END, "Sorry, I did not understand that.\n\n")
            except sr.RequestError:
                scroll_text.insert(ctk.END, "Sorry, my speech service is down.\n\n")
        else:


            scroll_text.insert(ctk.END, 'hello: ')

# Function to convert text to speech
def text_to_speech():  
    text = entry_text.get()
    tts_engine.say(text)
    tts_engine.runAndWait()
    scroll_text.insert(ctk.END, 'Written: ' + text + "\n\n")

# Create the main window
app = CTk()
app.geometry("600x600")
app.title("Speech to Text and Text to Speech")

translate_var = tk.IntVar(value=0)

# Create the scrolled text widget
scroll_text = CTkTextbox(master=app, width=580, height=300)
scroll_text.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Create the text entry widget
entry_text = CTkEntry(master=app, placeholder_text='Enter text...')
entry_text.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

# Create the buttons
btn_speech_to_text = CTkButton(master=app, text="Speech to Text", command=speech_to_text)
btn_speech_to_text.grid(row=1, column=0, padx=10, pady=10, sticky="w")

btn_text_to_speech = CTkButton(master=app, text="Text to Speech", command=text_to_speech)
btn_text_to_speech.grid(row=1, column=2, padx=10, pady=10, sticky="e")

# Create the toggle switch
tgl_translate = ctk.CTkSwitch(master=app, text="Translate text", variable=translate_var, onvalue=1, offvalue=0)
tgl_translate.grid(row=4, column=0, padx=10, pady=10, sticky="w")

# Create the option menu (empty, configure as needed)
drp_translate = ctk.CTkOptionMenu(master=app, values = ['english', 'japanese'])
drp_translate.grid(row=2, column=0, padx=10, pady=10, sticky="we")

# Configure the grid to adjust properly on resizing
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)

# Run the GUI loop
app.mainloop()
