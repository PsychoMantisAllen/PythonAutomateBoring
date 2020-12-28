#! /usr/bin/env python3
import webbrowser, sys, pyperclip

# creating a programme to automatically open google map for the address
sys.argv    # ['mapit.py', '870', 'Valencia', 'St.']
# in the command line we will type mapit.py 870 Valencia St.

# check if command line arguments were passed
if len(sys.argv) > 1:   # sys.argv is a list of string, we can just check the length
    address = ' '.join(sys.argv[1:])   # transform the list of string into one combined string
else:
    address = pyperclip.paste() # if the address is pasted

# what is the format in google map address?
# using the following example
# https://www.google.com.au/maps/place/255+Anzac+Parade,+Kingsford+NSW+2032/@-33.9200719,151.2240614,17z/data=!3m1!4b1!4m5!3m4!1s0x6b12b18e95be84b5:0x5fcacc1c5d9380b7!8m2!3d-33.9200719!4d151.2262501
webbrowser.open('https://www.google.com.au/maps/place/' + address)