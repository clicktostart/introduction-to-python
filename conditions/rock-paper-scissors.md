# Rock, Paper, Scissors

Let's get even more practice with if-elif-else statements. Create a new file called `rps.py` and following along with the code, filling in as necessary:

```python
# We're going to have Python generate a random number for us
# 1 - rock, 2 - paper, 3 - scissors
# Let's begin by importing the randomint function
from random import randint
# We give the randint function the range of values we want
computer_choice = randint(1,3) # 1 - 3 inclusive

# Create a variable called human_input that asks the user for input
human_input =

# Now let's check the choice to get the human_value
# Complete the function convert_choice as follows:

def convert_choice(letter):
    # If letter equals 'r' then return 1
    if :
        return 1
    # If letter equals 'p' then return 2
    elif :
    # If letter equals 's' then return 3
    elif :
    # Otherwise return 1
    else:


# From the input let's get the human's choice
human_choice = convert_choice(human_input)

# Now do a comparison:
def rps_winner(player1_choice, player2_choice):
    # 1) If the two arguments are equal then it's a tie
    if player1_choice == player2_choice:
        return 'Game is tied'
    # 2) Else, if the player1 is rock and the computer is scissors
        # 3) Or if the player is paper and the computer is rock
        # 4) Or, if the player is scissors and the computer is paper then return
        # 'Player 1 wins!'
    # 5) Otherwise return 'Player 2 wins!'


print(rps_winner(human_choice, computer_choice))
```
