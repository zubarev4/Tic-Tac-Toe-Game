def display(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_info():
    while True:
        player_nr = input('Do you want to be Player 1 (X) or Player 2 (O)?').strip().upper()
        if player_nr in ['1', 'X']:
            return 'X', 'O'
        elif player_nr in ['2', 'O']:
            return 'O', 'X'
        else:
            print('Invalid input. Please enter 1 or 2.')
            continue

def player_turn(board, player):
    while True:
        inp = input(f'Where do you want to place your {player} (1-9)?').strip()
        if inp in '123456789' and board[int(inp)] == ' ':
            board[int(inp)] = player
            display(board)
            break

def check_win(board, player):
    win_conditions = [
        (7, 8, 9), (4, 5, 6), (1, 2, 3),
        (7, 4, 1), (8, 5, 2), (9, 6, 3),
        (7, 5, 3), (9, 5, 1)
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_tie(board):
    return ' ' not in board[1:]


test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
display(test_board)
player1, player2 = player_info()
players = [player1, player2]

while not check_win(test_board, player1) and not check_win(test_board, player2):
    for player in players:
        player_turn(test_board, player)
        if check_win(test_board, player):
            print(f'Player {player1 if player == player1 else player2} wins!')
            break
        elif check_tie(test_board):
            print('It\'s a tie!')
            break

