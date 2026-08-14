Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# set
name = {'bharath','kumar'}
type(name)
<class 'set'>
bio = {'name':'bharath','age':21,'city':'chennai'}
type(bio)
<class 'dict'>
#example
>>> bike = {'pulsar','duke','R15','MT15','gixxer'}
>>> bike
{'MT15', 'duke', 'gixxer', 'R15', 'pulsar'}
>>> #unordered collection of datasets
>>> bike
{'MT15', 'duke', 'gixxer', 'R15', 'pulsar'}
>>> #once it will be taken in a random order and then continues with the same
>>> bike.add('NS200')
>>> bike
{'NS200', 'MT15', 'duke', 'gixxer', 'R15', 'pulsar'}
>>> #example2
>>> a = {10,20,30,40,50}
>>> b = {15,25,35,45,55}
>>> a.difference(b)
{40, 10, 50, 20, 30}
>>> a = {1,2,3,4,5,6,7,8}
>>> b = {4,5,6,9}
>>> a
{1, 2, 3, 4, 5, 6, 7, 8}
>>> b
{9, 4, 5, 6}
>>> a.difference(b)
{1, 2, 3, 7, 8}
>>> a.difference_update(b)
>>> a.pop()
1
>>> a
{2, 3, 7, 8}
>>> b
{9, 4, 5, 6}
>>> a.union(b)
{2, 3, 4, 5, 6, 7, 8, 9}
>>> a
{2, 3, 7, 8}
>>> a.clear()
a
set()
b.clear()
b
set()
a = {1,2,3,4,5}
b = {3,4,5}
b.issubset(a)
True
a.issuperset(a)
True

#Dictionary

# dictionary is not indexed
# dictionary is a ordered collection of data items
# instead of indexing,dict follows {key:value} as a paired items
# duplicate values are not followed
 bio = {'name':'bharath','age':23,'city':'chennai','yob':2004}
 
SyntaxError: unexpected indent
bio = {'name':'bharath','age':23,'city':'chennai','yob':2004}
bio
{'name': 'bharath', 'age': 23, 'city': 'chennai', 'yob': 2004}
type(bio)
<class 'dict'>
bio[0]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    bio[0]
KeyError: 0
bio['name']
'bharath'
bio['yob']
2004

#example

bio
{'name': 'bharath', 'age': 23, 'city': 'chennai', 'yob': 2004}
bio.items()
dict_items([('name', 'bharath'), ('age', 23), ('city', 'chennai'), ('yob', 2004)])
bio.keys()
dict_keys(['name', 'age', 'city', 'yob'])
bio.values()
dict_values(['bharath', 23, 'chennai', 2004])
bio.pop('yob')
2004
bio
{'name': 'bharath', 'age': 23, 'city': 'chennai'}
