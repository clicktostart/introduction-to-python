# Variables

Variables are names for stored values in a program. They can store a variety of data. Create a new file `my_variables.py` and type the following:

```python
# Variables can be strings i.e. text values
my_name = 'Rico Suave'
# Variables can be numbers, like integers (ints) - numbers without a decimal point
total_cars_owned = 10
# There are also floating numbers as well - they have decimal points
university_gpa = 3.8
# Somethings we just need to know if something is True or False
can_dance = True
# We can display variable values with the print function by using a placeholder and substituting them
print('Hola, me llamo %s' % my_name)
print('I have a total of %s cars' % total_cars_owned)
```

Can you print your GPA in a sentence as well? Some things to note:

* You don't need underscores in your variable names. It is standard practice in Python to separate words in variable names with them. You should maintain this standard.
* You can change the value of the variable at any time, that's why we call them variables after all. You can even change a variable from one type to another! For example, `university_gpa` can be set to "3.8" afterwards. This is generally discouraged as consistency is valuable in programming and the usual operators may not work with the variable's new type.
* You can always write `my_name='Rico Suave'`, but that's just not as readable as `my_name = 'Rico Suave'`. Be nice to yourself and to other programmers who may read your code, uses spaces.

## Variables and Operators

Variables won't be fun if we couldn't do anything with them. Let's work out how much money we make after being taxed. In a new file, `operations.py`, create a variable called `base_salary`. Assign 8000 to `base_salary`. Now create another variable called `tax` and set it to 0.15. Now that we have those two variables, let's find out how much money we actually get to keep, create one more variable:

```python
income_after_tax = base_salary * (1 - tax)
print(income_after_tax)
```

Congratulations! You've been the employee of the month, and the company wants to reward you with a bonus. The bonus policy states that you get twice your income after tax. Create a variable `monthly_earnings` with this value. Because you worked overtime, you're also going to get $200 extra. You can do that like this:

```python
monthly_earnings = monthly_earnings + 200
print(monthly_earnings)
```

You should have received 13800.0. Now let's try the same with strings. Create a variable called `hello` and set it to 'Hello'. Also create a variable called `world` and assign 'World' to it. Then write the follow:

```python
print(hello + ' ' + world)
```

This is called **string concatenation**, simply joining strings together. What happens if we type `hello - world` instead?

```text
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'str'
```

The last line tells us the problem: the minus operator does not support having two strings as its arguments. Operators are available to variables depending on their types. We see that in Python the plus operator is defined for numbers and for strings but behave differently. Keep this in mind as you code, and read errors as they come up!

## Type Conversion

We might get data in one format and want to do an operation with it in another format. Python allows us to convert from type to another to allow this. Let's see

```python
a = 4
b = '21'
c = 'que pasa?'

# Try to run this, it fails
# a + b
# You should get the following error:
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Let's try something else:
print(a + int(b))

# We use int(b) to convert b from a string to an integer, that way we can add it
# like we do with every other number

# Let's try to convert c to an integer, it will fail
# print(int(c))
# ValueError: invalid literal for int() with base 10: 'que pasa?'

# For a string to be converted to a number, the entire string must be a number

# We can convert integers to strings
print(str(a) + b) # Will be '421', string concatenation remember?

# Strings can also be converted to floats:
gpa = "3.8"
perfect_gpa = float(3.8) + 0.2
print(perfect_gpa)
```

## Exercises

1. Create 3 variables for a triangle: `side1`, `side2` and `side3`. Assign them values of 3, 4 and 5 respectively. What is the perimeter of this triangle? This triangle is right triangle, with `side1` and `side2` and as the base and height, can you create a variable and store its area?
