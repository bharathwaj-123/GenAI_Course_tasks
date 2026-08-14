Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #decision making statements
>>> #conditional statements
>>> 
>>> # if
>>> # if else
>>> # if elif else
>>> # nested if
>>> 
>>> #---------------------
>>> #if statement
>>> #---------------------
>>> #if the given test condition is satisfied then it prints something if not it prints nothing
>>> 
>>> #if else statement
>>> #------------------
>>> # if the given condition is satisfied then it returns IF block if not then exexutes ELSE block statements
>>> 
>>> #if elif else statements
>>> #------------------------
>>> # if a single value to be checked with multiple test conditions (eg.Grade of marks)
>>> 
>>> # nested if statement
>>> #---------------------
>>> # if statement inside another if statement
>>> 
>>> #if statement
>>> 
>>> name = 'bharath'
>>> if name == 'bharath':
...     print("Matching")
... 
...     
Matching
>>> 
>>> # if else statement
>>> 
>>> age = 23
>>> if age>=18:
...     print("Eligible to vote")
else:
    print("Not eligible")

    
Eligible to vote

#if elif else statement(Grade of marks)

mark = 63
if mark > 90 and mark <=100:
    print('O Grade')
elif mark > 80 and mark <=90:
    print('A Grade')
elif mark > 70 and mark <=80:
    print('B Grade')
elif mark > 60 and mark <= 70:
    print('C Grade')
elif mark >= 50 and mark <=60:
    print('D Grade')
elif mark < 50:
    print('U Grade')
else:
    print("Enter Valid mark")

    
C Grade

#Nested if statement

age = 23
weight = 67
if age >= 18:
    print('Age is eligible')
    if weight >= 50:
        print('Eligible to donate blood')
    else:
        print('Not Eligible')
else:
    print('Under 18 cannot donate blood')

    
Age is eligible
Eligible to donate blood
