Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# 8940655130

# 89406*****

'89406'.ljust(5,'*')
'89406'
'89406'.ljust(10,'*')
'89406*****'

# nested if
# ---------

# if one test condition is given inside another test condition

age = 16
weight = 53

if age >= 15:
    print('age wise eligible')
    if weight >= 50:
        print('eligible to donate blood')
    else:
        print('not eligible')
else:
    print('age criteria not matched')

    
age wise eligible
eligible to donate blood

age = 12
weight = 53
if age >= 15:
    print('age wise eligible')
    if weight >= 50:
        print('eligible to donate blood')
    else:
        print('not eligible')
else:
    print('age criteria not matched')

    
age criteria not matched

age = 23
weight = 49

if age >= 15:
    print('age wise eligible')
    if weight >= 50:
        print('eligible to donate blood')
    else:
        print('not eligible')
else:
    print('age criteria not matched')

    
age wise eligible
not eligible


car = ['creta','ciaz','cruze','santro','santafe']

car[:3]
['creta', 'ciaz', 'cruze']

car[0]
'creta'
car[0].startswith('c')
True

# looping statements
# ------------------

# looping = same set of actions repeated many times till n-1 times based on given condition

# for loop
# while loop

# what is iterative statements???
# -------------------------------

# Iterative = going through the elements of a given python collection(list/set/tuple/dict)
#             using for loop / while loop

car
['creta', 'ciaz', 'cruze', 'santro', 'santafe']


for i in range(5):
    print(i)

    
0
1
2
3
4
for i in range(0,5):
    print(i)

    
0
1
2
3
4
for i in range(0,5,1):
    print(i)

    
0
1
2
3
4
for i in range(1,11,1):
    print(i)

    
1
2
3
4
5
6
7
8
9
10
for i in range(1,11,1):
    print(i,end=' ')

    
1 2 3 4 5 6 7 8 9 10 
for i in range(1,11,1):
    print(i,end='_')

    
1_2_3_4_5_6_7_8_9_10_
for i in range(1,11,1):
    print(i)
    print('_')

    
1
_
2
_
3
_
4
_
5
_
6
_
7
_
8
_
9
_
10
_
for i in range(1,11):
    print(i, end=' ')

    
1 2 3 4 5 6 7 8 9 10 

# print even numbers b/w 1 to 10

for i in range(2,11,2):
    print(i, end=' ')

    
2 4 6 8 10 

# print odd numbers b/w 1 to 10
for i in range(1,11,2):
    print(i, end=' ')

    
1 3 5 7 9 

# 1 - odd
# 2 - even
# 3 - odd
# 4 - even
# 5 - odd


for i in range(1,11):
    if i%2==1:
        print(i,' - odd')
    else:
        print(i,' - even')

        
1  - odd
2  - even
3  - odd
4  - even
5  - odd
6  - even
7  - odd
8  - even
9  - odd
10  - even
2 % 10
2
3 % 10
3
7 % 10
7
9 % 10
9
12 % 10
2

car
['creta', 'ciaz', 'cruze', 'santro', 'santafe']


for i in car:
    print(i)

    
creta
ciaz
cruze
santro
santafe

for i in car:
    if i.startswith('c'):
        print(i)

        
creta
ciaz
cruze

for i in car:
    if i.endswith('e'):
        print(i)

        
cruze
santafe

name = ['sachin','priya','padma','viswa','kabil','deepi','tamil','akshy','danny']


len('rajesh')
6
for i in name:
    if len(i)==5:
        print(i)

        
priya
padma
viswa
kabil
deepi
tamil
akshy
danny
# print name that starts with 'p'

for i in name:
    if i.startswith('p'):
        print(i)

        
priya
padma

for i in name:
    if i.endswith('a'):
        print(i)
    elif i.endswith('e'):
        print(i)
    elif i.endswith('i'):
        print(i)
    elif i.endswith('o'):
        print(i)
    elif i.endswith('u'):
        print(i)

        
priya
padma
viswa
deepi

vowels = ['a','e','i','o','u']
for i in name:
    if i.endswith([i for i in vowels]):
        print(i)

        
Traceback (most recent call last):
  File "<pyshell#158>", line 2, in <module>
    if i.endswith([i for i in vowels]):
TypeError: endswith first arg must be str or a tuple of str, not list
[i for i in vowels]
['a', 'e', 'i', 'o', 'u']
for i in name:
    if i.endswith('a' or 'e' or 'i' or 'o' or 'u'):
        print(i)

        
priya
padma
viswa
for i in name:
    if i.endswith('a','e','i','o','u'):
        print(i)

        
Traceback (most recent call last):
  File "<pyshell#163>", line 2, in <module>
    if i.endswith('a','e','i','o','u'):
TypeError: endswith() takes at most 3 arguments (5 given)
for i in name:
    if i.endswith('a'|'e'|'i'|'o'|'u'):
        print(i)

        
Traceback (most recent call last):
  File "<pyshell#165>", line 2, in <module>
    if i.endswith('a'|'e'|'i'|'o'|'u'):
TypeError: unsupported operand type(s) for |: 'str' and 'str'


for i in name:
    if i.endswith('a') or i.endswith('i'):
        print(i)

        
priya
padma
viswa
deepi
vowels
['a', 'e', 'i', 'o', 'u']



for i in name:
    for j in vowels:
        if i.endswith(j):
            print(i)

            
priya
padma
viswa
deepi
# S1 S2 S3
# P1 P2 P3

# S1 P1
# S1 P2
# S1 P3
>>> 
>>> # S2 P1
>>> # S2 P2
>>> # S2 P3
>>> 
>>> # S3 P1
>>> # S3 P2
>>> # S3 P3
>>> 
>>> # while loop
>>> 
>>> 
>>> 
>>> # for loop
>>> # --------
>>> 
>>> # CORM process ---> Check Once Runs Many time
>>> # for loop checks the condition only once and runs the loop many times (n-1)
>>> 
>>> # while loop
>>> # ----------
>>> 
>>> # checks the every single time and runs the loop till the condition is TRUE
>>> # it is mandate to give the incremental / decremental value in while loop
>>> 
