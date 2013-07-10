# -*- coding: utf-8 -*-
"""
For tutorial
The goal of this tutorial is to go through the 
basic logic of how for loops work
and when to use them.

It will then discuss using for loops 
on arrays and in multiple dimensions.

This assumes you have done the previous intro
tutorial, if not, consider running through it.
"""
"""
At it's simpelist, a for loop says:
"Do all this indented stuff a number
of times equal to the length of this list
and move the list forward one item each time
you do that"
to test this, write out the following code:
i=1
list=['a','b','c','d','e']
for items in list:
    print i
    print items
    i=i+1
"""
#your code here






#Run it now
"""
Go back up to line 30 and erase one of the
items from your list run it, 
did it do as you expected?
Now add an item or two to your list, run it
did it do as you anticipated?

Now let's play with syntax. Go back to line 31
change items into stuffz, be sure to change
items into stuffz on line 33.

That varialbe, whatever you declare it as, will move
through your list one item at a time.
"""
"""
For loops within for loops:
    
For loops can be embedded inside each other.
Each time the outer loop runs
the internal loop with fully run.
to test this make two lists
list1=[1,2,3,4,5]
list2=['a','b','c','d']
make two for loops embedded in each other
wit hthe synatx
for items in list1:
    for stuff in list2:
        
print the results  from bothe lists inside the second loop. 
now print the results from the first list above the second loop
loop two should run
20 times.
"""
#your code here








#Run it now
"""
The len command
len returns the length of a list.
make a list with four elements
then  print len(yourlist)

"""
# your code here


#run it now
"""
len combined with range.
Change the above to print range(len(yourlist))
Run it
"""
"""
Now you can make an indexed forloop.
the basic syntax is:
for indexes in range(len(yourlist)):

make a list of five items and try this

for indexes in range(len(yourlist)):
    print yourlist[indexes]

This produces the same results as
for items in yourlist
    print items
    
"""
# your code here



#run it now
"""
note these loops are just running through 
the list produced by the range command
modify your above list to print
indexes
run it
"""
"""
This is useful if you want to move through two lists
that are lined up.
Similar to the example in class:
Make two lists
age=[1,2,3,4,5]
kidnames=['bob','jill','hetelvica','john','phil]
now type out the following
recall we combine strings with +
for index in range(len(age)):
    numstr= str(age[index]) # this is because you can't combine numbers and strings
    print kidnames[index]+" is "+numstr+" years old."
"""
# your code here





#run it now
"""
Complicated time!
import numpy as np below
"""
#here

#no need to run this
"""
remember to declare numpy arrays we use the following syntax:
yourArray=np.array([[1,2,3],[19,39,29],[109,209,309]])
Essentially it is a 'list of lists' that contain only numbers
declare and print yourArray from above
"""
# your code here


#run it now
"""
How to pull specific items out of an array
Arrays are just like lists except
element one controls what Row you are in 
Element two controls what column you are in.
so 
yourArray[1,2] would equal 29
using yourArray print out 109 
then 39
then 2
"""
# your code here



#run it now
"""
Combining this with loops:
the np.shape commmand is like len in two directions
run it on yourarray from above:
print np.shape(yourArray)
"""
# your code here

#run it now
"""
Make a variable 
HugeArray=np.array([[5,6,76,56,45],[23,45,23,15,1000],[1293,45452,2323,32,1],[1,2,3,4,5]])
print HugeArray by columns using a for loop. and the above
(consider declaring a variable called size=np.shape(HugeArray))
(then loop through the range(size[1]) or the second element of size
(Answer below)
"""
# your code here





#run it now
"""
size=np.shape(HugeArray)
for columnidx in range(size[1]):
    print HugeArray[:,columnidx] #print all numbers in each column
"""
"""
Change the above so it prints by rows
"""
# your code here



#run it now
"""
Now lets use a 2 layer for loop to go to each element of 
HugeArray and divide them by 20 then square the result, then
add 3 then write it back into HugeArray
Don't worry if you don't totally ge this
size=np.shape(HugeArray)
for rowidx in range(size[0]):
    for colidx in range(size[1]):
        Temp=HugeArray[rowidx,colidx]
        print Temp
        Temp=(Temp/20)**2+3
        print Temp
        HugeArray[rowidx,colidx]=Temp
As you can see, you can actually write back into arrays with loops!.
"""
# your code here







#run it now
"""
modify the above so it makes a new variable:
ListofResults
Declare ListofResults on line 226 (above the declaration of size)
ListofResults=[]
now for the internal loop append the results to ListofResults.
Outside the loops and after them (so around line 233 and tabbed
back to the edge) print ListofResults
"""
"""
The above is fairly crucial, play with it until you have
a feel for it"""