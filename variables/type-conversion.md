# Type Conversion

We might get data in one format and want to do an operation with it in another format. Python allows us to convert from type to another. Create a file `py_types.py` and following along with the code below:

```python
a = 4
b = '21'
c = 'que pasa?'

# Try to run this, it fails
# a + b
# You should get the following error:
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# It does make sense, how can you add an integer to a number?

# Let's try something else:
print(a + int(b))

# We use int(b) to convert b from a string to an integer, that way we can add it
# like we do with every other number

# Let's try to convert c to an integer, it will fail
# print(int(c))
# ValueError: invalid literal for int() with base 10: 'que pasa?'

# For a string to be converted to a number, the entire string must be a number

# We can convert integers to strings
print(str(a))
print(str(a) + b) # Will be '421', string concatenation remember?

# Strings can also be converted to floats:
gpa = "3.8"
perfect_gpa = float(gpa) + 0.2
print(perfect_gpa)
```
