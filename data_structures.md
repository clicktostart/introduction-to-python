# Data Structures

We know how to use variables to store values. And so far our examples have been
pretty small and well contained. What if we need to store 1,000 sets of data...
are we really going to make 1,000 variables? We should never have to. Python 
and other programming languages caters for this and for other scenarios with a
variety of **data structures** - methods for storing data in a computer
in an organised fashion.

## List
Well, the name kind of gave it away. In Python we use lists to store an
ordered sequence of items.

```python
# A list of items are enclosed by square brackets
# Each item is separated by a comma
# And that's right, a variable can store a list just like it can for 
# strings, numbers or booleans
face = ['eyes', 'nose', 'ears', 'mouth']

# List of numbers
favourite_numbers = [3, 42, 69, 7]

# Yes, any kind of number
more_numbers = [4.5, 2, 10.823]

# Empty list
nothing = []

# No limitation, mix and match
random_variable = 24 / 3
random_list = ['hill', 12, 'c', random_variable]

# Lists can be stored inside, you guessed it, lists!
listception = ['bob', ['damian', 'junior', 'stephen', 3], 9, 'rita', [67]]
```

It's quite easy to make lists. It's also very easy to get an item from a list.
Recall that lists are an **ordered** sequence of items. To get an item from a 
list, we can use the item's index - the position of a list item.

```python
# Let's take the face variable from before
face = ['eyes', 'nose', 'ears', 'mouth']

# The position of a list starts from 0
# All we simply do is use the variable, put square brackets in front and then
# put the index inside of the square brackets
face[0] # First item, 'eyes'
face[1] # Second item, 'nose'
face[2] # Third item, 'ears'
face[3] # Fourth item, 'mouth'
```

As you've noticed, the last item is one less than the length of the list. Let's
say you didn't create the list, how would know it's length? Use the `len`
function

```python
len(face)       # 4
len([5,False])  # 2
len([])         # 0
```

Let's go back to more list indices

```python
favourite_numbers = [3, 42, 69, 7]
favourite_numbers[2] # Third item, 69
# Remember, the index starts at 0!

# How do we get 'stephen'?
# Simple, first get the list containing the Marleys - 2nd item of listception
# Then get the the 3rd of item of that list
listception = ['bob', ['damian', 'junior', 'stephen', 3], 9, 'rita', [67]]
listception[1][2]

# To get the last item use the last index.
# A list with 5 items has indices: 0, 1, 2, 3, 4
listception[4] # [67]
# To get the actual number you do the following
listception[4][0] # 67

# Have a little more fun with len before you go
len(listception) # 5 - ['bob', ['damian', 'junior', 'stephen', 3], 9, 'rita', [67]]
len(listception[1]) # 4 - ['damian', 'junior', 'stephen', 3]
```

You can use negative numbers for list indices as well. Instead of going from 
left to right, you'll get the items from right to left.

```python
favourite_numbers = [3, 42, 69, 7]
favourite_numbers[-1] # 7
favourite_numbers[-2] # 7
favourite_numbers[-3] # 7
favourite_numbers[-4] # 7
```

You should also get accustomed to some common errors. Remember, errors are 
awesome because they tell us exactly what's wrong. Let's try the following:

```python
favourite_numbers = [3, 42, 69, 7]
favourite_numbers[4]
favourite_numbers[-5]
```

If you try the above in your Python interpreter you should get

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

So if ever you see that error you know that the list doesn't have an item for
that index. Either the list is missing items or the index is inappropriate for
the list.

### List Slicing

Now that you're comfortable with indices, let's to some cool things with lists.
Slicing is taking a portion of a list and creating a new one. Think of it like
cutting a slice of cake, but the original one stays intact (wouldn't that be
absolutely amazing?). Let's see below:

```python
fruits = ['banana', 'mango', 'tomato', 'plum', 'guava']
fruits[1] # 'mango'

# Let's slice to get a new list that starts from mango
fruits[1:]
# Above we tell Python we want a list that starts from the fruit's second item
# (recall that the 2nd item has index 1) till the end of the list

# So if we wanted plum and guava chow (ewww) we'll do the following
fruits[3:]

# Let's slice to get a new list that ends with plum
fruits[:4]
# Above we tell Python to start slicing from the beginning and end with fruit's
# 4th item. It's a little tricky, when a number came before the colon we gave
# the item's index. Now we give one more than the item's index. Practice more!
fruits[:5] # ['banana', 'mango', 'tomato', 'plum', 'guava']
fruits[:1] # ['banana']
fruits[:3] # ['banana', 'mango', 'tomato']

# Let's take it a step further and put them both together
fruits[1:4] # ['mango', 'tomato', 'plum']
# Make sure you understand, you're skipping the first element and going up to 
# the fourth one. Skip banana and stop and plum
fruits[2:3] # Skip banana and mango, end at tomato. So only tomato!
```

