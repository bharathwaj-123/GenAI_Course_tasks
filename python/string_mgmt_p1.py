Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """# string handling management
>>> # --------------------------
>>> 
>>> # categories
>>> # ----------
>>> 
>>> # string operations (indexing / slicing / ranging)
>>> # string methods (concatenation / repetition / formatting)
>>> # string supporting functions(string dotted functions)
>>> 
>>> # string operations
>>> # -----------------
>>> 
>>> # string = sequence of characters
>>> 
>>> # string are enclosed with quotations
>>> 
>>> name = 'rajesh'
>>> 
>>> # rajesh
>>> # 012345
>>> 
>>> name
'rajesh'
# indexing = getting a particular character from a string using its INDEX value

name[0]
'r'
name[1]
'a'
name[3]
'e'
name[5]
'h'
name[7]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    name[7]
IndexError: string index out of range

# this process is called STRING TRAVERSING / POSITIVE INDEXING

# r a j e s h
#-6-5-4-3-2-1

# NOTE: space is meaningful in python as it takes a index value

name[-1]
'h'
name[-2]
's'
name[-4]
'j'
name[-6]
'r'
name[-7]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    name[-7]
IndexError: string index out of range


name = 'alvina rk'

name[0]
'a'
name[3]
'i'
name[5]
'a'
name[6]
' '
name[8]
'k'
# slicing = getting a particular portion from a string using (starting : stopping)

name[0:3] # 012
'alv'
name[0:4] # 0123
'alvi'
name[0:5]
'alvin'
name[7:9]
'rk'
name[4:9]
'na rk'

# string reverese
# ----------------

name
'alvina rk'
name[::-1]
'kr anivla'

# NIBROK KORBIN

name='rajesh'

name[0:3]
'raj'

name[-6:-3]
'raj'
#-6-5-4
# r a j

name
'rajesh'

name[::2]
'rjs'
name[::3]
're'
name[::-2]
'hea'

# ranging = almost similar to slicing

name='manju nathan'
name[:5]
'manju'
name[5:]
' nathan'
name='jason andrew'
name[:5]
'jason'
name[5:]
' andrew'

name='hepzibah vinithra rk'





name[:5]
'hepzi'
name[0:5]
'hepzi'
name[:-15]
'hepzi'
name[-19:-15]
'epzi'
name[-20:-15]
'hepzi'
name[9:14]
'vinit'
name[9:13]
'vini'

name
'hepzibah vinithra rk'

name[9:13]
'vini'
name[13:9]
''
name[13:9:-1]
'tini'


# string methods(concatenation / repetition / formatting)

name='rajesh'
age=41
city='dindigul'


name + city
'rajeshdindigul'
10+10
20
'10'+'10'
'1010'
name+age
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    name+age
TypeError: can only concatenate str (not "int") to str
name + str(age)
'rajesh41'
age
41
# repetition

name
'rajesh'

name*5
'rajeshrajeshrajeshrajeshrajesh'

# formatting
# ----------

# manual formatting
name
'rajesh'
age
41
city
'dindigul'

print('my name is {0} from {1} aged {2}').
SyntaxError: invalid syntax
print('my name is {0} from {1} aged {2}')
my name is {0} from {1} aged {2}
print('my name is {0} from {1} aged {2}'.format(name,city,age))
my name is rajesh from dindigul aged 41
print('my name is {} from {} aged {}'.format(name,city,age))
my name is rajesh from dindigul aged 41
print('my name is {} from {} aged {}'.format(name,age,city))
my name is rajesh from 41 aged dindigul

# automated formatting
print('my name is %s from %s aged %d' % (name,city,age))
my name is rajesh from dindigul aged 41
print('my name is %s from %s aged %s' % (name,city,age))
my name is rajesh from dindigul aged 41
# general formatting
print('name is',name)
name is rajesh
print('name is',name,'hometown is',city)
name is rajesh hometown is dindigul
