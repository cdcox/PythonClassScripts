# -*- coding: utf-8 -*-
"""
Working Example 1.

This example shows the basic layout of a for loop:
    At the end it should print a word-number pairing printed to your
    console (should be on your bottom right)
"""
List1=['apples','oranges','grapefruits']
List2=[2,3,4]
# Note I made List1 and List2 the same length, this will not run
#if they are different lengths
'''This next line will generate a series of numbers
the lenght of List1'''
for Index in range(len(List1)):
    List2String=str(List2[Index]) #This converts the number to a string
    print 'There are '+List2String+' '+List1[Index]
    
'''
0. run the code
1. To get a feel for how this works, Go to line
9 and 10 and add some more items to the list
see how this changes the nature of the output. Run it.

2. Play with the string output on line 17. See what the plusses do. Run it

3. replace line 17 with print str(Index), does it do what you expected?. Run it


4. I mentioned there are two ways to run lists.
One is:
 
for Index in range(len(stuff))
    print stuff[Index]

The other (much less used) is

for items in stuff:
    print items
    
For this problem try to make two embedded for loops
it might look something like this: REMEMBER ONCE YOU ASSIGN A VARIABLE
IT OVERWRITES WHATEVER WAS THERE BEFORE!
    
for items in List1:
    for items2 in List2:
        print 'There are '+str(items2)+' '+items
(This is obviously not extremely useful as you lose the indexing positions
but it's fun to do)
then run it
'''