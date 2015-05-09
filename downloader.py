#-----------------------------------------------------------
#
# Web Page Downloader
#
# For a particular URL, this simple program downloads a web
# page and stores it in a text file in the current folder.
# You can then open the file in a text editor to inspect
# its contents or paste parts of it into our "regex tester"
# to explore ways of extracting particular elements from the
# document.  This simple script has no user interface or error
# handling, but feel free to add them if you want!
#
# Q: Why not just look at the web page's source in your
# favourite web browser (Firefox, Google Chrome, etc)?
# A: Because when a Python script uses the hyper-text transfer
# protocol to download a web document, it may not receive
# the same file you see in your browser!  Some web servers
# produce different HTML or XML code for different browsers.
# Therefore, to guarantee that the code you inspect is the
# same code that your own Python program sees, it's safer
# to download the web page using this script.
#

from urllib import urlopen

url = 'http://backend.deviantart.com/rss.xml?q=gallery%3Ajohnsonting+sort%3Atime&type=deviation' # Put your web page address here

filename = 'download.txt' # Put your preferred file name here

text_file = open(filename, 'w') # NB: This step will overwrite an existing text file!

web_page_contents = urlopen(url).read()

text_file.write(web_page_contents)

text_file.close()
