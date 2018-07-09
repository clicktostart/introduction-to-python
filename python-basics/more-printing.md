# More Printing

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
