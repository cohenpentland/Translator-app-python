🗣️ Voice Assistant App (with Login, Speech-to-Text, and Translation)




![project-1](https://github.com/user-attachments/assets/e260a231-1dab-4f48-b288-3823abe5d40f)





This Python desktop application, built with customtkinter, combines speech recognition, text-to-speech, and translation functionalities in a user-friendly graphical interface. It includes a basic login screen and leverages OpenAI's GPT API for real-time language translation.
📦 Features

    🔐 Login Screen: Basic login with username and password check.

    🎙️ Speech to Text: Convert spoken words to text using Google Speech Recognition.

    🗣️ Text to Speech: Convert written text to audio output.

    🌐 Translation Support: Optional translation of spoken or written text via OpenAI API (supports English ↔ Japanese).

    ⚙️ Options Menu: Adjust the TTS engine volume with a slider.

🛠️ Technologies Used

    customtkinter - For modern-looking GUI elements.

    speech_recognition - For converting spoken input to text.

    pyttsx3 - For offline text-to-speech.

    openai - For translation (via GPT model).

    tkinter - Underlying GUI framework.

🔑 Setup
1. Clone the Repository

git clone https://github.com/your-repo/voice-assistant-app.git
cd voice-assistant-app

2. Install Requirements

pip install customtkinter speechrecognition pyttsx3 openai

    🔄 You may also need to install pyaudio. On Windows:

    pip install pipwin
    pipwin install pyaudio

3. Add Your OpenAI API Key

Open the script and replace this line:

openai.api_key = ''

with:

openai.api_key = 'your-openai-api-key'

4. Run the App

python your_script_name.py

🔐 Default Login Credentials

    Username: admin

    Password: password

You can change these credentials in the login() method of the LoginApp class.
📋 Notes

    Requires an internet connection for translation and speech recognition.

    Speech features work best with a clear microphone input.

    The app supports basic fade-in/fade-out transitions between login and main interface.

🚀 Future Improvements

    Persistent user authentication (e.g., with hashed passwords and database).

    Expand supported translation languages.

    Speech-to-speech translation mode.

    Save transcription logs.

🧑‍💻 Author

Cohen Pentland
