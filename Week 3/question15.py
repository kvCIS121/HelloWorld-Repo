
#rock beats scissors
#scissors beats paper
#paper beats rock

done = False

while not done:
    player1 = input('rock, paper, or scissors. Player1 choice: ')
    player2 = input('rock, paper, or scissors. Player2 choice: ')

    if player1 == 'rock' and player2 == 'scissors':
        winner = ('player1')
    elif player1 == 'scissors' and player2 == 'paper':
        winner = ('player1')
    elif player1 == 'paper' and player2 == 'rock':
        winner = ('player1')
    else:
        winner = ('player2')
    print(f'the winner is  {winner}')

   
