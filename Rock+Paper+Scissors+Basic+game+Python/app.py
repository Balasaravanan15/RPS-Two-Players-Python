print('rock')
print('paper')
print('scissors')

player1 = input("Enter Player 1's Choice: ").lower()
print('NO CHEATING!\n' * 30)
player2 = input("Enter Player 2's Choice: ").lower()

if player1 == player2:
    print('It is a tie!')

elif player1 == 'rock':
    if player2 == 'scissors':
        print('player1 wins!')
    if player2 == 'paper':
        print('player2 wins!')

elif player1 == 'paper':
    if player2 == 'rock':
        print('player1 wins!')
    if player2 == 'scissors':
        print('player2 wins!')
        
elif player1 == 'scissors':
    if player2 == 'rock':
        print('player2 wins!')
    if player2 == 'paper':
        print('player1 wins!')
        
else:
    print('something went wrong')

'''
if (player1 == 'rock' and player2 == 'paper'):
    print("Player2 Wins!")
elif(player1 == 'paper' and player2 == 'rock'):
    print("Player1 Wins!")
elif(player1 == 'rock' and player2 == 'scissors'):
    print("Player1 Wins!")
elif(player1 == 'scissors' and player2 == 'rock'):
    print("Player2 Wins!")
elif(player1 == 'scissors' and player2 == 'paper'):
    print("Player1 Wins!")
elif(player1 == 'paper' and player2 == 'scissors'):
    print("Player2 Wins!")
elif(player1 == player2):
    print("It is a tie!")
else:
    print("Something went wrong!")
'''