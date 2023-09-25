import pyttsx3
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
if __name__ == '__main__':
    print("Welcome to RoboSpeaker. Created by Nikhil Garg")
    while True:
        text_input = input("Enter what you want me to speak: ")
        if text_input == "q":
            print("Bye bye friend")
            break
        speak_text(text_input)

