import time

print('Input Player 1\'s Name: ')
player1 = input()
print('Input Player 2\'s Name: ')
player2 = input()
# the zeros in player_turn is a win counter
player_turn = [player1, player2, 0, 0]
center = [len(player2), len(player1)]
center.sort()
center_line = (center[1] + 12)


def tictactoe():
    time.sleep(1)
    global player1, player2, center_line, player_turn
    # variable to check for win conditions later
    winner = []
    board = [['1', '|', '2', '|', '3'],
             ['4', '|', '5', '|', '6'],
             ['7', '|', '8', '|', '9']]
    turn = ['✖', '○']
    # creates a scoreboard with the player names
    print('\n\n' + 'NEW GAME'.center(center_line))
    print(''.center(center_line, '='))
    print(f'{player1}\'s wins: {player_turn[-2]}'.center(center_line, '='))
    print(f'{player2}\'s wins: {player_turn[-1]}'.center(center_line, '='))
    print(''.center(center_line, '='))
    # ensures that X always goes first
    if player_turn[0] == player2:
        turn.sort()
    # prints the board
    for x, y in enumerate(board):
        print(''.join(board[x]).center(center_line, ))
    # iterates through the maximum 9 turns
    for _ in range(9):
        print('\n' + player_turn[0] + ', pick your spot: '.center(center_line))
        spot = input()
        # ensure that the player enters a number for a valid spot
        while spot.isdecimal() is False:
            print(player_turn[0] + ', type a number: '.center(center_line))
            spot = input()
        # ensures that the player picks a numbered spot 1-9
        while len(spot) > 1:
            print(player_turn[0] + ', type a single digit')
            spot = input()
        # f variable is a counter that checks each spot for the player's input
        # if the number is on the board, that means the spot was available, the counter will reach 14
        # if the f variable gets to 15, the input wasn't on the board so it's already been taken
        f = 0
        for index in range(5):
            for p in range(3):
                if spot not in (board[p][index]):
                    f += 1
        # this triggers if the spot was already taken and the player needs choose again
        while f == 15:
            print('That spot is taken,', player_turn[0] + '. Pick a different spot: '.center(center_line))
            spot = input()
            # next 2 while statements are the same from lines 36-43
            # ensure that the player enters a number for a valid spot (again)
            while spot.isdecimal() is False:
                print(player_turn[0] + ', type a number: '.center(center_line))
                spot = input()
            # ensures that the player picks a numbered spot 1-9 (again)
            while len(spot) > 1:
                print(player_turn[0] + ', type a single digit')
                spot = input()
            # resets f to 0 so the following for loop can see if the above while loop needs to be triggered again
            f = 0
            for index in range(5):
                for p in range(3):
                    if spot not in (board[p][index]):
                        f += 1
        # prints the updated board
        for index in range(5):
            for p in range(3):
                (board[p][index]) = ((board[p][index]).replace(spot, turn[0]))
                if index > 3:
                    print(''.join(board[p]).center(center_line))
        # after inserting a valid spot on the board, this turn.insert changes the turn to the other player
        turn.insert(0, turn[1])
        # after inserting a valid spot on the board, this changes the name to match of the next turn's player name
        player_turn.insert(0, player_turn[1])

        # the rest of the program checks for win conditions
        # first it checks if anything matches 3 in a row
        # second it checks if those matches is an 'X'
        # if it's an 'X', it gives that player a +1 to the win counter. if it's not an 'X', player 'O' gets it
        # if there is a winner, the winner variable length changes from 0 to 1, and that winner is congratulated
        # lastly, if none of the win conditions are met, the game is declared a tie and starts anew

        # this for loop checks for horizontal wins
        for a in range(3):
            if board[a][0] == board[a][2] == board[a][4]:
                winner.append(board[a][0])
                if board[a][0] == '✖':
                    player_turn[-2] += 1
                else:
                    player_turn[-1] += 1
        # checks for vertical wins
        for b in range(5):
            if board[0][b] == board[1][b] == board[2][b]:
                if board[0][b] != '|':
                    winner.append(board[0][b])
                    if board[0][b] == '✖':
                        player_turn[-2] += 1
                    else:
                        player_turn[-1] += 1
        # checks for forward slash diagonal win
        if board[0][0] == board[1][2] == board[2][4]:
            winner.append(board[0][0])
            if board[0][0] == '✖':
                player_turn[-2] += 1
            else:
                player_turn[-1] += 1
        # checks for backslash diagonal wins
        if board[2][0] == board[1][2] == board[0][4]:
            winner.append(board[2][0])
            if board[2][0] == '✖':
                player_turn[-2] += 1
            else:
                player_turn[-1] += 1
        if len(winner) > 0:
            if winner[0] == '✖':
                print(f'\n{player1} Wins!'.center(center_line))
            if winner[0] == '○':
                print(f'\n{player2} Wins!'.center(center_line))
            turn.insert(0, turn[1])
            tictactoe()
    print('It\'s a tie!'.center(center_line))
    tictactoe()


tictactoe()
