# Exercises

1. Write a function `chosen_one` which accepts a parameter `name`. If the name is 'Neo' then print 'You are the chosen one' and return True. Otherwise let them know they aren't the chosen one and return false.
2. The Three Stooges were Moe, Larry and Shemp. Write a function `we_miss_you` that accepts a parameter `name`. If `name` is one of the Stooges then return "I'm gonna change my socks. What an experience!". Otherwise return "Don't forget to watch their show on YouTube!"
    * Tip - use the `or` operator
3. Write a function `is_triangle` that accepts 3 numbers and determines if they form a triangle. Three numbers form a triangle if and only if the sum of two sides are greater than the third side. So for three sides `a`, `b` and `c`: a + b &gt;= c, b + c &gt;= a and c + a &gt;= b.
    * Tip - use the `and` operator
4. Create a function `guessing_game` where the computer generates a random number between 1 and 10. If the user gets the answer correct return "Congratulations", if they get it wrong print "Sorry, wrong number!".
   * Remember, to get a random integer first import the random module: `from random import randint` and specify the ranges for randint. E.g. `randint(3,8)` - chooses a number between 3 and 8 inclusive.
   * Tip - use the `else` keyword
5. Write a function `happy_song` that accepts a parameter `mood`. If the mood is "happy" then ask the user if they know it, storing the result in a variable `know_it` - "Y" for yes and "N" for no. If they're happy and know it, return "Clap your hands". If they're happy and don't know it then return "At least you're happy". If mood is sad then return "Laughter is the best medicine". For any other mood return "Just keep swimming".
    * Tip - use the `elif` keyword
