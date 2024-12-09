import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech engine for text-to-speech
engine = pyttsx3.init()

# Function for speaking text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your command...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"Your command: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Sorry, the service is down.")
        return None

# Main function to process commands
def voice_assistant():
    speak("Hello! How can I assist you today?")
    
    while True:
        command = listen()
        if command:
            if "hello" in command:
                speak("Hello! How are you today?")
            elif "time" in command:
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M:%S")
                speak(f"The current time is {current_time}")
            elif "date" in command:
                today = datetime.date.today()
                speak(f"Today's date is {today}")
            elif "search" in command:
                search_query = command.replace("search", "").strip()
                speak(f"Searching for {search_query}")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
            elif "stop" in command:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I did not understand that command.")

# Run the assistant
if __name__ == "__main__":
    voice_assistant()