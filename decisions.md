# Decisions

Python uses if-statements to decide whether a block of code should be run or
not. To determine if code needs to be run, we check if a condition is true.

## Booleans

Python can work out if an expresion is true or false e.g. is 10 greater than 5?
When we work out those conditional expresses, Python gets a Boolean value:
either the expression is `True` or the expression is `False`. **You have to
write to True and False exactly like that!** TRUE or true or tRue won't cut it.
Let's see them in action:

```python
# Type these in your Python interpeter and you'll get them back
True
False

# We can get their inverses with the not operator
not True
not False

# We can use the 'or' operator, which returns True if any one of the values
# are True
True or False   # True
True or True    # True
False or True   # True
False or False  # False

# We can also use the 'and' operator, which returns True only if both values
# are True
True and False  # False
True and True   # True
False and True  # False
False and False # False

# We can chain them with the 'not' operator as well
not (True and False)  # True
not (True and True)   # False
not (False and True)  # True
not (False and False) # True
```

We know variables can store numbers and string, they can also store Booleans as
well. A variable can store any data type. And like numbers and strings, you can
use operators on them. In this case you can use: or, and, not.

```python
it_is_raining = True
it_is_hot = False

it_is_raining and it_is_hot         # False
it_is_raining or it_is_hot          # True
it_is_raining and (not it_is_hot)   # True
```

## Exercises 1

Work out the following boolean expressions
1. not False
2. True and (not False)
3. not (not True)
4. not (False or True)
5. False and not (True or (False or not False))
6. True and True and True
7. True and not (True or not (False and True))

## Conditions

Given what we know so far, we know the result of comparing two numbers or string
lengths - it's either True or False. We know that Boolean values and Boolean
expressions (code that needs to be evaluated to True or False) can use logical
operations or/and/not. For other data types we can get Boolean expressions with
comparative operators.

```python
# All the following code evaluates to True
1 == 1                          # Equal to
'Chloe' == 'Chloe'              # Works for strings as well
2.001 != 2                      # Not equal to
'Chloe' != 'chloe'              # Case matters, these aren't equal strings
1 > 0                           # Greater than
3 < 5                           # Less than
15 >= 15                        # Greater than or equal to
# The above is equivalent to (15 > 15 or 15 == 15 )
amount_of_apples = 50
a <= 1400                       # Less than or equal to
```

## Exercises 2

Work out whether the following would be True or False
1. 10 < 17 or (not False and 7 == 7.0)
2. 'Justin' == "Justin"
3.  energy_level = 3

    low_energy = energy_level < 5

    likes_coffee = True

    low_energy and likes_coffee
4. not (10 == 1 or 1000 == 1000)
5. "bunji" == "bunji" or "machel" == "soca king"

## If Statements

So we got True and False values, and ways to figure out if expressions in Python
are one of those Boolean values. Now all we need to do is tell Python to run
some code if and only if a condition is true. Luckily it's nearly just like
English:

```python
# Let's set up a variable with the amount of money we got
money_in_pocket = 100.75

if money_in_pocket > 100000:
    print('Congratulations, you can buy an Armani handkerchief')
```

It's that simple! You beigin the if statement by first typing `if`, then you
write the conditional expresion, and finally you put a colon just like you did
for functions. After a colon we indent to show Python where this block of code
belongs to. Let's see another example, we'll write a function is_even that
returns true or false if the number is even.

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

Because that function returns either True or False, we can treat it like another
Boolean value and use it in expressions. Let's consider checking if it's odd:

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

Let's write a function to determine if someone needs to get a valid National ID
card:

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

An if statement would not be necessary for this function if it didn't need to
print to the screen

```python
def needs_id_simple(age):
    return age >= 16

needs_id_simple(67) # True
needs_id_simple(3) # False
```

## Elif and Else Statements

There are times where we need to check a variety of values to determine what
should be done. Think about getting a grade for your mark. School's usually have
many possible grades your mark can fall into: A, B, C etc. Let's a write a
function that returns a grade.

```python
def get_grade(mark):
    # This part is normal
    if mark >= 90:
        result = 'A'
    # Now we want to see if someone got a B
    elif mark < 90 and mark >= 80:
        result = 'B'
    elif mark < 80 and mark >= 70:
        result = 'C'
    # If all other conditions are false, do this code
    else:
        result = 'F' # Pretty harsh from the school if you ask me
    return result

get_grade(100)  # 'A'
get_grade(85)   # 'B'
get_grade(35)   # 'F'
```

**After** the first if statement, we can have more options to check. We use
elif ("else if") statements to do additional comparisons and run different code.
At the end, and only at the end, we used an else statement. This executes as
long as no previous condition in the if statement was true. Not too bad right?
But wait... why can't we just write multiple if statements?

```python
def get_grade_inefficient(mark):
    if mark >= 90:
        result = 'A'

    if mark < 90 and mark >= 80:
        result = 'B'

    if mark < 80 and mark >= 70:
        result = 'C'

    if mark < 70:
        result = 'F'

    return result

get_grade_inefficient(100)  # 'A'
get_grade_inefficient(85)   # 'B'
get_grade_inefficient(35)   # 'F'
```

They retun the same results! But as the function name implies, this is really
inefficient. For one, no matter what grade the user gets, the function always
checks each if statement every single time it's run. In the first get_grade
function, no more checks needed to be done if the grade was an A for example.
In the second version, Python still checks if the grade is B or C even though
we already got the answer. That's just unnecessary. Also, we have to explicitly
state the last case for the F, in the first function we just `else` to state
what the default value is.

## Exercises 3

1. Write a function chosen_one which accepts a name. If the name is 'Neo' then
    print 'You are the chosen one' and return True. Otherwise let them know they
    aren't the chosen one and return false.
2. The Three Stooges were Moe, Larry and Shemp. Write a function we_miss_you
    that accepts a name. If the name is one of the Stooges then return
    "I'm gonna change my socks. What an experience!". Otherwise return "Don't"
    forget to watch their show on YouTube!"
3. Write a program that accepts 3 numbers from a user and determines if
    they form a triangle. Three numbers for a triangle if and only if the
    sum of two sides are greater than the third side. So for three sides
    a, b and c - a + b >= c, b + c >= a and c + a >= b
4. Create a guessing game where the computer generates a random number
    between 1 and 10. If the user gets the answer correct they are
    congratulated, if they get it wrong print "Hard lucks!".
    * Remember, to get a random integer first import the random module:
    `from random import randint` and specify the ranges for randint. E.g.
    `randint(3,8)` - choose a number between 3 and 8 inclusive.
5. Write a function happy_song that accepts mood as an argument. If the mood is
    happy then ask the user if they know it. If they're happy and know it, print
    "Clap your hands". If they're happy and don't know it then print "At least
    your're happy". If mood is sad then print "Laughter is the best medicine.".
    For any other mood print "Just keep swimming".
