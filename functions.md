# Functions

So we're going practice functions until we dream them at night. Functions are blocks of code which contains a specific set of instructions when called. What do you mean "when called"? Well after we create a function we have to explicitly use the function so that the code will run.

```python
print('Hey, I\'m the Pink Power Ranger') # We call the print function
```

In the above example we call the print function. A function is called by using it's name and providing any arguments i.e. inputs, in this case the greeting being printed. After we create our functions, we'll have to call them in the same way we call the print function

## Motivation

The king of all things prideful and vain implemented a new law: every string that's displayed in a program must be preceded by "For the glory of the King" and succeeded by "He is mighty!". Let's see how it looks like

```python
# This is now illegal
print('JAXA is to Japan what NASA is to the USA') # Don't get locked up!

# This is exactly what we need to do
print('For the glrory of the King')
print('JAXA is to Japan what NASA is to the USA')
print('He is mighty!')
```

Now that the mad king has spoken, every single print statement must have those lines as well, what a loser. We could type it every single time we print... but that's so much effort. Even copying and pasting will get tedious over time. Luckily with functions there's an easier way to avoid to jail.

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

```text
For the glrory of the King
JAXA is to Japan what NASA is to the USA
He is mighty!
```

Functions allow for high levels of code reusability. Any time we need to print the extra lines, we simply have to call the function. We are writing better code by repeating ourselves less. If you ever find yourself writing code that does the same thing in different parts of the program, you should make it a function.

Let's say the mad king wants to change the last line from "He is mighty!" to "He is supreme!!!". We still want to avoid prison for a bad print statement, so we need to change all our prints now! Luckily, since we have a function, we only need to change the function definition. If we didn't have a function, we'd have to change every single that prints "He is mighty!". Imagine if we printed that 1000 times, yikes.

Let's look at another way to write the `king_print` function

```python
# Let's first define the function
def king_print2(message):
    print('For the glrory of the King\n' + message + '\nHe is mighty!')

# Let's call it again
king_print2('JAXA is to Japan what NASA is to the USA')
```

You should get the same exact output as `king_print`

```text
For the glrory of the King
JAXA is to Japan what NASA is to the USA
He is mighty!
```

If we decided to share our function with other poor citizens, they won't really care how we implement it \(I mean sometimes they do, but most time they won't\). All they need to know is the function name and what inputs to give it, in this case the string to be printed. This is abstraction, we're saving coders from the details of how it works. Think about it, do you know how the `print` function works? You can learn how it does, but for your programs you don't need to.

## Anatomy of a Function

You probably noticed from the earlier examples how we create functions. Let's look at the `king_print` function once more:

```python
def king_print(message):
    print('For the glrory of the King')
    print(message)
    print('He is mighty!')
```

We first write def to tell python that we're **def**ining a function. We then write the function name, which is the same as naming a variable. We following with brackets and the arguments inside them. Arguments are inputs to your function. We then write a colon, colons tell Python that there's a block of code coming right after. All the code of the function is indented.

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

## Returning Values

Well the functions we wrote previously print things to the screen but they don't return a value. Huh? Let's seee

```python
# Adds 5 to a number but doesn't return it
def add_5_no_return(n):
    print(n + 5)

add_5_no_return(10) # Shows 15, so it works right?

def add_5_return(n):
    return n + 5

add_5_return(10) # Shows 15
```

So... what's the issue? Well we get a number and we add 5 to it. It'd be nice if we can use it with other calculators as well:

```python
10 * add_5_return(8) # 130
10 * add_5_no_return(8) # Error!
```

The no return one fails. Why? Well like computers, functions get input -&gt; processes the input -&gt; returns the output. With the functions we created that used only print statements, Python returned nothing. Or more correctly, it returned `None`. Python does it for you automatically if you don't explicitly return a value.

Knowing that Python reutrns None automatically, these two functions do the same thing:

```python
def favourite_number(n):
    print(n*10)

def favourite_number2(n):
    print(n*10)
    return
```

If you don't need to return a value, don't use the word. The `return` keyword also stops the execution of a program.

```python
def my_multiply(x, y):
    print('We multiply the first number by 10')
    return x * 10 * y
    print('This never prints')

my_multiply(7, 5)
```

## Exercises

1. Create a function `rect_perimeter` that takes two arguments, `length` & `width` and returns the perimeter
2. Create a function `rect_area` that takes two arguments, `length` & `width` and returns the area.
3. Create a function `super_hi` that takes a name as an argument and **returns** 'hi' plus the name in all capital letters For e.g. `super_hi('Marcus')` returns 'HI MARCUS'. Use the function `upper()` on a string,  e.g. `'test'.upper()`.
