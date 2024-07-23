import customtkinter as ctk
from customtkinter import CTk, CTkEntry, CTkButton, CTkTextbox, CTkSwitch, CTkOptionMenu
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import messagebox
import openai

openai.api_key = ''

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

class LoginApp(CTk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("600x600")

        self.create_login_widgets()

    def create_login_widgets(self):
        # Configure grid to center the widgets
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.username_label = ctk.CTkLabel(self, text="Username")
        self.username_label.grid(row=2, column=1, padx=10, pady=10, sticky="e")
        self.username_entry = ctk.CTkEntry(self)
        self.username_entry.grid(row=2, column=2, padx=10, pady=10, sticky="w")

        self.password_label = ctk.CTkLabel(self, text="Password")
        self.password_label.grid(row=3, column=1, padx=10, pady=10, sticky="e")
        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.grid(row=3, column=2, padx=10, pady=10, sticky="w")

        self.login_button = ctk.CTkButton(self, text="Login", command=self.login)
        self.login_button.grid(row=4, column=2, padx=10, pady=10, sticky="")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Replace the following lines with your actual username and password validation
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome!")
            self.fade_to_main_app()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def fade_to_main_app(self):
        self.fade_out(self.create_main_app_widgets)

    def fade_out(self, callback, step=0.05):
        alpha = self.attributes('-alpha')
        if alpha > 0:
            alpha -= step
            self.attributes('-alpha', alpha)
            self.after(50, lambda: self.fade_out(callback, step))
        else:
            callback()
            self.fade_in()

    def fade_in(self, step=0.05):
        alpha = self.attributes('-alpha')
        if alpha < 1:
            alpha += step
            self.attributes('-alpha', alpha)
            self.after(50, lambda: self.fade_in(step))

    def create_main_app_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.geometry("600x600")
        self.title("Speech to Text and Text to Speech")

        self.translate_var = tk.IntVar(value=0)

        # Create the scrolled text widget
        self.scroll_text = CTkTextbox(master=self, width=580, height=300)
        self.scroll_text.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Create the text entry widget
        self.entry_text = CTkEntry(master=self, placeholder_text='Enter text...')
        self.entry_text.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

        # Create the buttons
        self.btn_speech_to_text = CTkButton(master=self, text="Speech to Text", command=self.speech_to_text)
        self.btn_speech_to_text.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.btn_text_to_speech = CTkButton(master=self, text="Text to Speech", command=self.text_to_speech)
        self.btn_text_to_speech.grid(row=1, column=2, padx=10, pady=10, sticky="e")

        # Create the toggle switch
        self.tgl_translate = CTkSwitch(master=self, text="Translate text", variable=self.translate_var, onvalue=1, offvalue=0)
        self.tgl_translate.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        # Create the option menu (empty, configure as needed)
        self.drp_translate = CTkOptionMenu(master=self, values=['english', 'japanese'])
        self.drp_translate.grid(row=2, column=0, padx=10, pady=10, sticky="we")

        language = self.drp_translate.get()  # Get the selected language
        # Configure the grid to adjust properly on resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        

    def speech_to_text(self):
        with sr.Microphone() as source:
            if self.translate_var.get() == 0:
                try:
                    self.scroll_text.insert(ctk.END, 'Now Listening...\n')
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)
                    text = recognizer.recognize_google(audio)
                    self.scroll_text.insert(ctk.END, 'Spoken: ' + text + '\n\n')
                except sr.UnknownValueError:
                    self.scroll_text.insert(ctk.END, "Sorry, I did not understand that.\n\n")
                except sr.RequestError:
                    self.scroll_text.insert(ctk.END, "Sorry, my speech service is down.\n\n")
            else:
                try:
                    language = self.drp_translate.get()  # Get the selected language
                    
                    self.scroll_text.insert(ctk.END, 'Now Listening...\n')
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)
                    text = recognizer.recognize_google(audio)
                    
                    prompt = f"Translate this text to {language}: {text}"
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": prompt}
                        ],
                        max_tokens=150
                    )
    
                    translated_text = response.choices[0].message['content'].strip()
                    self.scroll_text.insert(ctk.END, 'Translated: ' + translated_text + '\n\n')
    
                except sr.UnknownValueError:
                    self.scroll_text.insert(ctk.END, "Sorry, I did not understand that.\n\n")
                except sr.RequestError:
                    self.scroll_text.insert(ctk.END, "Sorry, my speech service is down.\n\n")
    
    def text_to_speech(self):   
        if self.translate_var.get() == 0:   
            try:    
                text = self.entry_text.get()
                tts_engine.say(text)
                tts_engine.runAndWait()
                self.scroll_text.insert(ctk.END, 'Written: ' + text + "\n\n")
            except sr.UnknownValueError:
                    self.scroll_text.insert(ctk.END, "Sorry, I did not understand that.\n\n")
            except sr.RequestError:
                    self.scroll_text.insert(ctk.END, "Sorry, my speech service is down.\n\n")       
    
                
        
        else:
            try:
                language = self.drp_translate.get()  # Get the selected language
                
                text = self.entry_text.get()
                prompt = f"Translate this text to {language}: {text}"
                response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "you only provide the translation no additinal text"},
                            {"role": "user", "content": prompt}
                        ],
                        max_tokens=150
                    )
                translated_text = response.choices[0].message['content'].strip()

                self.scroll_text.insert(ctk.END, 'Translated: ' + translated_text + '\n\n')

                tts_engine.say(translated_text)

                tts_engine.runAndWait()

            except sr.UnknownValueError:
                    self.scroll_text.insert(ctk.END, "Sorry, I did not understand that.\n\n")
            except sr.RequestError:
                    self.scroll_text.insert(ctk.END, "Sorry, my speech service is down.\n\n")
            
            
                


if __name__ == "__main__":
    login_app = LoginApp()
    login_app.mainloop()
