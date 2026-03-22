# 4. Write a function to create a game of Rock, Paper, Scissors. The function will return the winner of the
# game played by two players. The arguments to the function will be player1 (the first player’s choice)
# and player2 (the second player’s choice), if no argument is provided then the default for either player
# should be Rock.

# Print the winner according to the following rules.

# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock
# 
# Examples: 

# find_winner(”Rock”, ”Paper”) → ”Player 2 wins!”,
# find_winner(”Scissors”, ”Paper”) → ”Player 1 wins!”,
# find_winner(”Rock”, ”Rock”) → ”It’s a tie!”
# find_winner(”Rock”) → ”It’s a tie!”
# find_winner( ) → ”It’s a tie!”
# find_winner(”Scissors”) → ”Player 2 wins!”

def find_winner(player1 = 'rock', player2 = 'rock'):

    if player1 == player2:
        return 'it is a tie'
    
    elif player1 == 'rock' and player2 == 'scissors':
        winner = 'player1 wins'
    elif player1 == 'scissors' and player2 == 'paper':
        winner = 'player1 wins'
    elif player1 == 'paper' and player2 == 'rock':
        winner = 'player1 wins'
    else:
        winner = 'player2 wins'
    
    return winner

player1_choice = input('rock, paper, or scissors: ')
player2_choice = input('rock, paper, or scissors: ')
print(find_winner(player1_choice, player2_choice))



