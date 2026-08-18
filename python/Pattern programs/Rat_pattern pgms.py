Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Pattern programs
>>> 
>>> # Right angle triangle(Rat)
>>> 
>>> # 1.Rat - Number row printing
>>> 
>>> for i in range(1,6):
...     for j in range(0,i):
...         print(i,end=' ')
...     print()
... 
...     
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
>>> 
>>> # 2.Rat - Number column printing
>>> 
>>> for i in range(1,6):
...     for j in range(1,i+1):
...         print(j,end=' ')
...     print()
... 
...     
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
>>> 
>>> # 3.Rat - Upper row printing

for i in range(1,6):
    for j in range(0,i):
        print(chr(i+64),end=' ')
    print()

    
A 
B B 
C C C 
D D D D 
E E E E E 

# 4.Rat - Upper col printing

for i in range(1,6):
    for j in range(0,i):
        print(chr(j+65),end=' ')
    print()

    
A 
A B 
A B C 
A B C D 
A B C D E 

# 5.Rat - star printing

for i in range(1,6):
    for j in range(0,i):
        print('*',end=' ')
    print()

    
* 
* * 
* * * 
* * * * 
* * * * * 

# 6.Rat - Lower row printing

for i in range(1,6):
    for j in range(0,i):
        print(chr(i+96),end=' ')
    print()

    
a 
b b 
c c c 
d d d d 
e e e e e 

# 7.Rat - Lower column printing

for i in range(1,6):
    for j in range(0,i):
        print(chr(j+97),end=' ')
    print()

    
a 
a b 
a b c 
a b c d 
a b c d e 

# 8.Rat - Name row printing

name = 'bharath'
for i in range(0,7):
    for j in range(0,i+1):
        print(name[i],end=' ')
    print()

    
b 
h h 
a a a 
r r r r 
a a a a a 
t t t t t t 
h h h h h h h 

# 9.Name column printing

for i in range(0,7):
    for j in range(0,i+1):
        print(name[j],end=' ')
    print()

    
b 
b h 
b h a 
b h a r 
b h a r a 
b h a r a t 
b h a r a t h 
