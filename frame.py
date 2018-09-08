import youtube_dl
from link import video
from tkinter import *

root = Tk()
frame = Frame(root)

# frame configs
frame.grid(row=0, column=0, sticky="nsew")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.geometry("1280x720")
root.title("Youtube to Mp3 Converter")
frame.configure(background='Grey')

# Entry Label & Naming
el = Label(frame, text="File Name:", font=("Calibri", 12)).grid(column=0, sticky=NW, pady=(10, 25))

e = Entry(frame, font=("Calibri", 17), width=29)
e.focus_set()
e.grid(row=1, column=0, pady=(0, 40), ipady=8)

# Label Menu
dpl = Label(frame, text="Download Entire Playlist:", font=("Calibri", 12)).grid(row=3, sticky=W)

tkvar = StringVar(root)
choices = {"True", "False"}
tkvar.set("False")

dplay_menu = OptionMenu(frame, tkvar, *choices)
dplay_menu.config(width=25, height=1, font=("Calibri", 17))
dplay_menu.grid(row=4, sticky=W, ipady=8)

# main link conversion
linkl = Label(frame, text="Input Link:", font=("Calibri", 20)).grid(row=2, column=2, padx=450)

e1 = Entry(frame, font=("Calibri", 14), width=70)
e1.focus_set()
e1.grid(row=3, column=2, ipady=10, pady=10)


# create a callback function for converting
def callback():
    if tkvar.get() == "True":
        d_playlist = True
    else:
        d_playlist = False
    name = e.get()
    link = e1.get()

    # converting
    video(link=link, name=name, d_plist=d_playlist).convert()


convertb = Button(frame, text="Convert", font=("Calibri", 20), width=15, command=callback).grid(row=4, column=2,
                                                                                                pady=(15, 0),
                                                                                                padx=(155, 0), sticky=W)

# TODO write a "terminate" function to break out anytime
# TODO find a way to print the logs on the screen
# TODO find a way to have it converting in the background so it doesn't make it seem like that it has stopped responding
# TODO Make try and except to catch empty converts
root.mainloop()
