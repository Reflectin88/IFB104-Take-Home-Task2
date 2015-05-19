
# Import the Tkinter functions
from Tkinter import *

# Import the function for downloading web pages
from urllib import urlopen

# Import the regular expression function
from re import findall

# Import PIL, Python Image Libary
from PIL import Image, ImageTk

from StringIO import StringIO

author = []

deviant = urlopen('http://backend.deviantart.com/rss.xml?q=favby%3Ajohnsonting%2F40216396&type=deviation')
site_data = deviant.read()
deviant.close()

for each in findall('"urn:ebu">([A-Za-z-0-9]+)</', site_data):
    author.append(each)

for each in author:
    print '%s' % each