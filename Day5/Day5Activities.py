# -*- coding: utf-8 -*-
"""
Making pretty python:

0. To get use to the def function return thing,
write a program that asks a user for a number.
Then make function called add_fifty
have it take the number as an input and return
the number as an output. 
print the number.
remember to have a if __name__=='__main__':
    at the bottom.

Bonus: Try running the function by calling it externally (go to
the command line and type python (your files path and name))
Windows user can set a program to run with python as the default program
try that out!

1. Make a program that finds the 1001 prime number!
to do this we need the following elements:
I've written out the code to do it below, break out the chunck of code
from the for loop to the append line into a function,
remember you have to give it previouslist and your nubmer
and return prevoius list and the number
set the rest of the code under an __init__=='__main___'
(remember only one of these per program!)

i=4
previous_list=[2,3]
while len(previous_list)<1001:
    i=i+1
    checking_number=0    
    for items in previous_list:
        if i%items==0:
            checking_number=1
    if checking_number==0:
        previous_list.append(i)
        
2. Below this code you will find two lists of numbers
Control and experimental
make a function strip_low_values that goes
through both lists and turns numbers below zero into 0
(use an indexing for loop for this)
after this make a 
if __init__=='__main__' that runs through this which each list
and returns the new list. then perform a ttest
under scipy.stats.ttest_ind on the two output lists.

3. Thanks for sticking out the intro weeks! go to your console
and type in. 
import this

be sure to tell me what you'd like to see:

Things I came up with: 
 cell counting
 text document parsing (for numbers)
 neural network stuff
 character recognition for pictures
 graphing
 image processing
 
 We have many weeks ahead (after this quarter so all ideas will
 be taught, but I'll teach the ones with the most interest first
 so if any of the above sound good tell me!)


"""















"""
control=[ 0.29892391,  0.29390532,  0.44596463,  0.4905357 , -0.49486145,
       -0.29503334, -0.03309252,  0.43755501,  0.13342393, -0.27069969]
       
experimental= [ 1.37913615,  0.23513822, -0.0032897 ,  1.35233926,  0.85305913,
        1.30169848,  0.29811183, -0.21212195, -0.09939539,  1.01793759]
"""
