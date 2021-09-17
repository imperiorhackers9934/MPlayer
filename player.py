from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from pygame import mixer
from PIL import Image, ImageTk
from mutagen.mp3 import MP3
import os

root = Tk()
root.geometry("800x300")
root.resizable(False, False)
root.title("Audio Player - V-0.1 (Beta)")
v1 = DoubleVar()
ico = Image.open('Icon.png')
ick = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, ick)
Label(root,text="Choose a Audio that you Want to Play").place(x=35,y=0)
mixer.init()
#Music Photo
player = PhotoImage(file="play1.png")
p = Label(root,image=player,width=300,height=220)
p.place(x=20,y=0)
#Scroll
sb = Scrollbar(root, orient='vertical')  
sb.pack(side=RIGHT,fill=Y)
condn = True
#Play Selected Song
def play(song):
    mixer.music.load(song)
    mixer.music.play()
    s1.set(0)
    a.config(text="Pause",command=pau)
    y["state"] = "normal"
    z["state"] = "disabled"
    play.audio = MP3(song)
    
#Event Functions    
def my1(event):
    global condn
    condn = False
def my2(event):
    global condn
    condn = True
    myposn()

#Select a Song
def open():
    filepath = fd.askdirectory(
        title='Select a Music Path',
        initialdir='/')
    try:    
        #List of Songs
        for r, d, f in os.walk(filepath):
            for file in f:
                if ".mp3" in file:
                    open.varl = r
                    #print(os.path.join(r, file))
                    for line in range(1):  
                        mylist.insert(END, file)
        a["state"] = "normal"
        a.config(text="Play",command=select)
    except Exception as e:
        messagebox.showerror("Error", "Something went Wrong")
        print(e)

#Sets the Position of song according to Position of Slidebar    
def cposn(event):
    a = s1.get()
    mixer.music.set_pos(a)
    
    
#Sets the maximum value of Slidebar according to time of song     
def gposn():
    audio_info = play.audio.info    
    length_in_secs = int(audio_info.length)
    s1.config(to=length_in_secs)
    
#Gets the Position of Music and Sets it to Slidebar
def myposn():
    current = mixer.music.get_pos()
    if(condn):   
        if mixer.music.get_busy():
            s1.set(current/1000)
            root.after(1000,lambda:myposn())
            #a.after(1000,lambda:myposn())
        #elif(current/1000 == gposn.length_in_secs):
    #    stop()    
    
#For Getting full path of Song and Playing it
def select():
    for i in mylist.curselection():
        play(os.path.join(open.varl,mylist.get(i)))
        gposn()
        myposn()
while(True):
    def pau():
        mixer.music.pause()
        a.config(text="Resume",command = unpau)
    def unpau():
        mixer.music.unpause()
        myposn()
        a.config(text="Pause",command = pau)
    def stop():
        mixer.music.stop()
        a.config(text="Play",command=select)
        a["state"] = "normal"
        z["state"] = "disabled"
        y["state"] = "disabled"
        
    break
    
z = Button(root, text="Select Path",command = open)
z.place(x=100,y=250)
y = Button(root, text="Stop",command = stop)
y.place(x=40,y=250)
a = Button(root, text="Pause",command = pau)
a.place(x=190,y=250)

a["state"] = "disabled"
y["state"] = "disabled"



s1 = Scale( root, variable = v1,from_ = 0, to = 0,orient = VERTICAL, command=cposn, length=230)
s1.place(x=320,y=10)
s1.bind('<Button-1>',my1)
s1.bind('<ButtonRelease-1>',my2)
mylist = Listbox(root,yscrollcommand=sb.set,width=62,height=18,selectmode=SINGLE)
mylist.place(x=390,y=0)  

sb.config(command=mylist.yview)

root.mainloop() 