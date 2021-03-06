# Lists

We previously had a [brief introduction to lists](variables/brief_intro-to-lists.md) earlier in the course. Let's create a file `list_practice.py` and write the following:

```python
# List of strings
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

It's quite easy to make lists. It's also very easy to get an item from a list. Recall that lists are an **ordered** sequence of items. To get an item from a list, we can use the item's index - the position of a list item.

```python
# Let's take the face variable from before
# face = ['eyes', 'nose', 'ears', 'mouth']

# The position of a list starts from 0
# All we simply do is use the variable, put square brackets in front and then
# put the index inside of the square brackets
print(face[0]) # First item, 'eyes'
print(face[1]) # Second item, 'nose'
print(face[2]) # Third item, 'ears'
print(face[3]) # Fourth item, 'mouth'
```

As you've noticed, the last item is one less than the length of the list. Let's say you didn't create the list, how would know it's length? Use the `len` function

```python
face_length = len(face)
print(face_length)      # 4
print(len([5,False]))   # 2
empty_length = len([])
print(empty_length)     # 0
```

Let's go back to more list indices

```python
# Let's use favourite_numbers from before
# favourite_numbers = [3, 42, 69, 7]
print(favourite_numbers[2]) # Third item, 69
# Remember, the index starts at 0!

# How do we get 'stephen'?
# Simple, first get the list containing the Marleys - 2nd item of listception
# Then get the the 3rd of item of that list
listception = ['bob', ['damian', 'junior', 'stephen', 3], 9, 'rita', [67]]
print(listception[1][2])

# To get the last item use the last index.
# A list with 5 items has indices: 0, 1, 2, 3, 4
print(listception[4]) # [67]
# To get the actual number you do the following
print(listception[4][0]) # 67

# Have a little more fun with len before you go
print(len(listception)) # 5 - ['bob', ['damian', 'junior', 'stephen', 3], 9, 'rita', [67]]
print(len(listception[1])) # 4 - ['damian', 'junior', 'stephen', 3]
```

You can use negative numbers for list indices as well. Instead of going from left to right, you'll get the items from right to left.

```python
favourite_numbers = [3, 42, 69, 7]
print(favourite_numbers[-1]) # 7
print(favourite_numbers[-2]) # 69
print(favourite_numbers[-3]) # 42
print(favourite_numbers[-4]) # 3
```

You should also get accustomed to some common errors. Remember, errors are awesome because they tell us exactly what's wrong. Let's try the following:

```python
# favourite_numbers = [3, 42, 69, 7]
print(favourite_numbers[4])
print(favourite_numbers[-5])
```

If you try the above you should get:

```text
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

So if ever you see that error you know that the list doesn't have an item for that index. Therefore your list could be missing items or the index is inappropriate for that list.

## List Functions

Lists also come with useful functions that can changed the elements contained within. Let's look at how easy it is to add to a list:

```python
old_anime = ['bleach', 'naruto']
musicians = ['coldplay', 'chainsmokers', 'dj khaled']
# We can add two lists together
procrastination_hobbies = old_anime + musicians
print(my_third_list) # ['bleach', 'naruto', 'coldplay', 'chainsmokers', 'dj khaled']
# And yes, order matters
my_fourth_list = musicians + old_anime
print(my_fourth_list) # ['coldplay', 'chainsmokers', 'dj khaled', 'bleach', 'naruto']


alpha = ['a', 'b', 'c', 'd', 'e']
# You can add an item to a list by the append method
alpha.append('f')
print(alpha) # ['a', 'b', 'c', 'd', 'e', 'f']
alpha.append('g')
print(alpha) # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
```

`append` simply adds an item to the end of the list. You may be asking... why does that function come after the list and '.'? That's because, it's no ordinary function, it's a method. We'll learn more about them later when we discucss Classes and Objects. For now, think of lists as special variables that can store both data and functions, which we call methods.

```python
# Here are a couple other nifty functions that your list has access to
# Sort is a breeze
num_list = [7, 0.5, 23, 9]
num_list.sort()
print(num_list) # [0.5, 7, 9, 23]

# As well as reversing
num_list.reverse()
print(num_list) # [23, 9, 7, 0.5]
num_list.reverse()
print(num_list) # [0.5, 7, 9, 23]
```

## Lists and If Statements

It's not hard to imagine that there'll be a time when you'd like to know if an item is inside a list. Luckily Python makes this dead simple:

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

## Exercises

1. A list has a length of 4, what are its indices?
2. Consider the list `twelves = [12, 'twelve', [12.0]]`. What are:
   1. `twelves[1]`
   2. `twelves[2]`
   3. `twelves[-8]`
   4. `twelves[-1][0] / 3`
   5. `twelves[-3]`
3. Consider `a = [12, 45, 88, 93, 232, 121]`
   1. Add 33 to a
   2. Add 90 to b
   3. Sort b
   4. Reverse a
4. Given list `l1 = ['morning', 'noon', 'evening']` and `l2 = [9.9, 3, 11.5]`, create a list l3 using list functions and operators so that it has \[11.5, 9.9, 3, 'morning', 'noon', 'evening', 9.9, 3, 11.5\].
5. Write a function `is_waldo_here` that accepts a list of suspects. If 'waldo' is in the list then **return** "We can find Waldo, go search!". Otherwise return, "Maybe we'll find him... tomorrow!"
