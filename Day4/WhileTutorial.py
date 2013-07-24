# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 23:22:59 2013

@author: Ionox
"""
"""
If and while
"""
"""
If and while allow you to test if conditions are true
if they are, the  functino will run, if theya re not
the fucntion embedded with not run
"""
"""
Before diving into if and while it's important to understand
Boolean logic.
Boolean logic is basically a tool to tell if a statement is true
or false.
Test the following statements
1==2
2==2
2>3
3>2
2<3
3<2
"""
#Your code here






#run it
"""
Boolean logic can also be applied to strings
== directly compares strings
in checks if one string is in another
Test the following statements
"bob"=="bob"
"bob"=="not bob"
"bob" in "not bob"
"bobz" in "not bob"
"""
#Your code here






#run it
"""
If basically says, if the boolean statement is true
run everything below this if statement
if it is false, do not run every thing tabbed below it
Test the following
if True:
    print "this was true"

if False:
    print "this was not"
    
"""
#Your code here







# run it
""" 
if statements can be embedded in for statements to only
perform operations on datapoints that meet certain parameters
for instance take the list:
[1,2,3,4,5,5,6]
if an item is list is greater than 4 multiply it by 10 and print it
if it's less than 4 do not.
consider code like
for items in list:
    if items>4:
        print items*10
"""
#Your code here







# run it
"""
It can also be used to use an index from one list to print itesm
from another.
Suppose we have two lists
['Atrees','Btrees','ABushes','BBushes']
[50,43,24,35]
We want to know the total number of tress, we don't care about bushes
combining a for if loop
we can do
counter=0
for idx in range(len(plants)):
    if 'trees' in stuff[idx]:
        counter=counter+counts[idx]
print counter
Try it out, does it work as you expect, can you make it count
bushes?
"""
#Your code here







# run it
"""
If you want to test the truth of two statements, you can use
elif which means else if. This basically says, if the first statement
is false and I am true, run me.
Try the following
if True:
    print 'this'
elif True:
    print 'that'

if False:
    print 'YAY'
elif True:
    print 'boo'

if False:
    print 'More strings'
elif False:
    print 'this isn't going to print enyway'
    
Guess which statements are going to print!
"""
#Your code here









# run it
"""
We can also use else. Else says, if the if and elifs above me
are all false, print me instead.
Taking the above add on the following
if True:
    print 'this'
elif True:
    print 'that'
else:
    print 'nope'

if False:
    print 'YAY'
elif True:
    print 'boo'
else:
    print 'yep'
    
if False:
    print 'More strings'
elif False:
    print 'this isn't going to print enyway'
else:
    print 'this isn't too hard!'
"""
#Your code here













# run it
"""
While loops:
A while loop basically runs until it is true
so in the following while loop
i=10
while i>=0:
    istr=str(i)
    print "t-minus "+istr
    i=i-1
print "lift off"
"""
#Your code here










# run it
"""
While loops can be risky, if the while loop will never end
you will just end up freezing your program.
try the following (and when it freezes jsut quit spyder)
i=1
while i>0:
    print i
"""
#Your code here




# run it
"""
While loops are fairly inferior to for loops for a number of reasons
but the most common use for them is when you only need a few
items from a massive list
Say you only wanted the first 50 numbers from range(63000)
you could do somethign like this
massiverange=range(63000)
newlist=[]
idx=0
while len(newlist)<100:
    newlist.append(massiverange[idx])
This could be used to test embedded if statements etc.
Another use for while loops is double looping them
but this use is kind of beyond the scope of what I am trying to 
get across here
"""
#Your code here




# run it
"""
If we want to reverse the direction of a boolean statment
we can use not(statement)
try printing not(True)
go back tothe top and add not around everything in the first examples
"""
#Your code here

# run it
"""
That's all for if and while
"""