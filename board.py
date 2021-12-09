# Title:  CSC.120 Software Engineering Project
# SubTitle:  Tic Tac Toe
# Author:  Leon Henry Squire
# Version Stage 2
# Players 1 and 2 can alternate turns

def main():
    # Tic-Tac-Toe grid is a 3 x 3 matrix implemented with a lists of lists
    # '-' represents an empty space on the board
    ttt_grid = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    move_vector = ['', '']  # 1 X 1 matrix of player move
    players = {}
    ttt_row = 0
    ttt_column = 0
    move_count = 0  # keep track of total moves; when equals 3, begin checking for a winner

    # Player definitions
    player1 = {'Player1': 'X'}
    player2 = {'Player2': 'O'}

    # move vector contains grid coordinates used to place marker
    move_vector = []

    # begin the game by first printing empty playing board
    print_board(ttt_grid)

    while True:
        for i in range(1, 3):
            if i == 1:
                # get player1 input
                while True:
                    ttt_row, ttt_column = get_move(player1)
                    if empty_slot(ttt_row, ttt_column, ttt_grid):
                        ttt_grid[ttt_row][ttt_column] = player1['Player1']
                        out_str = 'Player 1 added mark at location {},{}'
                        print(out_str.format(ttt_row, ttt_column))
                        print_board(ttt_grid)
                        move_count += 1
                        break
                    else:
                        # slot is not empty
                        out_str = '**** Board[{}][{}] has already been selected.  Please place marker somewhere ' \
                                  'else on the board'
                        print(out_str.format(ttt_row,ttt_column))
                        print('**** Invalid choice.  Please mark again! ****')
                        print_board(ttt_grid)
            else:
                # get player2 input
                while True:
                    ttt_row, ttt_column = get_move(player2)
                    if empty_slot(ttt_row, ttt_column, ttt_grid):
                        ttt_grid[ttt_row][ttt_column] = player2['Player2']
                        out_str = 'Player 2 added mark at location {},{}'
                        print(out_str.format(ttt_row, ttt_column))
                        print_board(ttt_grid)
                        move_count += 1
                        break
                    else:
                        # slot is not empty
                        out_str = '**** Board[{}][{}] has already been selected.  Please place marker somewhere ' \
                                  'else on the board'
                        print(out_str.format(ttt_row,ttt_column))
                        print('**** Invalid choice.  Please mark again! ****')
                        print_board(ttt_grid)


def empty_slot(row, column, ttt_grid):
    # determine if slot already occupied with player marker; has '-' if empty
    is_empty = True
    if ttt_grid[row][column] != '-':
        is_empty = False
    return is_empty


def get_move(player):
    # player's move is added to the grid
    # determine if this is this player 1 or player 2
    player_name = list(player.keys())
    if player_name[0] == 'Player1':
        player_num = 1
    else:
        player_num = 2
    while True:
        out_str = 'Player {}, make your move'
        print(out_str.format(player_num))

        # get row and column number of the player's move
        row = int(input('Enter row nos (0-2):'))
        col = int(input('Enter col nos (0-2):'))
        if not (0 <= row <=2) or not (0 <= col <=2):
            print('**** Invalid row or column.  Please select row / col between values 0 to 2 ****')
            print('**** Invalid choice.  Please mark again! ****')
            continue
        else:
            return row, col


def print_board(ttt_g):
    # display the playing board on the screen
    print('Printing board...')
    for i in range(0, 3):
        print(ttt_g[i])


def set_player():
    # add players and markers to the players dictionary
    name = input("Enter the player's name: ")
    marker = input("enter the player's marker: ")
    return name, marker


main()
