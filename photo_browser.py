
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
from PIL import Image, ImageTk

# Import StringIO,
from StringIO import StringIO

title = [] # List of the titles
date = [] # List of the Dates
author = [] # List of the Authors
img_junk = []
img = [] # List of URLs
image = ''
tkimg = ''
height = [] # List of image heights
width = [] # List of image widths
heightint = []
widthtint = []
heading = ''

# Setup counter for going through the lists
counter = 0


def update_img():
    global counter
    global tkimg
    global heightint
    global widthtint

    image = img[counter]
    fd = urlopen(image)
    image_file = StringIO(fd.read())
    im = Image.open(image_file)
    for each in heightint:
       if heightint[counter] > widthtint[counter]: # Portrate scaling
           im = im.resize((400,600), Image.ANTIALIAS)

       elif heightint[counter] < widthtint[counter]: # Landscape scaling
           im = im.resize((1000,600), Image.ANTIALIAS)

       elif (heightint[counter] - widthtint[counter]) < 100: # Square scaling
           im = im.resize ((600,600), Image.ANTIALIAS)

    tkimg = ImageTk.PhotoImage(im)
    my_canvas.create_image(500,300, image=tkimg)

def prev_button():
    global counter

    counter = counter - 1

    update_img()

    titletext.config(text=title[counter])
    datetext.config(text=date[counter])
    authortext.config(text=author[counter])

def next_button():
    global counter

    counter = counter + 1

    update_img()

    titletext.config(text=title[counter])
    datetext.config(text=date[counter])
    authortext.config(text=author[counter])

def load_url():
    global heightint
    global widthtint
    global heading

    # RSS Feed URL, get images and data from
    deviant = urlopen('http://backend.deviantart.com/rss.xml?q=gallery%3Ajohnsonting+sort%3Atime&type=deviation')
    # http://backend.deviantart.com/rss.xml?q=favby%3Ajohnsonting%2F40216396&type=deviation
    # http://backend.deviantart.com/rss.xml?q=gallery%3Ajohnsonting+sort%3Atime&type=deviation
    site_data = deviant.read()
    deviant.close()

    for each in findall('<title>(.*)</title>', site_data): # Getting the title for each image from site_data
        title.append(each) # Putting the Title information into the title list

    for each in findall('<pubDate>(.*)</pubDate>', site_data): # Getting the date for each image from site_data
        date.append(each) # Putting the date information into the date list

    for each in findall('<media:content url=(.*)medium', site_data): # Getting the image urls from site_data
        img_junk.append(each) # Putting the url information into the rul list

    for each in findall('"urn:ebu">([A-Za-z-0-9]+)</', site_data):
        author.append(each)

    test = '\n'.join(img_junk)

    for each in findall( '"(.*)" height', test):
        img.append(each)

    heightremove = '\n'.join(img_junk)

    for each in findall('height="(.*)" width', heightremove):
        height.append(each)


    # heightremove = '\n'.join(height)

    heightint = [int(heightint) for heightint in height]


    widthremove = '\n'.join(img_junk)

    for each in findall('width="(.*)"', widthremove):
        width.append(each)

    # widthtremove = '\n'.join(width)

    widthtint = [int(widthtint) for widthtint in width]

    heading = title[0] # Getting the first title from the deviantart page before it is removed from the list

    del title[0] # Removing the first title as it is a page title not an image title

# Downloading the data to the spesific lists
load_url()

# Create a window
photo_window = Tk()

photo_window.title(heading)


bottom_frame = Frame(photo_window)
top_frame = Frame(photo_window)

title_frame = Frame(photo_window)
date_frame = Frame(photo_window)
author_frame = Frame(photo_window)


# Create the canvas where the image will be stored & put it into the grid
my_canvas = Canvas(photo_window, width=1000, height=600, bg='white')
update_img()
my_canvas.create_image(500, 300, image=tkimg)

# Create the control buttons & put them into the grid
Button(bottom_frame, text='<-- Previous', command=prev_button).pack( side = LEFT )
Button(bottom_frame, text='Next -->', command=next_button).pack ( side = RIGHT)
# Button(bottom_frame, text='Configuration').pack()

# Various Titles being created
titletext = Label(top_frame, text=title[counter])
datetext = Label(top_frame, text=date[counter])
authortext = Label(top_frame, text=author[counter])

# Putting everything into the grid (unless done above)
# my_canvas.grid(row=2, column=1, columnspan=3)
my_canvas.grid(row=2,column=1, columnspan=3)

authortext.pack(side=LEFT)
datetext.pack(side=RIGHT) # Putting datetext into grid
titletext.pack() # Putting titletext into grid


# title_frame.grid(row=1, column=2)
# date_frame.grid(row=1, column=3)
# author_frame.grid(row=1, column=1)

top_frame.grid(row=1, column=1, columnspan=3)
bottom_frame.grid(row=3, column=1, columnspan=3)

# Start the event loop to react to user inputs
photo_window.mainloop()
