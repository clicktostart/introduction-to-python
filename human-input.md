# Human Input

There will be programs we write that would need human input to function properly. As much as we'd like to think we know everything, we should leave it up to the user as well.

This is quite simple in Python. Let's say we'd like find out the user's name:

```python
name = input('Hello, what is your name?\n')
print('Hi %s! Nice to meet you, hope you like Python!' % name)
```

It's as simple as that! Note the following:

* User input is saved as a string. If you want to you to change its type you'll

  have convert it.

* You don't need to have a question asked to received user input, you can just

  call `input()` and the user could still enter data.

* Python does not put any kind of space when displaying input prompts, which is

  why we added the newline character ourselves.

## Exercises

1. Create a variable called `age` and prompt the user for theirs. Convert that

   age into an integer \(recall you can assign a variable a new value with its

   current one\). Multiply that age by 3 and print the result.

2. Create a python script called `rectangle_perimeter.py`, it asks the user for

   the rectangle's length and width and print the perimeter.

