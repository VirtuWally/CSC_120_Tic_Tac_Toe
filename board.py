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
    # keep track of total moves; when equals 5, begin checking for a winner
    move_count = 0
    # flags to track the winner; if both remain false at the end of all plays, we have a draw
    player1_winner = False
    player2_winner = False

    # Player definitions; allows different player tokens to be chosen
    player1 = {'Player1': 'X'}
    player2 = {'Player2': 'O'}

    # begin the game by first printing empty playing board
    print_board(ttt_grid)

    while True:
        for i in range(1, 3):
            if i == 1:
                # get player1 input
                while True:
                    ttt_row, ttt_column = get_move(player1)
                    if empty_slot(ttt_row, ttt_column, ttt_grid):
                        ttt_grid[ttt_row][ttt_column] = player1['Player1']  # get player 1 game token
                        out_str = 'Player 1 added mark at location {},{}'
                        print(out_str.format(ttt_row, ttt_column))
                        print_board(ttt_grid)

                        # after maximum 9 moves, there is no winner
                        move_count += 1
                        if move_count == 9:
                            print('Draw!  Game over!')
                            exit()
                        player1_winner, player2_winner = check_win(ttt_grid)

                        # only need to check for player 1 since player 1 made the potential winning move
                        if player1_winner:
                            print('Player 1 wins!  Game over!')
                            exit()

                        break
                    else:
                        # slot is not empty
                        out_str = '**** Board[{}][{}] has already been selected.  Please place marker somewhere ' \
                                  'else on the board'
                        print(out_str.format(ttt_row, ttt_column))
                        print('**** Invalid choice.  Please mark again! ****')
                        print_board(ttt_grid)
            else:
                # get player2 input
                while True:
                    ttt_row, ttt_column = get_move(player2)
                    if empty_slot(ttt_row, ttt_column, ttt_grid):
                        ttt_grid[ttt_row][ttt_column] = player2['Player2']  # get player 2 game token
                        out_str = 'Player 2 added mark at location {},{}'
                        print(out_str.format(ttt_row, ttt_column))
                        print_board(ttt_grid)

                        # after maximum 9 moves, there is no winner
                        move_count += 1
                        # excess logic; we never get here because player 2 gets all of the even numbered moves
                        if move_count == 9:
                            print('Draw!  Game over!')
                            exit()

                        player1_winner, player2_winner = check_win(ttt_grid)

                        # only need to check for player 2 since player 2 made the potential winning move
                        if player2_winner:
                            print('Player 2 wins!  Game over!')
                            exit()

                        break
                    else:
                        # slot is not empty
                        out_str = '**** Board[{}][{}] has already been selected.  Please place marker somewhere ' \
                                  'else on the board'
                        print(out_str.format(ttt_row, ttt_column))
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

        # get row and column number of the player's move; catch improper in integer input
        try:
            row = int(input('Enter row nos (0-2):'))
            col = int(input('Enter col nos (0-2):'))
            if not (0 <= row <= 2) or not (0 <= col <= 2):
                print('**** Invalid row or column.  Please select row / col between values 0 to 2 ****')
                print('**** Invalid choice.  Please mark again! ****')
                continue
            else:
                return row, col
        except:
            print('**** Invalid row or column.  Please select row / col between values 0 to 2 ****')
            print('**** Invalid input type.  Please mark again! ****')
            continue


def check_win(ttt_g):
    # checking winner requires checking rows, columns, left-to-right diagonals, and right-to-left diagonals
    # set p_flags to true when slot is taken by player.  If flag remains True after for-loop, that player wins
    # this will be case for all 4 conditions, such that when winner found, we can end the current game
    p1_win = False
    p2_win = False

    # check rows
    p1_win, p2_win = check_rows(ttt_g)
    if p1_win or p2_win:
        return p1_win, p2_win
    else:
        p1_win, p2_win = check_columns(ttt_g)

    if p1_win or p2_win:
        return p1_win, p2_win
    else:
        p1_win, p2_win = check_left_to_right_diagonal(ttt_g)

    if p1_win or p2_win:
        return p1_win, p2_win
    else:
        p1_win, p2_win = check_right_to_left_diagonal(ttt_g)

    return p1_win, p2_win  # at this point, either p1_wins, p2_wins, or we cannot determine a winner yet


# checks right to left diagonal: 0-2, 1-1, 2-0
def check_right_to_left_diagonal(ttt_g):
    p1_win = False
    p2_win = False
    p1_cnt = 0
    p2_cnt = 0

    for i in range(3):
        if ttt_g[i][2 - i] == 'X':
            p1_cnt += 1
        elif ttt_g[i][2 - i] == 'O':
            p2_cnt += 1
    if p1_cnt == 3:
        p1_win = True  # p1 wins by RTL diagonal
    elif p2_cnt == 3:
        p2_win = True  # p2 wins by RTL diagonal

    return p1_win, p2_win


# checks left to right diagonal: 1-1, 2-2, 3-3
def check_left_to_right_diagonal(ttt_g):
    p1_win = False
    p2_win = False
    p1_cnt = 0
    p2_cnt = 0

    for i in range(3):
        if ttt_g[i][i] == 'X':
            p1_cnt += 1
        elif ttt_g[i][i] == 'O':
            p2_cnt += 1
    if p1_cnt == 3:
        p1_win = True  # p1 wins by LTR diagonal
    elif p2_cnt == 3:
        p2_win = True  # p2 wins by LTR diagonal

    return p1_win, p2_win


def check_columns(ttt_g):
    p1_win = False
    p2_win = False
    for j in range(3):
        p1_cnt = 0
        p2_cnt = 0
        for i in range(3):
            if ttt_g[i][j] == 'X':
                p1_cnt += 1
            elif ttt_g[i][j] == 'O':
                p2_cnt += 1
        if p1_cnt == 3:
            p1_win = True  # p1 wins and we don't need to process unchecked columns
            break
        elif p2_cnt == 3:
            p2_win = True  # p2 wins and we don't need to process unchecked columns
            break
    return p1_win, p2_win


def check_rows(ttt_g):
    p1_win = False
    p2_win = False
    for i in range(3):
        p1_cnt = 0
        p2_cnt = 0
        for j in range(3):
            if ttt_g[i][j] == 'X':
                p1_cnt += 1
            elif ttt_g[i][j] == 'O':
                p2_cnt += 1
        if p1_cnt == 3:
            p1_win = True  # p1 wins and we don't need to process unchecked rows
            break
        elif p2_cnt == 3:
            p2_win = True  # p2 wins and we don't need to process unchecked rows
            break
    return p1_win, p2_win


def print_board(ttt_g):
    # display the playing board on the screen
    print('Printing board...')
    for i in range(0, 3):
        print(ttt_g[i])


main()
