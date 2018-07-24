# Loops

With loops we'll finally have all the Pythonic ingredients to begin making games. Loops allow us to repeat tasks over and over again. Think about how we used if statements before to check user input:

```python
def is_valid_user(username):
    if username == 'shaka zulu':
        return True
    else:
        print('Invalid username')
        return False
```

Well if our entire program checked the input once, it would end with False if I entered 'eric williams'. What if we wanted to give the user 3 times before we stop them from trying? Loops can be useful then.
