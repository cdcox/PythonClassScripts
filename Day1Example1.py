# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:26:49 2013

@author: Conor

In this file you will open an csv that I prodivded: SampleData1.csv.
You will then peform a histogram analsis of each row and column. Save this as
DataOut.
The code will then write DataOut on it's own. You need to do three things.
1. Fill in a Directory under Directory= be sure to use "" and not '' and be sure
to add two / at the end of the name.

2. import numpy as np.

3. Perform mean on all columns and write this as DataOut.

4. Do the same to all rows.

5. Try a historgram.

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

Directory =               #fill in your directory here

# Intialization code:
InFile=Directory+"//"+"SampleData1.csv" # I added the slashes in case you failed at that
f=open(InFile) #open the file
DataIn=csv.reader(f)
DataIn=list(DataIn)
f.close() #Closing my file
DataIn=np.array(DataIn[1:-1]).astype('float')
##### Your Code Goes here#####
DataOut=np.histogram(DataIn)





######### Set Variable DataOut#######

OutFile=Directory+"//"+"OutPutData1.csv"
g=open(OutFile,"wb")
wr=csv.writer(g)
FlippedOut=itertools.izip(*DataOut) #flipping rows and columns for easy writing

wr.writerows(FlippedOut)
g.close()