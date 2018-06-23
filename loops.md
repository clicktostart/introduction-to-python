# Loops
With loops we'll finally have all the Pythonic ingredients to begin making
games. Loops allow us to repeat tasks over and over again. Think about how we
used if statements before to check user input:

```python
def is_valid_user(username):
    if username == 'shaka zulu':
        return True
    else:
        print('Invalid username')
        return False
```

Well if our entire program checked the input once, it would end with False if
I entered 'eric williams'. What if we wanted to give the user 3 times before
we stop them from trying? Loops can be useful then.

## For Loops
A for-loop allows us to repeat code for a finite amount of time. In Python, we
can use the for-loop to **iterate** over a list. The for-loop will go through
each element of the list one by one, starting with the first and ending with
the last.

```python
blue_foods = ['dasheen', 'yam', 'cassava', 'sweet potato']

# The 'in' keyword is used a again
# Read this as "for NEW_TEMPORARY_VARIABLE in LIST_OF_ITEMS"
for blue_food in blue_foods:
    print(blue_food)
    # On the console you'll see
    # dasheen
    # yam
    # cassava
    # sweet potato


# Function that prints a list of numbers after adding 2 to them
def add_two(numbers):
    for n in numbers:
        print(n + 2)

add_two([1,2,3,4,10]) # 3,4,5,6,12


# Let's do a function that prints out the values of a list of lists
# In this case, we'll nest the for loops to print them out
def print_double_list(double_list):
    for dl in double_list:
        for dl_item in dl:
            print(dl_item)

print_double_list([[1,2],['bob',10,34.0],['c']])


# While Python already has a built in sum function, we can do one too!
def my_sum_1(items):
    total = 0
    for item in items:
        total += item
    return total

my_sum_1([1,2,4,5]) # 12

```

### Better coding with errors
A good coder knows how to deal with errors. Let's take some bad input for the 
my_sum_1 function in the previous section:

```python
my_sum_1([1,2,'bob',5])
```

You'd get something like this:
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in my_sum_1
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
```
So we can see that Python is complaining that you're trying to add a string
with an int. It's not the best error message, if we expect the list to have only
numbers why would there be a string? In this case we knew what was in the
list, what if we didn't?

Let's write a better sum function that checks to see if the item being added
is a number. If it's not, raise an error to let the user know what's in the
list.

```python
# First let's import this very useful numbers package
# Particularly the number class
from numbers import Number

def my_sum_2(items):
    total = 0
    for item in items:
        # We check if the list item is a number
        # isinstance is a function we can use to compare types
        # in this case it would be True for 0, 3, 4.4 etc but false for 'me'
        # and other strings
        if isinstance(item, Number):
            total += item
        else:
            # In the same way we return values, we raise Errors
            # This is a different kind of error we've never seen but is a lot
            # more useful. As the name suggests, we have a problem with a value
            raise ValueError('List item %s is not a number' % item)
    return total

my_sum_2([1,2,'bob',5]) # Much better
```

Now the error message is a lot clearer:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in my_sum_2
ValueError: List item bob is not a number
```

### Range Function
If you have some experience with other programming languages, you may be
accustomed to for-loops with a variable that's the iteration number. Python
can do that as well:
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

### Exercises 1
1. For-loops are best suited to finite objects - true or false?
2. Write a function `product` that uses a for-loop to multiply every item
    in a list passed as an argument.
    1. What happens if the empty list is given? Modify the function such that
        if an empty list is given, 1 is returned
    2. What happens if the list has data that aren't numbers? Raise an error
        if a non-number is detected.
3. Use the range function to create for loop that prints the numbers 35 to
    210 in increments of 3
4. Write a function my_max which determines the highest number found in a list.
    Let's break it down, you will be constantly comparing the current number to
    last recorded highest number. Think about, the highest number can appear
    anywhere in the list, right? So what do you compare the first number to?
    When you create a max_num variable, first set it to -100000000000. 

## While Loops
Another common way to loop through code is the while-loop. The for-loop loops
through a series of objects. The while-loop is considerably different, the loop
will continue until a condition is met. Similar to if-statements, the
while-statement evaluates a boolean expression to determine if it's True or
False. It does that evaluation at the beginning of every iteration. If the
expression evaluates to False then the loop is exited and the subsequent code
is run. If it's True, then the code in the while-loop is run and condition is
re-evaluated once again.

```python
# We can start off simple with a countdown
def countdown(n):
    while n > 0:
        print (n)
        n = n - 1

countdown(5) # 5,4,3,2,1
countdown(-10) # Nothing, -10 is less than 0 so the loop never runs
```

It's pretty simple, after typing 'while' you put the boolean expression and
then a semi-colon. All the code under the while block will be executed. After
the last line of while-loop block (n = n - 1) the condition is then evaluated
again. It stops when n = 0 in our example.

So what happens if we don't have that last line which decreases the value of n?
Well Python, as with all programming languages, does what it tell it do. As n
doesn't decrease and will always be greater than 0, and the loop will continue
indefinitely. It's called an infinite loop.
```python
def bad_countdown(n):
    while n > 0:
        print (n)
        
# Don't run this kids, it's bad for your health!
bad_countdown(4)

# ... You ran it didn't you? Fine, press Ctrl-C while in the shell, the
# KeyboardInterrupt will stop the shell from executing the current code

# Remember that function earlier to add two numbers? Let's do it with a while-loop
def add_two_while(numbers):
    count = 0 # Create a counter
        while count < len(numbers):
            print(numbers[count] + 2)
            count += 1 #Increment the counter, why is this important?

add_two_while([1,2,3,4,10]) # 3,4,5,6,12
# In general, any for-loop can be rewritten as a while-loop.
# In the above function, the for-loop version is better suited for the task.

# You may want a loop to default to always repeating. For games that is essential actually.
Let's try to verify user input with the help of a while-loop
def get_favourite_number():
    while True:
        fav_num = input('Please enter your favourite number!\n')
            if fav_num.isdigit(): # Neat built-in function to check whether a string contains only numbers
                print('%s is a nice number' % fav_num)
                break # Exit the loop
            else:
                print('You did not enter a valid number, try again')

# We use the break-statement to immediately exit the loop, doesn't matter how
# many times it was executed or if/when the loop will finish iterate later.
# For-loops can use the break-statement as well
```

Let's see this sample execution of the get favourite number function:
`get_favourite_number()`

```
Please enter your favourite number!
dfds
You did not enter a valid number, try again
Please enter your favourite number!
23
23 is a nice number
```

### Exercises 2
1. Write a function `guess_num` that creates a random number between 1
    and 10 then asks the user to enter a number within that range. If the
    number is smaller or larger the user will be notified accordingly. The user
    can only enter if the number entered is correct.
2. Write a function `print_until_odd` that prints out the elements of a list
    but stops if the current number is odd. If it prints out every element of
    the list then display a congratulatory message. If if finds an odd number,
    tell the user that one was found and exit the loop.
