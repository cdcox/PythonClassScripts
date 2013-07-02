# -*- coding: utf-8 -*-
"""
Pulling it all together in a super complex assignment.

Motivation: Combining the concept of images as arrays and for loops
We are going to open every image in a directory, perform an operation,
then resave them to a new directory.

What you should do:
    
    Make two directories, an input and output, put the images from the image
    directory that I have provided into the input directory
"""
import os
import scipy.misc
Indirectory=                           # fill in input directory
OutDirectory=                       #fill it output directory
InFileList=os.listdir(Indirectory)
###########your code here##########






####################################

""" Guide:
0. set input and output directories.
1. on line 20 start a for loop that loops through all the items in the
InFileList.
2. On line 21 combine the looped items and the directory into a variable
FullPath=Directory+Items
3. On 22 open the file into a variable Image=scipy.misc.imread(FullPath)
4. On line 23, switch the image's channels around NewImage=Image[:,:,::-1]
5. On 24 make your output file name FullOut=OutDirectory+Items
6. On 25 save your file: scipy.imsave(Fullout,NewImage)
7. Run it! Play with the lines until you are comfortable that you 'get them'
"""