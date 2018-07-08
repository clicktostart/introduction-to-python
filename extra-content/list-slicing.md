# List Slicing

Now that you're comfortable with indices, let's to some cool things with lists. Slicing is taking a portion of a list and creating a new one. Think of it like cutting a slice of cake, but the original one stays intact \(wouldn't that be absolutely amazing?\). Let's see below:

```python
fruits = ['banana', 'mango', 'tomato', 'plum', 'guava']
fruits[1] # 'mango'

# Let's slice to get a new list that starts from mango
fruits[1:]
# Above we tell Python we want a list that starts from the fruit's second item
# (recall that the 2nd item has index 1) till the end of the list

# So if we wanted plum and guava chow (ewww) we'll do the following
fruits[3:]

# Let's slice to get a new list that ends with plum
fruits[:4]
# Above we tell Python to start slicing from the beginning and end with fruit's
# 4th item. It's a little tricky, when a number came before the colon we gave
# the item's index. Now we give one more than the item's index. Practice more!
fruits[:5] # ['banana', 'mango', 'tomato', 'plum', 'guava']
fruits[:1] # ['banana']
fruits[:3] # ['banana', 'mango', 'tomato']

# Let's take it a step further and put them both together
fruits[1:4] # ['mango', 'tomato', 'plum']
# Make sure you understand, you're skipping the first element and going up to
# the fourth one. Skip banana and stop and plum
fruits[2:3] # Skip banana and mango, end at tomato. So only tomato!
```

