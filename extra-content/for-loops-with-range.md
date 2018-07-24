# For Loops with Range

If you have some experience with other programming languages, you may be accustomed to for-loops with a variable that's the iteration number. Python can do that as well:

```python
# We can use the range function
for i in range(0, 6):
    print(i) # Prints 0,1,2,3,4,5

# The range function's first argument is the starting point
# Its second argument is ONE MORE than the end point
# Let's count from 4 till 21
for i in range(4, 22):
    print(i)

# There's a third parameter that allows us to skip, or rather step,
# through the range:
# Let's get even numbers from 0 to 10 inclusive
for i in range(0, 11, 2):
    print(i)

# With step we can go in descending order as well
for i in range(10, -1, -1):
    print(i)

# Why does the above work? Starting point is 10, end point is one more
# than -1 => 0, and we're stepping with one less each time

# Let's have a list with Nintendo Characters
my_childhood = ['mario', 'luigi', 'peach', 'yoshi', 'zelda', 'link', 'samus', 'kirby', 'falcon']

# We only want to print characters whose index is even, let's use the range function
for i in range(0, len(my_childhood)):
    if i % 2 == 0:
        print(my_childhood[i])
        # mario, peach, zelda, samus, falcon

# In summary: range(start, end + 1, step - defaults to 1)
```

## Exercises

1. Use the range function to create for loop that prints the numbers 35 to 210 in increments of 3
