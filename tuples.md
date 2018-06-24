# Tuples

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

## Exercises

1. t1 = ('w', 'a', 'l', 'l', 'e', 4, 0, 4)
Slice the tuple so that it only contains ('w', 'a', 'l', 'l', 'e').
2. Write a function funky_points_sum which takes tuples t1 and t2 as arguments
and adds the 2nd item of t1 to the 1st item of t2, then multiplies that result
by the 2nd item of t2 minus the first item of t1.
