# Logical Operators

Given what we know so far, we know the result of comparing two numbers or string lengths - it's either True or False. We know that Boolean values and Boolean expressions \(code that needs to be evaluated to True or False\) can use logical operations or/and/not. For other data types we can get Boolean expressions with comparative operators.

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

## Exercises

1. Work out whether the following would be True or False:
   1.  10 &lt; 17 or \(not False and 7 == 7.0\)
   2.  'Justin' == "Justin" 3.
   3. not \(10 == 1 or 1000 == 1000\)
   4. "bunji" == "bunji" or "machel" == "soca king"
   5.   ```python
       energy_level = 3

       low_energy = energy_level < 5

       likes_coffee = True

       low_energy and likes_coffee
      ```



