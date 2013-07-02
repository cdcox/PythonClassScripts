# -*- coding: utf-8 -*-
"""
Day 2 example 2: Looping through files

Motivation: suppose you wanted to go through a directory of files and do
something to each one.

To do this we need to use the os module. This will go throught the
basics of that with a for loop
"""
import os

Directory=    # Define a working directory here
FileList=os.listdir(Directory)
print FileList

for items in FileList:
    print 'A file is '+Directory+items
    

""" Things to do!

0. Run the script above

1. Change the print command, see what the print order is doing. run it

2. Go to line 12 and make an empty list Filez=[] perhaps.
Go to line 19 and while still indented try to make a new list with
Directoy+items for all items. remember, to add an item to a list:
Filez.append(Directory+items)
run it
"""