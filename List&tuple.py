Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #python primitive datatypes
>>> 
>>> #Int/Float/String/Boolean/Complex
>>> #Int/Float/String/Boolean/Complex
>>> name = 'bharath'
>>> type(name)
<class 'str'>
>>> 
>>> #Non-primitive datatypes/python collections/native datatypes
>>> 
>>> # List/Tuple/Set/Dictionary
>>> 
>>> #List
>>> #----
>>> # eclosed with brackets[]
>>> # contains ordered collection of data
>>> # values are indexed
>>> # mutable and changeable
>>> # values can be heterogenous
>>> 
>>> list_1 = [2,4,6,8,10]
>>> type(list_1)
<class 'list'>
>>> list_1
[2, 4, 6, 8, 10]
>>> list_1[0]
2
>>> list_1[4]
10
>>> list_1[0]= 1
>>> list_1
[1, 4, 6, 8, 10]
>>> #value is changed in 0th position as 1 permanently
list_1[3]
8
list_1[1:4]
[4, 6, 8]
list_1[:2]
[1, 4]
list_1[2:]
[6, 8, 10]
#these are the indexing,slicing and ranging operations in list

#List methods/list supporting functions

brand = ['audi','bmw','benz','tata','hyundai','honda','maruthi']
brand
['audi', 'bmw', 'benz', 'tata', 'hyundai', 'honda', 'maruthi']
brand.append('rollsroyce')
brand
['audi', 'bmw', 'benz', 'tata', 'hyundai', 'honda', 'maruthi', 'rollsroyce']
brand.count('audi')
1
brand.append('audi')
brand
['audi', 'bmw', 'benz', 'tata', 'hyundai', 'honda', 'maruthi', 'rollsroyce', 'audi']
brand.count('audi')
2
brand.extend(['toyota','jaguar','thar'])
brand
['audi', 'bmw', 'benz', 'tata', 'hyundai', 'honda', 'maruthi', 'rollsroyce', 'audi', 'toyota', 'jaguar', 'thar']
brand.remove('audi')
brand
['bmw', 'benz', 'tata', 'hyundai', 'honda', 'maruthi', 'rollsroyce', 'audi', 'toyota', 'jaguar', 'thar']
brand.remove('audi')
brand
['bmw', 'benz', 'tata', 'hyundai', 'honda', 'maruthi', 'rollsroyce', 'toyota', 'jaguar', 'thar']
brand[0]='audi'
brand
['audi', 'benz', 'tata', 'hyundai', 'honda', 'maruthi', 'rollsroyce', 'toyota', 'jaguar', 'thar']
brand.pop()
'thar'
brand.reverse()
brand
['jaguar', 'toyota', 'rollsroyce', 'maruthi', 'honda', 'hyundai', 'tata', 'benz', 'audi']

#tuple
#------
car =['audi','bmw','benz','jaguar']
dup_car = ['audi','bmw','benz','jaguar']
dup_car = car
dup_car[2]
'benz'
dup_car[2]='RR'
dup_car
['audi', 'bmw', 'RR', 'jaguar']
car
['audi', 'bmw', 'RR', 'jaguar']
#this is called SHALLOW COPY where the original list get affected even you perform changes in the duplicate list

#tuple

# tuple is enclosed with parenthesis()
# values are ordered,indexed
# supports duplicate values
# values are immutable

t = ('a','b','c','d')
type(t)
<class 'tuple'>
t.count('c')
1
t.index('a')
0
#tuple is similar to list but values are immutable,we cannot modify instead we convert into a list,modify the list[] and convert to a tuple()
t
('a', 'b', 'c', 'd')
t.append('e')
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    t.append('e')
AttributeError: 'tuple' object has no attribute 'append'
t = list(t)
t
['a', 'b', 'c', 'd']
t.append('e')
t = tuple(t)
t
('a', 'b', 'c', 'd', 'e')
