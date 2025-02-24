import tkinter
from tkinter import *
import tkinter as tk
from tkinter import PhotoImage
from tkinter import Listbox, END
import customtkinter

from tkinter import messagebox
from PIL import Image, ImageTk

#Sets the Tkinter splash screen / Gives screen a title / Gives screen an icon
#splash_root = Tk()
#splash_root.title("Bird-Dogey Splash Screen")
#splash_root.iconbitmap('flag.ico')

#Sets splash form size and centers it on any size monitor
#app_width = 611
#app_height = 489
#screen_width = splash_root.winfo_screenwidth()
#screen_height = splash_root.winfo_screenheight()
#x = (screen_width / 2) - (app_width / 2)
#y = (screen_height / 2) - (app_height / 2)
#splash_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#Sets background image on form
#image_path = PhotoImage(file = r"splash.png")
#bg_image = tkinter.Label(splash_root, image = image_path)
#splash_label = Label(splash_root, image = image_path)
#splash_label.place(x =0, y = 0, relwidth = 1, relheight = 1)

#Close splash form
#splash_root.destroy()

def clear_label(event):
    #Clears the display_score_label
    display_score_label.config(text="")

def search_scores():

    searchwin = tk.Tk()
    searchwin.title('Bird-Dogey Search Data Form')
    searchwin.iconbitmap('flag.ico')

    # Set height and width for application
    app_width = 914
    app_height = 484
    screen_width = searchwin.winfo_screenwidth()
    screen_height = searchwin.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    searchwin.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    searchwin.config(bg="#afed66")

    # Create a heading/banner across Entry_Form
    search_heading = Label(searchwin,text="Bird Dogey Search Information Form", bg="green", font="10", width="500", height="3")
    search_heading.pack()

def save_info():

    playerid = playerid_entry.get()
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    course = course_listbox.get(ANCHOR)
    date = date_entry.get()
    holes = holes_entry.get()
    score = score_entry.get()
    par = par_entry.get()

    file = open("data.txt", "a")
    file.write(playerid + "," + firstname + "," + lastname + ","  + course + "," + date + ","
               + holes + ","  + score + "," + par + "\n")
    file.close()

    #Display score for round
    score = int(score_entry.get())
    par = int(par_entry.get())
    score_round = score - par
    print(score_round)
    if score == par:
        print("You shot even par today!")
        display_score_label.config(text="You shot even par today!")
    elif score < par:
        print("You shot " + str(score_round) + " under par today!")
        display_score_label.config(text="You shot " + str(score_round) + " under par today!")
    elif score > par:
        print("You shot +" + str(score_round) + " over par today!")
        display_score_label.config(text="You shot +" + str(score_round) + " over par today!")

    #Clear text fields and listbox
    playerid_entry.delete(0, END)
    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    date_entry.delete(0, END)
    holes_entry.delete(0, END)
    score_entry.delete(0, END)
    par_entry.delete(0, END)
    #course_listbox.delete(ANCHOR)
    course_listbox.selection_clear(0, END)
    course_listbox.selection_set(0)
    course_listbox.activate(0)

root = tk.Tk()
root.title('Bird-Dogey Data Entry Form')
root.iconbitmap('flag.ico')

# Set height and width for application
app_width = 914
app_height = 484
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#Set background image for Entry_Form
entry_image_path = PhotoImage(file=r"entry.png")
entry_bg_image = tkinter.Label(root, image=entry_image_path)
entry_label = Label(root, image=entry_image_path)
entry_label.place(x=0, y=0, relwidth=1, relheight=1)

#Create a heading/banner across Entry_Form
heading = Label(text="Bird Dogey Golfer Information Form", bg="green", font="10", width="500", height="3")
heading.pack()

#Create labels for Entry_Form
playerid_label = Label(text="Player ID: ", bg="#afed66")
firstname_label = Label(text="FirstName: ", bg="#afed66")
lastname_label = Label(text="LastName: ", bg="#afed66")

#Create and Populate listbox from list
course_listbox = Listbox(root, font=("arial", 10), width=30, bg="lightgreen")
course_list = ["Cascades Golf Course", "Rolling Meadows", "The Point Resort", "Taylor's Par 3",
               "Bloomington Country Club", "Stone Crest", "Pine Woods", "Salt Creek Golf Course",
               "Foxcliff Golf Course", "Other"]
for course in course_list:
    course_listbox.insert(END, course)

course_label = Label(text="Course Played: ", bg="#afed66")
date_label = Label(text="Date Played :", bg="#afed66")
holes_label = Label(text="Holes Played :", bg="#afed66")
score_label = Label(text="Score :", bg="#afed66")
par_label = Label(text="Par for Course :", bg="#afed66")
display_score_label = Label(text="", bg="#afed66", font="16")

#Places labels specifically on Entry_Form
playerid_label.place(x=300, y=73)
firstname_label.place(x=300, y=110)
lastname_label.place(x=300, y=150)
date_label.place(x=300, y=190)
holes_label.place(x=300, y=230)
score_label.place(x=300, y=270)
par_label.place(x=300, y=310)
course_label.place(x=630, y=80)
display_score_label.place(x=50, y=80)

#Creates entry boxes for the Entry_Form
playerid_entry = Entry(root,width=6, bg="lightgreen")
firstname_entry = Entry(root, width=30, bg="lightgreen")
lastname_entry = Entry(root, width=30, bg="lightgreen")
date_entry = Entry(root, width=12, bg="lightgreen")
holes_entry = Entry(root, width=4, bg="lightgreen")
score_entry = Entry(root, width=4, bg="lightgreen")
par_entry = Entry(root, width=4, bg="lightgreen")

#Place textboxes specifically on Entry_Form
playerid_entry.place(x=390, y=76)
firstname_entry.place(x=390, y=113)
lastname_entry.place(x=390, y=150)
date_entry.place(x=390, y=190)
holes_entry.place(x=390, y=232)
score_entry.place(x=390, y=273)
par_entry.place(x=390, y=312)
course_listbox.place(x=630, y=110)

#Calls function to clear the display_score_label on playerid(click)
playerid_entry.bind("<Button-1>", clear_label)

button_submit = Button(root, text="Save Information", command=save_info)
button_submit.place(x=500, y=320)

button_exit = Button(root, text="Exit Application", command=root.destroy)
button_exit.place(x=800, y=320)

button_search = Button(root, text="Search Scores", command=search_scores)
button_search.place(x=650, y=320)

#Splash Screen Timer
#splash_root.after(3000, entry_window)

mainloop()