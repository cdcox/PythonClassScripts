# -*- coding: utf-8 -*-
"""
This is going to be a little review about lists and a sort of primer about
opening images.

Images on computers are basically 3-D Matrixes 1024x1024x3 (The three channels)
This is useful as we can then pull images in and do math to them,
then resave them.

In this first bit of code I'm going to load in one image and flip it top to bottom
then resave it. I will then direct you to do some similar stuff.

There should be a directory with some animal pictures including
Dog1.jpg
All images from wikimedia foundation
"""
import scipy.misc # This is just a tool that lets me open images

Directory=          #Your directory here
DogInFilename=Directory+'Dog1.jpg'
DogOutFilename=Directory+'Dogflip.jpg'

Dog=scipy.misc.imread(DogInFilename)

DogFlip=Dog[::-1,:,:]

scipy.misc.imsave(DogOutFilename,DogFlip)

"""
0. Insert the dirictory run the code.
1. The important line here is line 25. Try changing it so it reverses the channel order.
2. Change it so it flips the image left to right. run it
3. Brighten the image, add 25 to each point. run it
4. Dim the image, divide it by 2 run it
5. Take the mean of the image, have it print out into your console run it
"""