# More Practice with Functions and If Statements

## Functions
So we're going practice functions until we dream them at night. Functions are
blocks of code which contains a specific set of instructions when called. What
do you mean "when called"? Well after we create a function we have to explicitly
use the function so that the code will run. 

```python
print('Hey, I\'m the Pink Power Ranger') # We call the print function
```

In the above example we call the print function. A function is called by using
it's name and providing any arguments i.e. inputs, in this case the greeting
being printed. After we create our functions, we'll have to call them in the 
same way we call the print function

### Motivation
The king of all things prideful and vain implemented a new law: every string 
that's displayed in a program must be preceded by "For the glory of the King"
and succeeded by "He is mighty!". Let's see how it looks like

```python
# This is now illegal
print('JAXA is to Japan what NASA is to the USA') # Don't get locked up!

# This is exactly what we need to do
print('For the glrory of the King')
print('JAXA is to Japan what NASA is to the USA')
print('He is mighty!')
```
Now that the mad king has spoken, every single print statement must have those
lines as well, what a loser. We could type it every single time we print... but
that's so much effort. Even copying and pasting will get tedious over time. 
Luckily with functions there's an easier way to avoid to jail. 

```python
# Let's first define the function
def king_print(message):
    print('For the glory of the King')
    print(message)
    print('He is mighty!')

# Now we can call it, just like what we do with print!
king_print('JAXA is to Japan what NASA is to the USA')
```

When you call the function you should see the following output

```
For the glrory of the King
JAXA is to Japan what NASA is to the USA
He is mighty!
```

Functions allow for high levels of code reusability. Any time we need to print
the extra lines, we simply have to call the function. We are writing better code
by repeating ourselves less. If you ever find yourself writing code that does 
the same thing in different parts of the program, you should make it a function.

Let's say the mad king wants to change the last line from "He is mighty!" to "He
is supreme!!!". We still want to avoid prison for a bad print statement, so we
need to change all our prints now! Luckily, since we have a function, we only
need to change the function definition. If we didn't have a function, we'd have
to change every single that prints "He is mighty!". Imagine if we printed that 
1000 times, yikes.

Let's look at another way to write the king_print function
```python
# Let's first define the function
def king_print2(message):
    print('For the glrory of the King\n' + message + '\nHe is mighty!')

# Let's call it again
king_print2('JAXA is to Japan what NASA is to the USA')
```

You should get the same exact output as `king_print`
```
For the glrory of the King
JAXA is to Japan what NASA is to the USA
He is mighty!
```

If we decided to share our function with other poor citizens, they won't really
care how we implement it (I mean sometimes they do, but most time they won't). 
All they need to know is the function name and what inputs to give it, in this 
case the string to be printed. This is abstraction, we're saving coders from 
the details of how it works. Think about it, do you know how the `print`
function works? You can learn how it does, but for your programs you don't need
to. 

### Anatomy of a Function
You probably noticed from the earlier examples how we create functions. Let's
look at the king_print function once more:

```python
def king_print(message):
    print('For the glrory of the King')
    print(message)
    print('He is mighty!')
```

We first write def to tell python that we're **def**ining a function. We then
write the function name, which is the same as naming a variable. We following
with brackets and the arguments inside them. Arguments are inputs to your 
function. We then write a colon, colons tell Python that there's a block of code
coming right after. All the code of the function is indented.

Let's see some more examples:

```python
# Functions do not always need arguments, just put nothing in the brackets
def say_hi():
    print('Hi!')

say_hi() # You call them with nothing in the brackets as well

# Argument names follow the same rule as variable names.
def greet(name):
    print('Hi ' + name)

greet('bob') # Hi bob

# You can have more than one argument
def greet_2_people(name1, name2):
    greet(name1)
    greet(name2)

# Notice arguments are separated by a comma and have different names
# You can also use a function you defined within a function, why not right?

# Ensure that each argument name is unique to the function
# def greet_4_people(name, name name name) is wrong...
def greet_4_people(name, name1, name2, name3):
    greet_2_people(name, name1)
    greet_2_people(name2, name3)

# Doesn't matter if 'name' is an argument in the first greet function, two
# different functions can have the same argument name
```

### Returning Values
Well the functions we wrote previously print things to the screen but they don't
return a value. Huh? Let's seee

```python
# Adds 5 to a number but doesn't return it
def add_5_no_return(n):
    print(n + 5)

add_5_no_return(10) # Shows 15, so it works right?

def add_5_return(n):
    return n + 5

add_5_return(10) # Shows 15
```

So... what's the issue? Well we get a number and we add 5 to it. It'd be nice
if we can use it with other calculators as well:

```python
10 * add_5_return(8) # 130
10 * add_5_no_return(8) # Error!
```

The no return one fails. Why? Well like computers, functions get input -> 
processes the input -> returns the output. With the functions we created that 
used only print statements, Python returned nothing. Or more correctly, it 
returned `None`. Python does it for you automatically if you don't explicitly
return a value. 

Knowing that Python reutrns None automatically, these two functions do the same
thing:

```python
def favourite_number(n):
    print(n*10)

def favourite_number2(n):
    print(n*10)
    return
```

If you don't need to return a value, don't use the word. The `return` keyword
also stops the execution of a program.

```python
def my_multiply(x, y):
    print('We multiply the first number by 10')
    return x * 10 * y
    print('This never prints')

my_multiply(7, 5)
```

### Exercises 1
1. Create a function *rect_perimeter* that takes two arguments, length & width
    and returns the perimeter
2. Create a function *rect_area* that takes two arguments, length & width and
    returns the area.
3. Create a function *super_hi* that takes a name as an argument and **returns**
    'hi' plus the name in all capital letters For e.g. super_hi('Marcus') 
    returns 'HI MARCUS'. Use the function upper() on a string, 'test'.upper().


## If Statements
Python uses if-statements to decide whether a block of code should be run or
not. To determine if code needs to be run, we check if a condition is true.

### Booleans 
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

### Exercises 2
Work out the following boolean expressions
1. not False
2. True and (not False)
3. not (not True)
4. not (False or True)
5. False and not (True or (False or not False))
6. True and True and True
7. True and not (True or not (False and True))

### Conditions
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

### Exercises 3
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

### Elif and Else Statements
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

### Exercises 4
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