# Functions

So we're going practice functions until we dream them at night. Functions are blocks of code which contains a specific set of instructions when called. What do you mean "when called"? Well after we create a function we have to explicitly use the function so that the code will run.

```python
print('Hey, I\'m the Pink Power Ranger') # We call the print function
```

In the above example we call the print function. A function is called by using it's name and providing any arguments i.e. inputs, in this case the greeting being printed. After we create our functions, we'll have to call them in the same way we call the print function.

## First Functions

Create a file called `my_functions.py` and take a look at the code below:

```python
def add_five(number):
    return number + 5

what_is_this_number = add_five(10) # It's a hard question but I guess 15...
print(what_is_this_number)
```

We're actually doing two things here: defining the `add_5` function and then calling it. We define the `add_five` function by first typing **def**, then the function name "add_five", we then have brackets which contain *parameters* and finally on that line a colon. The code of the function simply consists of the `return` keyword and a maths expresision that adds 5 to `number`.

That's a lot to take in, but it's simple. The parameters are simply inputs for the function. The colon says it's a new block of code i.e. all the code that's indented belongs to the function. The `return` keyword simply says what the function outputs. Let's see some other functions:

```python
# This function takes a string called 'message' and returns a new string
# that adds the word adios to the message
def say_goodbye(message):
    return message + ' ¡Adios!'

print(say_goodbye('Hi my name is Paul!'))

# Functions you defined can call other functions as well
def add_ten(number):
    with_five_more = add_five(number)
    return add_five(with_five_more)

print(add_ten(10)) # You'll get 20

# We can use the output of one function as input for another
def add_ten_version2(number):
    return add_five(add_five(number))

print(add_ten_version2(10)) # You'll get 20
```

So far our functions have been pretty much the same format: def keyword, function name, a parameter in brackets, some code that returns a value at the end. We got some flexibility, especially with the parameters and return values:

```python
# Yep, you can have multiple parameters
def my_multiply(x, y):
    return x * y

print(my_multiply(7, 5)) # 35

# Sometimes you don't need parameters
def greetings():
    return '¡Hola!'

print(greetings()) # You must still use the brackets even without parameters!

# Some functions may not return values
def haiku():
    print('Do I want to fight? Chuck Norris roundhouse kicked me! I will fight no more...')

haiku() # Because this function prints we don't call the print statement again
```

There's something to note about the `return` statement, it ends the execution of the function. So every line of code that comes after it is never run. Try this quick example:

```python
def maths_for_fun(num1, num2, num3):
    mult_nums = num1 * num3
    div_nums = num2 / num1
    return mult_nums - div_nums
    # This code with never run
    add_nums = num2 + num3
    return add_nums

print(maths_for_fun(5,25,6)) # 25 instead of 31
```

## Exercises

1. Create a function `rect_perimeter` that takes two arguments, `length` & `width` and returns the perimeter
2. Create a function `rect_area` that takes two arguments, `length` & `width` and returns the area.
3. Create a function `super_hi` that takes a name as an argument and **returns** 'hi' plus the name in all capital letters For e.g. `super_hi('Marcus')` returns 'HI MARCUS'. Use the function `upper()` on a string,  e.g. `'test'.upper()`.
