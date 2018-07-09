# Strings

Without knowing it, we've been printing strings in the Python shell. A string is simply a sequence of characters. Characters are letters, numbers, punctuation marks and spaces like the newline character we just saw. The important features about these character sequences are that they are wrapped around quotation marks. We've previously used single quotes thus far. Strings can also be represented by double quotes. For example, let's revisit the hello world using double quotes this time:

```python
print("Hello World")
```

The exact same thing happens. Do it for the other examples to get more practice and sate your curiosity. Practice and curiousity are important to becoming a good programmer! Let's try the following, we'll begin with a single quote and ending with a double quote:

```python
print('Hello World")
```

We should get the following error

```text
    >>> print('Hello World")
    File "<stdin>", line 1
        print('Hello World")
                       ^
SyntaxError: EOL while scanning string literal
```

Congrats, you got your first error! Errors are good things for learning, it helps us find out what's wrong with our program. We'll encounter quite a lot of these as we go on, it's all part of the process so don't be alarmed when they come up. What this error tells us is that the code we wrote isn't valid Python code - the syntax is off. That's because if we start a string with a single quote we must end it with a single quote. The same is true for double quotes. So, while these are valid:

```python
print('Domo arigato Mr Roboto')
print("Domo arigato Mr Roboto")
```

These are not:

```python
print('Domo arigato Mr Roboto")
print("Domo arigato Mr Roboto')
```

> Note on choosing which quotes to use for strings
>
> When it comes to strings, decide whether you're using single quotes or double quotes and stick with it. Be consistent, good code is readable and having conventions help achieve that. Throughout this course we will use single quotes, feel free to switch it up if you prefer double quotes. Just be consistent.
