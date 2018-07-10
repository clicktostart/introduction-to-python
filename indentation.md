# Indentation

We observed that in Python we have to indent the code when creating functions. We'll have to indent the code every time we create a new block of it. Indentation is **extremely important** in Python, your code will not work if the indentation isn't done correctly. There are some rules we have to adhere to:

* Indents can be between 1 and 8 spaces
    * We'll use four spaces as it's common convention
* Indents can be either space characters or tabs
    * We'll use spaces as it's common convention
* Do not mix and match indent styles - either use spaces or tabs throughout

```python
# Try to run the code below, what error do you get?
total_bananas = 4
price = 2
  bill = total_bananas * price
print('Your bill is {}'.format(bill))
```

You can indent your code as long as it's defined within a code block (or go with 0 indentation as we begin). We've seen code blocks created via functions, and we'll see more as we learn more about if statements and loops.