### List Functions

Lists also come with useful functions that can changed the elements contained
within. Let's look at how easy it is to add to a list:

```python

my_first_list = ['bleach', 'naruto']
my_second_list = ['coldplay', 'chainsmokers', 'dj khaled']
# We can add two lists together
my_third_list = my_first_list + my_second_list
my_third_list # ['bleach', 'naruto', 'coldplay', 'chainsmokers', 'dj khaled']
# And yes, order matters
my_fourth_list = my_second_list + my_first_list
my_fourth_list # ['coldplay', 'chainsmokers', 'dj khaled', 'bleach', 'naruto']


alpha = ['a', 'b', 'c', 'd', 'e']
# You can add an item to a list by the append method
alpha.append('f')
alpha # ['a', 'b', 'c', 'd', 'e', 'f']
alpha.append('g')
alpha # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
```

`append` simply adds an item to the end of the list. You may be asking... why does
that function come after the list and '.'? That's because, it's no ordinary
function, it's a method. We'll learn more about them later when we discucss
Classes and Objects. For now, think of lists as special variables that can
store both data and functions, which we call methods.

```python
# Here are a couple other nifty functions that your list has access to
# Sort is a breeze
num_list = [7, 0.5, 23, 9]
num_list.sort()
num_list # [0.5, 7, 9, 23]

# As well as reversing
num_list.reverse()
num_list # [23, 9, 7, 0.5]
num_list.reverse()
num_list # [0.5, 7, 9, 23]
```

### Lists and If Statements
It's not hard to imagine that there'll be a time when you'd like to know if an
item is inside a list. Luckily Python makes this dead simple

```python
cool_kids = ['carla', 'prakash', 'john', 'priya', 'mei']
'marcus' in cool_kids # False, damn!
'priya' in cool_kids # True

# Use it in if statements like other Boolean expressions
evens = [2, 4, 6, 8, 10, 12]

# This does not print
if 5 in evens:
    print('Gotcha! You\'re not in the list of even numbers')

awesome_number = 8
# This prints
if awesome_number in evens:
    print('Say it loud, I\'m even and proud')
```

### Exercises 1
1. A list has a length of 4, what are its indices?
2. Consider the list `twelves = [12, 'twelve', [12.0]]`. What are:
    1. `twelves[1]`
    2. `twelves[2]`
    3. `twelves[-8]`
    4. `twelves[-1][0] / 3`
    5. `twelves[-3]`
3. Consider `a = [12, 45, 88, 93, 232, 121]`
    1. Add 33 to a
    2. Slice a so that a new variable b has from the 3rd to 6th items of a
    3. Add 90 to b
    4. Sort b
    5. Reverse a
4. Given list `l1 = ['morning', 'noon', 'evening']` and `l2 = [9.9, 3, 11.5]`, create
    a list l3 using list functions and operators so that it has
    [11.5, 9.9, 3, 'morning', 'noon', 'evening', 9.9, 3, 11.5]. 
5. Write a function is_waldo_here that accepts a list of suspects. If 'waldo' is
    in the list then **return** "We can find Waldo, go search!". Otherwise 
    return, "Maybe we'll find him... tomorrow!"

## Tuples
Lists are pretty flexible, we can change their values whenever we want to. For 
e.g. consider:
```python
peanuts = ['charlie', 'snoopy', 'linus', 'schroeder']

# We can swap out linus for lucy like this:
peanuts[2] = 'lucy'
peanuts  # ['charlie', 'snoopy', 'lucy', 'schroeder']
```

In programming, the fancy word we use to describe that we can change the value
after it's set is *mutable*. Tuples are like lists in that they store a sequence
of data but tuples are *immutable*. You guessed it, once the data is defined 
then we can't change it.

```python
# For tuples, we use normal brackets as opposed to square brackets
coordinate1 = (1, 2, 3)
# As with lists, you must separate each value by a comma

mixed_tuple = (True, 'chris gayle', (4,4))
# Tuples can store mixed values, and even tuples!

# You access data from a tuple the same way you access them from a list
mixed_tuple[0] # True
# Yes, the index also starts at 0
mixed_tuple[2][1] # 4
```

