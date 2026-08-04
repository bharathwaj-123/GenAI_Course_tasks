Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Python Native datatypes / python collections / python NON PRIMITVE DATATYPES
# -----------------------------------------------------------------------------

# primitive datatypes:- String/Float/Int/Complex/Boolean

name='rajesh'

type(name)
<class 'str'>

name='rajesh','kumar'

type(name)
<class 'tuple'>

# Non primitive datatypes --> list / tuple / set / dict


# LIST
# ----

# enclosed with []
# list contains ordered collection of data items
# list values are indexed
# values are mutable and changeable
# list supports duplicate values
# list contains hetrogenous values

car = ['creta','civic','santro','wagonr','creta','beat']

type(car)
<class 'list'>
car
['creta', 'civic', 'santro', 'wagonr', 'creta', 'beat']
car[0]
'creta'
car[2]
'santro'
car[4]
'creta'
car[4]==car[0]
True
car[0]
'creta'

car[0]='polo'

car
['polo', 'civic', 'santro', 'wagonr', 'creta', 'beat']

car[1:3]
['civic', 'santro']
car[3:]
['wagonr', 'creta', 'beat']
cae[:3]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    cae[:3]
NameError: name 'cae' is not defined. Did you mean: 'car'?
car[:3]
['polo', 'civic', 'santro']

# list methods / list supporting functions / list operations
# -----------------------------------------------------------

car
['polo', 'civic', 'santro', 'wagonr', 'creta', 'beat']

car.append('swift')
car
['polo', 'civic', 'santro', 'wagonr', 'creta', 'beat', 'swift']
car.append('swift','kushaq')
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    car.append('swift','kushaq')
TypeError: list.append() takes exactly one argument (2 given)

car.clear()
car
[]
car.append('creta')
car.append('swift')
car.append('beetle')
car
['creta', 'swift', 'beetle']

car.extend(['ciaz','civic','taigun'])
car
['creta', 'swift', 'beetle', 'ciaz', 'civic', 'taigun']

car.extend(['ciaz','civic','taigun'],['tiguan','rapid'])
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    car.extend(['ciaz','civic','taigun'],['tiguan','rapid'])
TypeError: list.extend() takes exactly one argument (2 given)
car
['creta', 'swift', 'beetle', 'ciaz', 'civic', 'taigun']

car.count('swift')
1
car.count('ciaz')
1
car.index('civic')
4
car[1]
'swift'

car.insert(1,'omni')
car
['creta', 'omni', 'swift', 'beetle', 'ciaz', 'civic', 'taigun']

car[1]='rk'
car
['creta', 'rk', 'swift', 'beetle', 'ciaz', 'civic', 'taigun']
car.pop()
'taigun'
car
['creta', 'rk', 'swift', 'beetle', 'ciaz', 'civic']
car.pop()
'civic'
car
['creta', 'rk', 'swift', 'beetle', 'ciaz']

car.pop('rk')
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    car.pop('rk')
TypeError: 'str' object cannot be interpreted as an integer
car.pop(2)
'swift'
car
['creta', 'rk', 'beetle', 'ciaz']

car.remove('rk')
car
['creta', 'beetle', 'ciaz']
car.remove()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    car.remove()
TypeError: list.remove() takes exactly one argument (0 given)
car.remove('Ciaz')
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    car.remove('Ciaz')
ValueError: list.remove(x): x not in list

car
['creta', 'beetle', 'ciaz']

car.reverse()
car
['ciaz', 'beetle', 'creta']

car
['ciaz', 'beetle', 'creta']
car.sort()
car
['beetle', 'ciaz', 'creta']

car
['beetle', 'ciaz', 'creta']




car
['beetle', 'ciaz', 'creta']



car_dup = car


car
['beetle', 'ciaz', 'creta']

car_dup
['beetle', 'ciaz', 'creta']


car_dup[1]
'ciaz'

car_dup[1] = 'santafe'


car_dup
['beetle', 'santafe', 'creta']


car
['beetle', 'santafe', 'creta']

dup = car.copy()



car
['beetle', 'santafe', 'creta']


dup
['beetle', 'santafe', 'creta']


dup[2]='rk'


dup
['beetle', 'santafe', 'rk']


car
['beetle', 'santafe', 'creta']

# tuple
# -----

# tuple is enclosed with ()
# tuple values are also ordered collection
# tuple values are indexed
# tuple values support duplicates
# tuple values are IMMUTABLE


t = ('rajesh','kumar','rajesh','kumar')

type(t)
<class 'tuple'>

t.count('kumar')
2
t.index('rajesh')
0
t
('rajesh', 'kumar', 'rajesh', 'kumar')

>>> t = list(t)
>>> t
['rajesh', 'kumar', 'rajesh', 'kumar']

>>> t.append('alvina')
>>> t
['rajesh', 'kumar', 'rajesh', 'kumar', 'alvina']
>>> 
>>> 
>>> t = tuple(t)
>>> 
>>> t
('rajesh', 'kumar', 'rajesh', 'kumar', 'alvina')
>>> t1 = (10,20,30)
>>> 
>>> t
('rajesh', 'kumar', 'rajesh', 'kumar', 'alvina')
>>> t1
(10, 20, 30)

>>> 
>>> t = t + t1
>>> 
>>> t
('rajesh', 'kumar', 'rajesh', 'kumar', 'alvina', 10, 20, 30)
