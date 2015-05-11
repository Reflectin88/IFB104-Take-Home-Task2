# Import the Tkinter functions
from Tkinter import *

# Import the function for downloading web pages
from urllib import urlopen

# Import the regular expression function
from re import findall

# Import PIL, Python Image Libary
from PIL import Image,ImageTk

import StringIO


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
img_junk = []
img = [] # Creating url list

for each in findall('<title>(.*)</title>', site_data): # Getting the title for each image from site_data
    title.append(each) # Putting the Title information into the title list

for each in findall('<pubDate>(.*)</pubDate>', site_data): # Getting the date for each image from site_data
    date.append(each) # Putting the date information into the date list

for each in findall('<media:content url=(.*)height', site_data): # Getting the image urls from site_data
    img_junk.append(each) # Putting the url information into the rul list

test = '\n'.join(img_junk)

for each in findall( '"(.*)"', test):
    img.append(each)


for each in img:
    print "%s" % each