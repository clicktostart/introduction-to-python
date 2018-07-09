# Basics

## More Printing

Well, with the same Python shell we used in the last section, let's print some
more things.

```python
print('Roses are red')
print('Violets are blue')
print('Sugar is sweet')
print('And so are you')
```

As Python processes code line by line, the output comes out line by line. Think you can put them all together and get one big output? Of course you can! Let's try:

```python
print('Roses are red Violets are blue Sugar is sweet And so are you')
```

Well that's not exactly what we expected, we got this for output

    Roses are red Violets are blue Sugar is sweet And so are you

Let's format it so that it'll print out more like how we expect poems to be written.

```python
print('Roses are red\nViolets are blue\nSugar is sweet\nAnd so are you')
```

The output should be like this:

    Roses are red
    Violets are blue
    Doubles with heavy pepper
    Will never be sweet for you

You would have noticed that instead of a space we use `\n`. That's a newline character, it's used in strings to output to, unsuprisinly, a new line.

## Strings

Without knowing it, we've been printing strings in the Python shell. A string is simply a sequence of characters. Characters are letters, numbers, punctuation marks and spaces like the newline character we just saw. The important features about these character sequences are that they are wrapped around quotation marks. We've previously used single quotes thus far. Strings can also be represented by double quotes. For example, let's revisit the hello world using double quotes this time:

```python
print("Hello World")
```

The exact same thing happens. Do it for the other examples to get more practice and sate your curiosity. Practice and curiousity are important to becoming a good programmer! Let's try the following, we'll begin with a single quote and ending with a double quote:

```python
print('Hello World")
```

We should get the following error

        >>> print('Hello World")
        File "<stdin>", line 1
        print('Hello World")
                    ^
    SyntaxError: EOL while scanning string literal

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

## Numbers

In the Python shell, enter `2`. It returns `2`, right? Nothing special there, we get back the number we entered. Now enter `2 + 4`. Nice, Python worked out that the number was `6`. Let's try some more additions and subtractions, enter the following and observe Python's output

* `4 + 4 + 4`
* `100 - 50`
* `-25`
* `-22 + 32`
* `-10 - 5`

Those simple exercises highlights a few capabilities for us. We can add more than two numbers at a time. We can do subtraction. We can have negative numbers. We can add and subtract with negative numbers like we do with positive ones. Let's do some multiplication now

* `4 * 4`
* `42 * 0`
* `-10 * 5`
* `3 * 2 - 4`
* `3 * (2 - 4)`

Like before, we can multiply by positive and negative numbers, as well as 0. Pay attention to the last two in particular. If you recall, in secondary school mathematics we learn BODMAS or BOMDAS - Brackets of Division/Multiplication Addition and Subtraction. They indicate the order by which things are calculated. In the first case of `3 * 2 - 4`, the multiplication happens first and then we perform the subtraction. In the second case of `3 * (2 - 4)`, Python works out the expression in the brackets before multiplying. Be mindful of your maths and brackets, as you see they return very different results. Now let's do division:

* `10 / 2`
* `22 / 7`
* `-3 / 2`
* `-2 / 3`
* `10 / (20 * 2 - 5)`

In the first example had 10 and 2, and the shell returned `5.0`. This is deliberate, if Python didn't return a decimal value we could potentially lose the true value, as we see in the second example when the division has a remainder. As before, doesn't matter if a number is positive or negative.The last example also showed that we can mix and match to get results. Let's try to break things and divide by 0:

    >>> 5 / 0
    Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
    ZeroDivisionError: division by zero

We got another error! Division by 0 isn't possible, so Python raises an error to stop it from ever happening. Imagine a computer trying to work out how to divide a number by 0, it'll take forever trying to figure it out or return an erroneous result that could affect further processing. Programmers write code for all kinds of situations, sometimes the code is critical to human safety like software that helps airplane navigation. If we don't watch for errors the results can be truly disastrous.

### Integers and Floats

Numbers in Python can be classified by two categories: integers and floats. Integers are whole numbers, like `3` or `210`. Floats are decimal values, like `15.2` or `0.456`. In Python, the values `5` and `5.0` are equal but their types are not. The first is a float type and the second is float type. While it seems trivial, different types can perform different operations and we may have problems that require a particular type of number.

### Integer Division

We noticed that `10 / 2` returns `5.0`. By default, Python returns floats for divisions even if the results will be a whole number. What if we wanted an integer for the answer instead of a float? Well, we use integer division. Enter the following in your shell:

```python
10 // 2
5 // 3
```

The answer should be `5` and `1` respectively. Integer division removes any value after the decimal point, the remainder of the division is always ignored.

## Exercises

Create a new file called `basics.py`. Write code in it to do the following:

1. Print your favourite video game on the console.
2. Print your favourite animal as well.
3. Use the `print` function once to output the two previous strings separated by a newline.
4. Print the following expressions in Python
    1. 61 + 4
    2. 25 - 12.5
    3. $$25 \div 2$$
    4. $$5 \times 5$$
    5. $$6 \times 2 + 5$$
    6. $$6 \times (2 + 5)$$
    7. $$10 \div (4 \times (5 \div 2))$$
