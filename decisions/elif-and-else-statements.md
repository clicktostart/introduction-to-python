# Elif and Else Statements

There are times where we need to check a variety of values to determine what should be done. Think about getting a grade for your mark. School's usually have many possible grades your mark can fall into: A, B, C etc. Let's a write a function that returns a grade.

```python
def get_grade(mark):
    # This part is normal
    if mark >= 90:
        result = 'A'
    # Now we want to see if someone got a B
    elif mark >= 80:
        result = 'B'
    elif mark >= 70:
        result = 'C'
    # If all other conditions are false, do this code
    else:
        result = 'F' # Pretty harsh from the school if you ask me
    return result

print(get_grade(99))    # 'A'
print(get_grade(85))    # 'B'
print(get_grade(35))    # 'F'
```

**After** the first if statement, we can have more options to check. We use elif \("else if"\) statements to do additional comparisons and run different code. At the end, and only at the end, we used an else statement. This executes as long as no previous condition in the if statement was true. Not too bad right?

What if we wrote multiple ifs?

```python
def get_grade_wrong(mark):
    if mark >= 90:
        result = 'A'

    if mark >= 80:
        result = 'B'

    if mark >= 70:
        result = 'C'

    if mark < 70:
        result = 'F'

    return result

print(get_grade_wrong(99))    # 'C'
print(get_grade_wrong(85))    # 'C'
print(get_grade_wrong(35))    # 'F', they always know when you fail right?
```

A mark of 99 should have been an A but we got a C. When the function is called with 99, it first checks if it's greater than 90. It is so result is set to A. As we don't use `elif` the function continues to check if the mark is greater than 80. 99 **is** greater than 80 so result is now B. The next if statement makes the result C as 99 is greater than 70. Luckily 99 is not less than 70 so the we don't see an F. In this case, `elif` statements would help bring the right results.