Remember that whole immutability thing? Let's try it with coordinate1:
```python
coordinate1[1] = 26 # (1, 26, 3) right? Nope...
```

You should get the following error
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

Let's go again...
```python
# You can add elements to tuples
x_o = ('x',) # So a tuple with a single element needs to trailing comma
# There really is no purpose for a tuple with a single element -_-
x_o += ('o',) # ('x', 'o')
```

Wait a minute, tuples are immutable so why are we changing them? Well
the + operator is actually creating a new tuple. As we learn about Classes and
Objects we'll also learn about references and why this is important and correct.

Before we get more practice with tuples, one more bit of fun!
```python
coordinate1 = (1, 2, 3)
5 in coordinate1 # False
1 in coordinate1 # True
len(coordinate1) # 3
coordinate1[1:] # (2, 3)
coordinate1[-1] # 3
```

### Exercises 2
1. t1 = ('w', 'a', 'l', 'l', 'e', 4, 0, 4)
    Slice the tuple so that it only contains ('w', 'a', 'l', 'l', 'e')
2. Write a function funky_points_sum which takes tuples t1 and t2 as arguments
    and adds the 2nd item of t1 to the 1st item of t2, then multiplies that 
    result by the 2nd item of t2 minus the first item of t1.

## Dictionaries
A dictionary is a mapping between a key and value. Huh? Well let's remember 
lists for one bit. Every list item has an index, a number. That's essentially
a mapping between a number and a value. e.g. `['hi', 'five', 'low', 'slow']` has
a mapping: 0 -> 'hi', 1 -> 'five', 2 -> 'low', 3 -> 'slow'. A dictionary
generalises that further, the mapping doens't have to be from a sequential 
integer to a value but a unique **key**. Dictionaries are sequences of 
*key-value* pairings. Let's have a look:

```python
grades = {'kevin': 30, 'jabari': 25}
# Let's say kevin and jabari both need to study, ASAP
# With a dictionary we can get their grades as follows:
grades['kevin'] # 30
grades['jabari'] # 25

# Let's get more practice
# Multi-line dictionaries normally have the brackets spanning a few lines
student_profile = {
    'name': 'roger rabbit',
    'age': 14,
    'courses': ['programming', 'maths', 'english', 'spanish'],
    'loves code': True
}

# You can store almost any type as the value, make the keys consistent
student_profile['name'] # 'roger rabbit'
student_profile['courses'][-2] # 'english'

# You can add key-value pairs as well
student_profile['mentor'] = 'plato'
student_profile # {'courses': ['programming', 'maths', 'english', 'spanish'], 'loves code': True, 'mentor': 'plato', 'name': 'roger rabbit', 'age': 14}
# Your order may be different, that's fine. Dictionaries don't keep order

if student_profile['loves code']:
    print('yayy')
```
Keep the following in mind while creating dictionaries:
* Use curly braces to put data inside a dictionary
* Separate each key-value pairing by a comma
* As with lists and tuples, use square brackets to get values from a dictionary

```python
# At time it might be useful to see the keys or the values alone
student_profile.keys() # dict_keys(['courses', 'loves code', 'mentor', 'name', 'age'])
student_profile.values() # dict_values([['programming', 'maths', 'english', 'spanish'], True, 'plato', 'roger rabbit', 14])

if 'favourite course' not in student_profile.keys():
    student_profile['favourite course'] = 'python'

student_profile['favourite course'] # 'python'
```

### Exercises 3
1.  A dictionary is an unordered sequence of key-value pairs. True or False?
2.  Consider the dict that contains European football clubs and the amount of
    Champions League trophies they won: 
    `clubs = {‘real madrid’: 12, ‘ac milan’: 7, ‘bayern munich’: 5, ‘ajax’: 4}`.
    1. Real Madrid are undoubtedly the greatest football team ever created but 
    there’s space for that other Spanish team. Add Barcelona with their measly
    5 trophies.
    2. How many trophies did ajax win? Get the value from the dictionary
    3. We have a function that’s interested in the teams but not so much
    their trophy haul. Return a list of keys for `clubs`
    4. A very ambitious but deluded Manchester City fan claims that his club
    has won champions league. Verify with a condition that his club has not.

