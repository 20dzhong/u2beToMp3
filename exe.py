import youtube_dl
import subprocess
from logs_utils import *
from link import *
from tkinter import *
import time


root = Tk()
frame = Frame(root)

# frame configs
frame.grid(row=0, column=0, sticky="nsew")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.geometry("1280x720")
root.title("Youtube to Mp3 Converter")
frame.configure(background='#ededed')

# Entry Label & Naming
el = Label(frame, text="File Name:", font=("Calibri", 12)).grid(column=0, sticky=NW, pady=(10, 25))
e = Entry(frame, font=("Calibri", 17), width=29)
e.focus_set()
e.grid(row=1, column=0, pady=(0, 40), ipady=8)

# Label Menu for drop down list
dpl = Label(frame, text="Download Entire Playlist:", font=("Calibri", 12)).grid(row=3, sticky=W)
tkvar = StringVar(root)
choices = {"True", "False"}
tkvar.set("False")

dplay_menu = OptionMenu(frame, tkvar, *choices)
dplay_menu.config(width=25, height=1, font=("Calibri", 17))
dplay_menu.grid(row=4, sticky=W, ipady=8)

# main link conversion, link entry box
linkl = Label(frame, text="Input Link:", font=("Calibri", 20)).grid(row=2, column=2, padx=450)
e1 = Entry(frame, font=("Calibri", 14), width=70)
e1.focus_set()
e1.grid(row=3, column=2, ipady=10, pady=10)

# create output as a global variable so that it could be altered later
output = StringVar()
output.set("")

new_log = logs_var("")

# create a callback function for converting
def callback():
    if tkvar.get() == "True":
        d_playlist = True
    else:
        d_playlist = False

    try:
        name = e.get()
        if name == '': raise Empty_Name
        link = e1.get()
        if link == '': raise Empty_Link
        start_time = time.time()
        output.set(new_log.concat("Processing, please wait..."))
        video(link=link, name=name, d_plist=d_playlist).convert()
        elapsed_time = time.time() - start_time
        output.set(new_log.concat("Process finished! It took " + str(elapsed_time) + " to finish"))

    except Empty_Name:
        output.set(new_log.concat("Empty name! Please enter a name to proceed"))

    except Empty_Link:
        output.set(new_log.concat("Empty link! Please enter a link to proceed"))

    except:
        output.set(new_log.concat("Unacceptable link or name, please try entering a new one."))


convertb = Button(frame, text="Convert", font=("Calibri", 20), width=15, command=callback)
convertb.grid(row=4, column=2, pady=(15, 0), padx=(155, 0), sticky=W)

# logs
logl = Label(frame, text="Logs:", font=("Calibri", 12)).grid(row=5, column=2, pady=15, sticky=W, padx=(155, 0))
log_output = Label(frame, textvariable=str(output), relief=SUNKEN, font=("Consolas", 12), anchor='w', wraplength=1000)
log_output.grid(row=6, column=2, padx=(155, 0), sticky=W)


# TODO write a "terminate" function to break out anytime
# TODO make the words towards the left
root.mainloop()

