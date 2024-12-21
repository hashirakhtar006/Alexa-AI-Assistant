import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLiberary

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def open_youtube_and_search():
    # Open YouTube
    webbrowser.open('https://www.youtube.com')  
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for search query...")
        audio = recognizer.listen(source)
        try:
            search_term = recognizer.recognize_google(audio)
            print(f"Search term: {search_term}")
            # Perform the search on YouTube
            search_url = f"https://www.youtube.com/results?search_query={search_term}"
            webbrowser.open(search_url)
            print(f"Searching for '{search_term}' on YouTube.")
        except Exception as e:
            print(f"Error: {e}")

def open_google_and_search():
    webbrowser.open('https://www.google.com')  # Open Google
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for search query...")
        audio = recognizer.listen(source)
        try:
            search_term = recognizer.recognize_google(audio)
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
            print(f"Searching for '{search_term}' on Google.")
        except Exception as e:
            print("Sorry, I couldn't understand that.")            


def ProcessCommand(c):
    if 'open google' in c.lower():
        open_google_and_search()
        speak("Opening Google")
    elif 'open youtube' in c.lower():
        open_youtube_and_search()
        speak("Opening YouTube")
    elif 'open facebook' in c.lower():
        webbrowser.open('https://www.facebook.com')
        speak("Opening Facebook")
    elif 'open whatsapp' in c.lower():
        webbrowser.open('https://web.whatsapp.com')
        speak("Opening Whatsapp")
    # elif c.lower().startswith("play"):
    #     song = c.lower().split(" ")[1]
    #     link = musicLiberary.music[song]
    #     webbrowser.open(link)
    elif 'play' in c.lower():
        song = c.lower().split(" ")[1]
        link = musicLiberary.music[song]
        webbrowser.open(link)

if __name__ == "__main__":
    speak("Initializing Alexa...")
    speak('How may I assit you Today?')

    while True:
        print("Listening for 'Alexa'...")

        try:
            with sr.Microphone() as source:
                # Adjust the microphone sensitivity once instead of each time
                print("Listening...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)  # Reduced timeout and phrase time limit
                word = recognizer.recognize_google(audio)
                print(f"You said: {word}")

                if 'alexa' in word.lower():  # Trigger when 'Alexa' is heard
                    speak("Yes Sir?")
                    

                    # Listen for the next command after "Alexa"
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
                    command = recognizer.recognize_google(audio)

                    ProcessCommand(command)  # Process the command

        except Exception as e:
            print(f"Error occurred: {e}")
            continue  # Continue the loop even after an error
