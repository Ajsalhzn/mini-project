def print_board(board):
    """
    This function prints the current state of the board
    """
    print('  |  |')
    print(' '+ board[0] + '|' + board[1] + '|' + board[2])
    print('  |  |')
    print('-------------')
    print(' '+ board[3] + '|' + board[4] + '|' + board[5])
    print('  |  |')
    print('-------------')
    print('  |  |')
    print(' '+ board[6] + '|' + board[7] + '|' + board[8])
    print('  |  |')
   
def check_win(board, palayar):
    """
    This function checks whether the playar has won the game.
    """
    if((board[0] == playar and board[1] == playar and board[2] == playar) or
       (board[3] == playar and board[4] == playar and board[5] == playar) or
       (board[6] == playar and board[7] == playar and board[8] == playar) or
       (board[0] == playar and board[3] == playar and board[6] == playar) or
       (board[1] == playar and board[4] == playar and board[7] == playar) or
       (board[2] == playar and board[5] == playar and board[8] == playar) or
       (board[0] == playar and board[4] == playar and board[8] == playar) or
       (board[2] == playar and board[4] == playar and board[6] == playar)):
        return True
    else:
        return False
    

def play_game():
    """
    This function plays the tic tac toe game.
    """
    board = [' '] * 9
    player = 'X'
    play_game = False

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while not game_over:
        print(f"it's {player}'s turn.")
        position = int(input("Enter a position(1-9): ")) - 1

        if board[position] == ' ':
            board[position] = player
