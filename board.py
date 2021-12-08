# Title:  CSC.120 Software Engineering Project
# SubTitle:  Tic Tac Toe
# Author:  Leon Henry Squire
# Version Stage 2
# Players 1 and 2 can alternate turns

def main
    # Tic-Tac-Toe grid is a 3 x 3 matrix implemented with a lists of lists
    # '-' represents an empty space on the board
    ttt_grid = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def print_board(ttt_g)
    print('Printing board')
    for i in range(0,3):
      print(ttt_g[i])

main()
