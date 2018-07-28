# Booleans

Python can work out if an expresion is true or false e.g. is 10 greater than 5? When we work out those conditional expresses, Python gets a Boolean value: either the expression is `True` or the expression is `False`. **You have to write to True and False exactly like that!** TRUE or true or tRue won't cut it. Let's see them in action:

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

We know variables can store numbers and string, they can also store Booleans as well. A variable can store any data type. And like numbers and strings, you can use operators on them. In this case you can use: or, and, not.

```python
it_is_raining = True
it_is_hot = False

it_is_raining and it_is_hot         # False
it_is_raining or it_is_hot          # True
it_is_raining and (not it_is_hot)   # True
```

## Exercises

Work out the following boolean expressions

1. not False
2. True and \(not False\)
3. not \(not True\)
4. not \(False or True\)
5. False and not \(True or \(False or not False\)\)
6. True and True and True
7. True and not \(True or not \(False and True\)\)
