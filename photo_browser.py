
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9378880
#    Student name: Jai Spicer
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files may be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  PHOTO BROWSER
#
#  There are many Web sites that provide regularly-update photographs,
#  especially for news stories.  Here you will create an interactive
#  application that makes it easy to browse the photos on a particular
#  Web page by showing them to the user one at a time, via an intuitive
#  Graphical User Interface.  See the instruction sheet accompanying
#  this file for full details.
#
#--------------------------------------------------------------------#

#
# Import the Tkinter functions
from Tkinter import *

# Import the function for downloading web pages
from urllib import urlopen

# Import the regular expression function
from re import findall

# Import PIL, Python Image Libary
from PIL import Image,ImageTk

counter = 0

def prev_button():
    global counter

    counter = counter - 1

    titletext.config(text=title[counter])
    datetext.config(text=date[counter])

def next_button():
    global counter

    counter = counter + 1

    titletext.config(text=title[counter])
    datetext.config(text=date[counter])



# RSS Feed URL, get images and data from
deviant = urlopen('http://backend.deviantart.com/rss.xml?q=gallery%3Ajohnsonting+sort%3Atime&type=deviation')
site_data = deviant.read()
deviant.close()

title = [] # Creating title list
date = [] # Creating data list
img = [] # Creating url list

for each in findall('<title>(.*)</title>', site_data): # Getting the title for each image from site_data
    title.append(each) # Putting the Title information into the title list

for each in findall('<pubDate>(.*)</pubDate>', site_data): # Getting the date for each image from site_data
    date.append(each) # Putting the date information into the date list

for each in findall('<media:content url=(.*)height', site_data): # Getting the image urls from site_data
    img.append(each) # Putting the url information into the rul list


heading = title[0] # Getting the first title from the deviantart page before it is removed from the list

del title[0] # Removing the first title as it is a page title not an image title

photo_window = Tk() # Create a window

photo_window.title(heading) # Give the window a title

# Create the canvas where the image will be stored & put it into the grid
my_canvas = Canvas(photo_window, width=800, height=500, bg='white').grid(row=2, column=1, columnspan=3)

# Create the control buttons & put them into the grid
Button(photo_window, text='<-- Previous', command=prev_button).grid(row=3, column=1)
Button(photo_window, text='Next -->', command=next_button).grid(row=3, column=3)

titletext = Label(photo_window, text=title[counter]) # Creating Image Title
datetext = Label(photo_window, text=date[counter]) # Creating Date Title

titletext.grid(row=1, column=2) # Putting titletext into grid
datetext.grid(row=1, column=3) # Putting datetext into grid

# Start the event loop to react to user inputs
photo_window.mainloop()