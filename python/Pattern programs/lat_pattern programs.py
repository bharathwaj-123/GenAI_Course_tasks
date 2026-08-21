Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============ RESTART: C:/Users/Bharathwaj/Desktop/Gen AI/SDLC/lat.py ===========
# Left angle triangle - patterns
#1.num row printing
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(k,end=' ')
    print()

    
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 
#2.num col printing
for i in range(5,0,-1):
    for j in range(1,i):
        print(' ',end=' ')
    for k in range(i,6):
        print(k,end=' ')
    print()

    
        5 
      4 5 
    3 4 5 
  2 3 4 5 
1 2 3 4 5 
#3.star printing

for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(1,i+1):
        print('*',end=' ')
    print()

    
        * 
      * * 
    * * * 
  * * * * 
* * * * * 

#4.upper row printing
>>> 
>>> for i in range(1,6):
...     for j in range(5,i,-1):
...         print(' ',end=' ')
...     for k in range(1,i+1):
...         print(chr(k+64),end=' ')
...     print()
... 
...     
        A 
      A B 
    A B C 
  A B C D 
A B C D E 
>>> 
>>> #5.upper col printing
>>> 
>>> for i in range(1,6):
...     for j in range(5,i,-1):
...         print(' ',end=' ')
...     for k in range(1,i+1):
...         print(chr(i+64),end=' ')
...     print()
... 
...     
        A 
      B B 
    C C C 
  D D D D 
E E E E E 
>>> 
>>> #6.lower row printing
>>> 
>>> for i in range(1,6):
...     for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(chr(k+96),end=' ')
    print()

    
        a 
      a b 
    a b c 
  a b c d 
a b c d e 

#7.lower col printing

for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(chr(i+96),end=' ')
    print()

    
        a 
      b b 
    c c c 
  d d d d 
e e e e e 

#name row printing

name='bharath'
for i in range(0,len(name)+1):
    for j in range(len(name),i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(name[i-1],end=' ')
    print()
    
SyntaxError: multiple statements found while compiling a single statement

name='bharath'
for i in range(0,len(name)+1):
    for j in range(len(name),i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(name[i-1],end=' ')
    print()

    
          
    
            b 
          h h 
        a a a 
      r r r r 
    a a a a a 
  t t t t t t 
h h h h h h h 

#9.name col printing

name='bharath'
for i in range(0,len(name)+1):
    for j in range(len(name),i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(name[k],end=' ')
    print()

    
              
            b 
          b h 
        b h a 
      b h a r 
    b h a r a 
  b h a r a t 
b h a r a t h 
