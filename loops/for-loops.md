# For Loops

A for-loop allows us to repeat code for a finite amount of time. In Python, we can use the for-loop to **iterate** over a list. The for-loop will go through each element of the list one by one, starting with the first and ending with the last.

```python
blue_foods = ['dasheen', 'yam', 'cassava', 'sweet potato']

# The 'in' keyword is used a again
# Read this as "for NEW_TEMPORARY_VARIABLE in LIST_OF_ITEMS"
for blue_food in blue_foods:
    print(blue_food)
    # On the console you'll see
    # dasheen
    # yam
    # cassava
    # sweet potato


# Function that prints a list of numbers after adding 2 to them
def add_two(numbers):
    for n in numbers:
        print(n + 2)

add_two([1,2,3,4,10]) # 3,4,5,6,12


# Let's do a function that prints out the values of a list of lists
# In this case, we'll nest the for loops to print them out
def print_double_list(double_list):
    for dl in double_list:
        for dl_item in dl:
            print(dl_item)

print_double_list([[1,2],['bob',10,34.0],['c']])


# While Python already has a built in sum function, we can do one too!
def my_sum_1(items):
    total = 0
    for item in items:
        total += item
    return total

my_sum_1([1,2,4,5]) # 12
```

## Better coding with errors

A good coder knows how to deal with errors. Let's take some bad input for the my\_sum\_1 function in the previous section:

```python
my_sum_1([1,2,'bob',5])
```

You'd get something like this:

```text
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in my_sum_1
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
```

So we can see that Python is complaining that you're trying to add a string with an int. It's not the best error message, if we expect the list to have only numbers why would there be a string? In this case we knew what was in the list, what if we didn't?

Let's write a better sum function that checks to see if the item being added is a number. If it's not, raise an error to let the user know what's in the list.

```python
# First let's import this very useful numbers package
# Particularly the number class
from numbers import Number

def my_sum_2(items):
    total = 0
    for item in items:
        # We check if the list item is a number
        # isinstance is a function we can use to compare types
        # in this case it would be True for 0, 3, 4.4 etc but false for 'me'
        # and other strings
        if isinstance(item, Number):
            total += item
        else:
            # In the same way we return values, we raise Errors
            # This is a different kind of error we've never seen but is a lot
            # more useful. As the name suggests, we have a problem with a value
            raise ValueError('List item %s is not a number' % item)
    return total

my_sum_2([1,2,'bob',5]) # Much better
```

Now the error message is a lot clearer:

```text
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in my_sum_2
ValueError: List item bob is not a number
```

## Exercises

1. For-loops are best suited to finite objects - true or false?
2. Write a function `product` that uses a for-loop to multiply every item in a

   list passed as an argument.

   1. What happens if the empty list is given? Modify the function such that

      if an empty list is given, 1 is returned

   2. What happens if the list has data that aren't numbers? Raise an error

      if a non-number is detected.

3. Write a function `my_max` which determines the highest number found in a

   list. Let's break it down, you will be constantly comparing the current number

   to last recorded highest number. Think about, the highest number can appear

   anywhere in the list, right? So what do you compare the first number to? When

   you create a max\_num variable, first set it to -100000000000.

