from tkinter import*
import pyttsx3

root=Tk()
root.title("text to speach converter")

label= Label(root,text="enter text to convert to speach")
label.pack()

text_entry=Entry(root,width=50)
text_entry.pack()

def convert_to_speach():
    text=text_entry.get()
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

button =Button(root,text="convert",command=convert_to_speach)
button.pack()

root.mainloop()


