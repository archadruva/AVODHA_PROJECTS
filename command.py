from tkinter import*
import pyttsx3

root=Tk()
root.title("text to speach")


engine = pyttsx3.init()
engine.say("hello im meera")
engine.runAndWait()

root.mainloop()

