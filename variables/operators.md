# Operators

Let's work out how much money we make after being taxed. In a new file, `tax.py`, create a variable called `base_salary`. Assign `8000` to `base_salary`. Now create another variable called `tax` and set it to `0.15`. Now that we have those two variables, let's find out how much money we actually get to keep, create one more variable as follows:

```python
income_after_tax = base_salary * (1 - tax)
print(income_after_tax)
```

Congratulations! You've been the employee of the month, and the company wants to reward you with a bonus. The bonus policy states that you get twice your income after tax. Create a variable `monthly_earnings` with this value. Because you worked overtime, you're also going to get $200 extra. We can do that like this:

```python
monthly_earnings = monthly_earnings + 200
print(monthly_earnings)
```

You should have received `13800.0`.

Now let's try the same with strings. Create a variable called `hello` and set it to `'Hello'`. Also create a variable called `world` and assign `'World'` to it. Then write the follow:

```python
print(hello + ' ' + world)
```

This is called **string concatenation**, simply joining strings together. What happens if we type `hello - world` instead?

```text
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'str'
```

The last line tells us the problem: the minus operator does not support having two strings as its arguments. Operators are available to variables depending on their types. We see that in Python the plus operator is defined for numbers and for strings but behave differently. Keep this in mind as you code, and keep reading errors as they come up.
