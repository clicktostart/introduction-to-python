# While Loops

Another common way to loop through code is the while-loop. The for-loop loops through a series of objects. The while-loop is considerably different, the loop will continue until a condition is met. Similar to if-statements, the while-statement evaluates a boolean expression to determine if it's True or False. It does that evaluation at the beginning of every iteration. If the expression evaluates to False then the loop is exited and the subsequent code is run. If it's True, then the code in the while-loop is run and condition is re-evaluated once again.

```python
# We can start off simple with a countdown
def countdown(n):
    while n > 0:
        print (n)
        n = n - 1

countdown(5) # 5,4,3,2,1
countdown(-10) # Nothing, -10 is less than 0 so the loop never runs
```

It's pretty simple, after typing 'while' you put the boolean expression and then a semi-colon. All the code under the while block will be executed. After the last line of while-loop block \(n = n - 1\) the condition is then evaluated again. It stops when n = 0 in our example.

So what happens if we don't have that last line which decreases the value of n? Well Python, as with all programming languages, does what it tell it do. As n doesn't decrease and will always be greater than 0, and the loop will continue indefinitely. It's called an infinite loop.

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

Let's see this sample execution of the get favourite number function: `get_favourite_number()`

```text
Please enter your favourite number!
dfds
You did not enter a valid number, try again
Please enter your favourite number!
23
23 is a nice number
```

## Exercises

1. Write a function `guess_num` that creates a random number between 1 and 10

   then asks the user to enter a number within that range. If the number is smaller

   or larger the user will be notified accordingly. The user can only enter if the

   number entered is correct.

2. Write a function `print_until_odd` that prints out the elements of a list but

   stops if the current number is odd. If it prints out every element of the list

   then display a congratulatory message. If if finds an odd number, tell the user

   that one was found and exit the loop.

