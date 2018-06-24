# Dictionaries

A dictionary is a mapping between a key and value. Huh? Well let's remember
lists for one bit. Every list item has an index, a number. That's essentially
a mapping between a number and a value. e.g. `['hi', 'five', 'low', 'slow']` has
a mapping: 0 -> 'hi', 1 -> 'five', 2 -> 'low', 3 -> 'slow'. A dictionary
generalises that further, the mapping doens't have to be from a sequential
integer to a value but a unique **key**. Dictionaries are sequences of
*key-value* pairings. Let's have a look:

```python
grades = {'kevin': 30, 'jabari': 25}
# Let's say kevin and jabari both need to study, ASAP
# With a dictionary we can get their grades as follows:
grades['kevin'] # 30
grades['jabari'] # 25

# Let's get more practice
# Multi-line dictionaries normally have the brackets spanning a few lines
student_profile = {
    'name': 'roger rabbit',
    'age': 14,
    'courses': ['programming', 'maths', 'english', 'spanish'],
    'loves code': True
}

# You can store almost any type as the value, make the keys consistent
student_profile['name'] # 'roger rabbit'
student_profile['courses'][-2] # 'english'

# You can add key-value pairs as well
student_profile['mentor'] = 'plato'
student_profile # {'courses': ['programming', 'maths', 'english', 'spanish'], 'loves code': True, 'mentor': 'plato', 'name': 'roger rabbit', 'age': 14}
# Your order may be different, that's fine. Dictionaries don't keep order

if student_profile['loves code']:
    print('yayy')
```

Keep the following in mind while creating dictionaries:
* Use curly braces to put data inside a dictionary
* Separate each key-value pairing by a comma
* As with lists and tuples, use square brackets to get values from a dictionary

```python
# At time it might be useful to see the keys or the values alone
student_profile.keys() # dict_keys(['courses', 'loves code', 'mentor', 'name', 'age'])
student_profile.values() # dict_values([['programming', 'maths', 'english', 'spanish'], True, 'plato', 'roger rabbit', 14])

if 'favourite course' not in student_profile.keys():
    student_profile['favourite course'] = 'python'

student_profile['favourite course'] # 'python'
```

## Exercises

1.  A dictionary is an unordered sequence of key-value pairs. True or False?
2.  Consider the dict that contains European football clubs and the amount of
    Champions League trophies they won:
    `clubs = {‘real madrid’: 13, ‘ac milan’: 7, ‘bayern munich’: 5, ‘ajax’: 4}`.
    1. Real Madrid are undoubtedly the greatest football team ever created but
    there’s space for that other Spanish team. Add Barcelona with their measly
    5 trophies.
    2. How many trophies did ajax win? Get the value from the dictionary
    3. We have a function that’s interested in the teams but not so much
    their trophy haul. Return a list of keys for `clubs`
    4. A very ambitious but deluded Manchester City fan claims that his club
    has won champions league. Verify with a condition that his club has not.
