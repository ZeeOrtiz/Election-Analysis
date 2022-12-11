print("hello world")
>>> type(3)
<class 'int'>
>>> ballots = 1,341
>>> ballots
(1, 341)
>>> type(ballots)
<class 'tuple'>
>>> ballots = 1341
>>> ballots
1341
>>> type(ballots)
<class 'int'>
>>> ballots = 1341
>>> ballots = 1,341
>>> ballots
(1, 341)
>>> type(ballots)
<class 'tuple'>
>>> type(73.81)
<class 'float'>
>>> type("hello world"
... type("Hello World")
  File "<stdin>", line 2
    type("Hello World")
       ^
SyntaxError: invalid syntax
>>> type("Hello World")
<class 'str'>
>>> type()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: type() takes 1 or 3 arguments
>>> type(true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> type(True)
<class 'bool'>
>>> type('True')
<class 'str'>
>>> num_candidates = 3
>>> winning_percentages = 73.81
>>> candidate = "Diane"
>>> won_election = True
>>> candidate_name = "Diane"
>>> help("keywords")

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not

>>> 5 + 2 * 3
11
>>> 8 // 5 - 3
-2
>>> 8 + 22 * 2 - 4
48
>>> 16 - 3 / 2 + 7 - 1
20.5
>>> 3 ** 3 % 5
2
>>> 5 + 9 * 3 / 2 - 4
14.5
>>> (5 + 2) * 3
21
>>> (8 // 5) - 3
-2
>>> 8 + (22 * (2 - 4))
-36
>>> 16 - 3 / (2 + 7) - 1
14.666666666666666
>>> 3 ** (3 % 5)
27
>>> 5 + (9 * 3 / (2 - 4))
-8.5
>>>  5 + (9 * 3 / 2 - 4)
  File "<stdin>", line 1
    5 + (9 * 3 / 2 - 4)
    ^
IndentationError: unexpected indent
>>> 5 + (9 * 3 / 2 - 4)
14.5
>>> counties = ["Arapahoe","Denver","Jefferson"]
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> my_list - []
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'my_list' is not defined
>>> list()
[]
>>> my_list
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'my_list' is not defined
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> counties[0]
'Arapahoe'
>>> counties[2]
'Jefferson'
>>> print(counties[2])
Jefferson
>>> print(counties[-1])
Jefferson
>>> counties[-2]
'Denver'
>>> len(counties)
3
>>> counties[0:2]
['Arapahoe', 'Denver']
>>> counties[0:1]
['Arapahoe']
>>> counties[:2]
['Arapahoe', 'Denver']
>>> counties[1:]
['Denver', 'Jefferson']
>>> counties.append("El Paso")
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties.insert(2, "El Paso")
>>> counties
['Arapahoe', 'Denver', 'El Paso', 'Jefferson', 'El Paso']
>>> counties.remove("El Paso")
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties.pop("El Paso")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an integer
>>> counties.pop(3)
'El Paso'
>>> counties.pop(-1)
'Jefferson'
>>> counties
['Arapahoe', 'Denver']
>>> counties.insert(2, "Jefferson")
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> counties[2] = "El Paso"
>>> counties
['Arapahoe', 'Denver', 'El Paso']
>>> counties
['Arapahoe', 'Denver', 'El Paso']
>>> counties = ["Arapahoe","Denver","Jefferson"]
>>> counties.insert(2, "El Paso")
>>> counties
['Arapahoe', 'Denver', 'El Paso', 'Jefferson']
>>> counties = ["Arapahoe","Denver","Jefferson"]
>>> counties.inset(1, "El Paso")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'inset'
>>> counties.insert(1, "El Paso")
>>> counties
['Arapahoe', 'El Paso', 'Denver', 'Jefferson']
>>> counties(-0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
>>> counties.remove("Arapahoe")
>>> counties
['El Paso', 'Denver', 'Jefferson']
>>> counties.insert(1, "Jefferson")
>>> counties
['El Paso', 'Jefferson', 'Denver', 'Jefferson']
>>> counties.remove(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> counties.remove[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> counties.remove("Jefferson")
>>> counties
['El Paso', 'Denver', 'Jefferson']
>>> counties[1] = Jefferson
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Jefferson' is not defined
>>> counties[1] = "Jefferson
  File "<stdin>", line 1
    counties[1] = "Jefferson
                           ^
SyntaxError: EOL while scanning string literal
>>> counties[1] = "Jefferson
  File "<stdin>", line 1
    counties[1] = "Jefferson
                           ^
SyntaxError: EOL while scanning string literal
>>> counties.insert(3, "Denver")
>>> counties
['El Paso', 'Denver', 'Jefferson', 'Denver']
>>> counties.pop(1)
'Denver'
>>> counties.remove(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list