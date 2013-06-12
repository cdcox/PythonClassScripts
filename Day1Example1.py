# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:26:49 2013

@author: Conor

In this file you will open an csv that I prodivded: SampleData1.csv.
You will then peform a histogram analsis of each row and column. Save this as
DataOut.
The code will then write DataOut on it's own. You need to do three things.

SIMPLE ASSIGNMENTS:
0. try import this on your command line

1. Fill in a Directory under Directory= be sure to use "" and not '' and be sure
to add two / at the end of the name.

2. import numpy as np.

3. Perform mean on all columns and write this as DataOut.

4. Do the same to all rows.

5. Try a historgram.

COMPLEX ASSIGNMENTS:

1. You will notice there is a header line on the original file. Suppose you wanted
to include that in your output file. Try making a blank list and running 
listname.append(Header) and ListName.append(DataOut) after you define both,
the header can be found as the first row of the DataIn in sheet.

2. Try turning off my itertools item and get the code to print results in the 
opposite way it does.


EXTREMELY COMPLEX ASSIGNMENTS:

1. import scipy.stats and run a ttest comparing two columns, obviously they are
different (we could have told this by the means)

2. You will notice the 'channel' variable is 1 and 0. Visually inspect the data
and write these two groups as seperate variables (you could do this in excel)

3. Perform a TTest comparing volume of the two groups, compare intensities as well.

4. Ouput these results in a pretty way in the oupupt file, remember you can define strings
with ' '

5. Do this analysis without visually inspecting the data first. Remember 
anything *0 = 0 and np.abs(0-1)=1. also look at getting indexes with np.min
google "indexes from numpy min". If you need help with this ask, I didn't flesh
it out because I suspected few would get here. but try multiplying across columns
and stuff.

NOTES:
 

A few  things to remember: You can snag all this code and run it in your executor
to see what it does in your variable explorer.

You can use pdb.set_trace() to freeze the code at any  point.

The error codes say which line is having a problem.

When you are done, try altering my code to see how it breaks.

Obviously, with list slicing we can run through each column of DataIn to build
a mutlilayer DataOut, that being said, that is not very efficient, next lesson
we will learn about the for loop to fix this.

You will notice your data is writing as columns. This is because I am using
itertools.izip(*DataOut)

"""
import csv #Module CSV makes reading CSVs easy
import itertools #don't worry too much about this.
                 #import numpy here.
Directory =               #fill in your directory here

# Intialization code:
InFile=Directory+"//"+"SampleData1.csv" # I added the slashes in case you failed at that
f=open(InFile) #open the file
DataIn=csv.reader(f)
DataIn=list(DataIn)
f.close() #Closing my file
DataIn=np.array(DataIn[1:-1]).astype('float')
##### Your Code Goes here#####






######### Set Variable DataOut#######

OutFile=Directory+"//"+"OutPutData1.csv"
g=open(OutFile,"wb")
wr=csv.writer(g)
FlippedOut=itertools.izip(*DataOut) #flipping rows and columns for easy writing

wr.writerows(FlippedOut)
g.close()