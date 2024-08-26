import pyttsx3

def on_end_speech(name, completed):
    print("Speech completed")
    # You can add more code here to perform actions after speech

engine = pyttsx3.init()
engine.connect('finished-utterance', on_end_speech)

engine.say("Hey, I am good")
engine.runAndWait()

# Keep the script alive
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Exiting...")