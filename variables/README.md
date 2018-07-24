# Variables

Variables are names for stored values in a program. They can store a variety of data. Create a new file `my_variables.py` and type the following:

```python
# Variables can be strings i.e. text values
my_name = 'Rico Suave'
# Variables can be numbers, like integers (ints)
total_cars_owned = 10
# There are also floats as well
university_gpa = 3.8
# Somethings we just need to know if something is True or False
can_dance = True
# We can display variable values by using string's format method and a placeholder - {}
print('Hola, me llamo {}'.format(my_name))
print('I have a total of {} cars'.format(total_cars_owned))
```

Can you print your GPA in a sentence as well? Some things to note:

* You don't need underscores in your variable names. It is standard practice in Python to separate words in variable names with them. You should maintain this standard.
* You can change the value of the variable at any time, that's why we call them variables after all. You can even change a variable from one type to another. For example, `university_gpa` can be set to `"3.8"` afterwards. This is generally discouraged as consistency is valuable in programming and the usual operators may not work with the variable's new type.
* You can always write `my_name='Rico Suave'`, but that's just not as readable as `my_name = 'Rico Suave'`. Be nice to yourself and to other programmers who may read your code, use spaces.
