# Numbers

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

```text
>>> 5 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

We got another error! Division by 0 isn't possible, so Python raises an error to stop it from ever happening. Imagine a computer trying to work out how to divide a number by 0, it'll take forever trying to figure it out or return an erroneous result that could affect further processing. Programmers write code for all kinds of situations, sometimes the code is critical to human safety like software that helps airplane navigation. If we don't watch for errors the results can be truly disastrous.

## Integers and Floats

Numbers in Python can be classified by two categories: integers and floats. Integers are whole numbers, like `3` or `210`. Floats are decimal values, like `15.2` or `0.456`. In Python, the values `5` and `5.0` are equal but their types are not. The first is a float type and the second is float type. While it seems trivial, different types can perform different operations and we may have problems that require a particular type of number.

## Integer Division

We noticed that `10 / 2` returns `5.0`. By default, Python returns floats for divisions even if the results will be a whole number. What if we wanted an integer for the answer instead of a float? Well, we use integer division. Enter the following in your shell:

```python
10 // 2
5 // 3
```

The answer should be `5` and `1` respectively. Integer division removes any value after the decimal point, the remainder of the division is always ignored.
