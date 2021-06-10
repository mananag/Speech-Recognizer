import pyttsx3

engine = pyttsx3.init()
engine.setProperty("languages", 'hi')
engine.say("अच्छा")
print(engine.getProperty("languages"))
engine.runAndWait()
