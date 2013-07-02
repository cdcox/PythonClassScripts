# -*- coding: utf-8 -*-
"""
Tutorial:
    this will guide you through the basic commans of python
    including variable types and how to call and manipulate them
    At the end it will discuss modules and errors.
    
    Throughout this tutorial, results should print to the console
    if you get a red result, that means you messed up somewhere.
    Reread the directions for that section and tweak your code.
    If you keep getting an error call me over!
    While you could jsut copy paste a lot of this, you will learn
    more by typing it out and calling the varialbes your own names
    (and even calling your own values)
"""
"""
Variables
"""
"""
Variables are essentially containers you can store information in
these containers can be used like the information stored in them
for instance: A=1 can be used anywhere 1 could be used.
Below declare A as two, on the next line print it. (To print type print A)
Then hit run. (f5 or arrow under run up top)"""
#Your code below here


## Run it now

""" A above is declared as a int. This means operations on A will
return integars. (whole numbers). Below, declare a varialbe B as 
A/10 On the line below it, print B, you should get 0. (If you don't
don't worry that just means you have a quirk in how you ran it, it 
shouldn't effect anything moving forward)
"""
#Your code below here


## Run it now
""" To fix this, simply declare a with . after it. This tells python
you want a 'float' this is a variable with large accuracy.
Go back to line 18 and declare A as 2. Now try running your code again.
It should produce the correct answer."""
"""in python the basic math terms are + - / * and ** (for exponential)
Below print A+A
print A-A
print A/A
print A*A
print A**34
"""
#Your code below here




## Run it now

"""
Ints and floats are not the only variable types, Another common type
is strings. Strings are lists of letters. They can be be as short as
one letter or as long as the entire corpus of all human literature.
To declare a string just type Variable='string of my choice'
Alternatively Variable="string of my choice"
Below, declare the string C as "Declaring a variable can be easy"
below that:
print C
"""
#Your code below here


## Run it now
r""" Strings have one big hangup you might run into when coding.
certain characters \x for instance, have a specific meanign to the 
computer because of this, it will eat/misread these characters, 
below declare BadVar as "this \x will cause an error"
print BadVar, you should get a red error"""
#Your code below here


## Run it now
r""" Fixing this is easy. Go back up to line 69 (where you declared 
BadVar)
and put an r before the "" so it should now read BadVar=r"this \x will cause an error"
Run it again.
You will notice it now prints (mostly) fine. 
(python does not care about 2 \ or 1)
what you are doing is telling python to read your line literally
and not translate anything into computer meanings.
It is a good habit to put r in everywhere you call a string."""
""" More on strings!
Strings have some special options associated with them,
to access these take the variable you have written a string into
and type . after it. (Do this in your console the area with three >>>)
 You will see a  number of options, most of these are not extremely
 useful to you right now. but to show how they work let's 
 use the 'split'. Set SplitVar= "Let's break this into indivdual strings"
 Next type K=SplitVar.split(" ") What this does is break SplitVar into individual
 words (as you are splitting it around spaces). print K below that.
"""
#Your code below here



## Run it now
""" Lists!
Lists are a slightly confusing concept. In essence they are a variable
that contains multiple things that could each be their own variable.
To declare lists you put [] around things you want in a list, seperate
items with commas
To test this:
    Below make a string Var1 as [1,2,3,4]
    Set Var2 as ['lists','can','be','words']
    Set Var3 as ['lists',2,'can',345,'have']
below that 
print Var1
print Var2
print Var3
"""
#Your code below here






## Run it now
""" Lists can be combined with the + sign.
Below make NewVar=Var1+Var2
then print NewVar
(Side note, strings can be combined the same way)
"""
#Your code below here


## Run it now
""" Lists have some of their own options (like strings), most of these
don't matter very much for now. The one that matters a lot is append.
Make a list Listez=[1,2,3,4,5]
now run Listez.append(7) (You will notice you don't 
declare a variable here! one of the few times you won't)
print Listez
"""
#Your code below here



## Run it now
"""The range command:
    Often it's useful to quickly make a list of numbers, we will
    be doing this a lot below. So heres how:
        
    range(start,finish,step)
    Below:
    print range(0,23) #all numbers from zero to 23 (not including 23)
    print range(1,10,2) # all numbers from one to ten stepping by 2
    print range(40) # all numbers from zero to 40
"""
#Your code below here



## Run it now
"""List slicing:
    List slicing allows us to access elements of lists easily
    the basic list slice is ListVar[first:last:step]
    if first is left blank it defaults to 0, if last is left blank
    it defaults to last element of the list. if step is left blank
    it defaults to 1.
    Declare ListVar=range(25)
    then print ListVar[:] All of ListVar
    print ListVar[:10:2] From 0 to 10 by steps of 2
    print ListVar[1:15:3] From 1 to 15 by steps of 3
    print ListVar[20:0:-1] From 20 to 0 by steps of -1 !
    print ListVar[::-1] From list end to list beginning by -1
    (That last one is kind of tricky as it actually breaks the above
    rules, however it's VERY useful)
    """
#Your code below here






## Run it now
""" The numpy module.
Numpy lets you quickly do complex math on lists.
It DOES NOT use lists (though most of it's commands can operate
on lists if you need to do something fast, but know that behind
the scenes it is converting these lists to something else)
It operates on arrays. An array is multidimensional list (like a
Matrix)
To bring numpy into our module we will call import numpy as np
to declare an array we declare arrayVar=np.array([[]]) Note the double brackets
Test this out!
one line 203 type import numpy as np
Declare ArrayVar=np.array([[1,2,3],[4,5,6]])
print ArrayVar
print ArrayVar**3
print ArrayVar+2
print ArrayVar-ArrayVar
"""
#Your code below here





## Run it now
""" Numpy also contains powerful tools like mean and standard deviation.
These tools have suboptions. To view these suboptions go to your console
type np.mean( in your object explorer, mean should show up. Note
you can declare axis, dtype and out. Most of the time you don't
need to declare these (as they are autodeclare to none!)
You can use these options to perform more powerful functions.
Most functions  only require one variable.
To perform a function the general syntax is:
    module.function(Variable)

for instance:
    np.mean(ArrayVar,0) Takes the mean by columns.
    np.mean(ArrayVar,1) Takes the mean by rows.

try this out:
print np.mean(ArrayVar)
print np.mean(ArrayVar,0)
print np.mean(ArrayVar,1)
"""
#Your code below here



## Run it now
""" List slicing in 2+D.
List slicing can be performed in multiple dimensions!
To do this just do
ArrayVar[firstY:LastY:StepY,FirstX:LastX:StepX]
try it out
print ArrayVar[:,::-1] Flips the x axis
print ArrayVar[:,0:2] First 2 columns
print ArrayVar[0,:] First row
"""
#Your code below here



## Run it now
""" Errors:
Python is fairly helpful, and very explicit when it comes to errors.
Generally an error will tell you what line it is on, and give a 'guess' as to
what went wrong.

To test this make a list G=[1,2,3]
print G**2
 You should get a type error
 """
 #Your code below here



## Run it now

""" To fix this, go back to line 258 and declare G as G=np.array([[1,2,3]])
now run it, the error should be gone
"""

""" That is all for this tutorial. Hopefully this was more useful
than the almost comically buggy first coding project was."""