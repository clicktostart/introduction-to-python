# If Statements

Before our code we wrote would only run sequentially, one line after the other. With if statements, our programs can 'branch', executing certain bits of code only when certain conditions are met.

```python
# Let's set up a variable with the amount of money we got
money_in_pocket = 100.75

# This code will not run, because money_in_pocket is not greater than 100000
if money_in_pocket > 100000:
    print('Congratulations, you can buy an Armani handkerchief')

if money_in_pocket <= 200:
    print('You could use a helping hand, he\'s another $100')
    money_in_pocket = money_in_pocket + 100
```

You begin the if statement by first typing `if`, then you write the conditional expresion, and finally you put a colon just like you did for functions. After a colon we indent to show Python where this block of code belongs to. Let's see another example, we'll write a function `is_even` that returns true or false if the argument is an even number.

```python
def is_even(num):
    if num % 2 == 0:
        print('The number is even')
        return True

    # If the number was even, the function would return True
    # That means that if this code would not run once the if statement's code
    # goes through (remember, return stops execution)
    # So this code will only run if the number was odd
    print('The number is odd')
    return False

is_even(6)
# The number is even
# True

is_even(19)
# The number is odd
# False
```

Because that function returns either True or False, we can treat it like another Boolean value and use it in expressions. Let's consider checking if it's odd:

```python
def is_odd(num):
    return not is_even(num)

is_odd(22)
# The number is even
# False

is_odd(103)
# The number is odd
# True
```

Let's write a function to determine if someone needs to get a valid National ID card:

```python
# Functions takes the person's age and returns either True or False
def needs_id(age):
    if age >= 16:
        print('You need to get an ID card')
        return True

    print('You do not need an ID card as yet')
    return False

needs_id(12)
# You do not need an ID card as yet
# False

needs_id(25)
# You need to get an ID card
# True
```

An if statement would not be necessary for this function if it didn't need to print to the screen

```python
def needs_id_simple(age):
    return age >= 16

needs_id_simple(67) # True
needs_id_simple(3) # False
```

