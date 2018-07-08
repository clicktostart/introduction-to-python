# Elif and Else Statements

There are times where we need to check a variety of values to determine what should be done. Think about getting a grade for your mark. School's usually have many possible grades your mark can fall into: A, B, C etc. Let's a write a function that returns a grade.

```python
def get_grade(mark):
    # This part is normal
    if mark >= 90:
        result = 'A'
    # Now we want to see if someone got a B
    elif mark < 90 and mark >= 80:
        result = 'B'
    elif mark < 80 and mark >= 70:
        result = 'C'
    # If all other conditions are false, do this code
    else:
        result = 'F' # Pretty harsh from the school if you ask me
    return result

get_grade(100)  # 'A'
get_grade(85)   # 'B'
get_grade(35)   # 'F'
```

**After** the first if statement, we can have more options to check. We use elif \("else if"\) statements to do additional comparisons and run different code. At the end, and only at the end, we used an else statement. This executes as long as no previous condition in the if statement was true. Not too bad right? But wait... why can't we just write multiple if statements?

```python
def get_grade_inefficient(mark):
    if mark >= 90:
        result = 'A'

    if mark < 90 and mark >= 80:
        result = 'B'

    if mark < 80 and mark >= 70:
        result = 'C'

    if mark < 70:
        result = 'F'

    return result

get_grade_inefficient(100)  # 'A'
get_grade_inefficient(85)   # 'B'
get_grade_inefficient(35)   # 'F'
```

They retun the same results! But as the function name implies, this is really inefficient. For one, no matter what grade the user gets, the function always checks each if statement every single time it's run. In the first `get_grade` function, no more checks needed to be done if the grade was an A for example. In the second version, Python still checks if the grade is B or C even though we already got the answer. That's just unnecessary. Also, we have to explicitly state the last case for the F, in the first function we just `else` to state what the default value is.

## Exercises

1. Write a function `chosen_one` which accepts a name. If the name is 'Neo' then print 'You are the chosen one' and return True. Otherwise let them know they aren't the chosen one and return false.
2. The Three Stooges were Moe, Larry and Shemp. Write a function `we_miss_you` that accepts a name. If the name is one of the Stooges then return "I'm gonna change my socks. What an experience!". Otherwise return "Don't forget to watch their show on YouTube!"
3. Write a function `is_triangle` that accepts 3 numbers from a user and determines if they form a triangle. Three numbers for a triangle if and only if the sum of two sides are greater than the third side. So for three sides `a`, `b` and `c`: a + b &gt;= c, b + c &gt;= a and c + a &gt;= b.
4. Create a function `guessing_game` where the computer generates a random number between 1 and 10. If the user gets the answer correct print "Congratulations", if they get it wrong print "Sorry, wrong number!".
   * Remember, to get a random integer first import the random module:

     `from random import randint` and specify the ranges for randint. E.g. `randint(3,8)` - choose a number between 3 and 8 inclusive.
5. Write a function `happy_song` that accepts mood as an argument. If the mood is happy then ask the user if they know it. If they're happy and know it, print "Clap your hands". If they're happy and don't know it then print "At least you're happy". If mood is sad then print "Laughter is the best medicine". For any other mood print "Just keep swimming".



