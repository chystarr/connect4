def print_board(board):
    header = '   '
    for i in range(len(board)):
        header += ' ' + str(i) + '  '
    line = '  ' + '+---' * (len(board)) + '+'

    print(header)
    print(line)
    for row in range(len(board[0])):
        print(str(row) + ' ', end = '')
        for col in range(len(board)):
            print('| ' + str(board[col][row]), end = ' ')
        print('|')
        print(line)

def choose_pieces():
    print("What is Player 1's piece? Enter one character:")
    while True:
        player1 = input()
        if player1 == ' ':
            print("A space isn't a valid entry.")
            continue
        elif len(player1) != 1:
            print("Entry must be one character.")
            continue
        else:
            break

    print("What is Player 2's piece? Enter one character:")
    while True:
        player2 = input()
        if player2 == player1:
            print("You can't use the same piece as Player 1!")
            continue
        elif player2 == ' ':
            print("A space isn't a valid entry.")
            continue
        elif len(player2) != 1:
            print("Entry must be one character.")
            continue
        else:
            break
    
    return player1, player2

def move_is_valid(board, col):
    if col < 0 or col > len(board) - 1:
        # column is nonexistent
        return False
    if board[col][0] != ' ':
        # column is filled to the top
        return False
    
    return True
# ISSUE with user choosing column number--need to prevent entry of ' ', letters, etc.
# (ValueError: invalid literal for int() with base 10)
# Add exception handling!!!!!!!!
def make_move(board, piece, designation):
    print(designation + ", choose a column to drop your piece into:")
    col = int(input())
    while not move_is_valid(board, col):
        print("That move is invalid. Please choose a different column:")
        col = int(input())

    for i in range(len(board[col]) - 1, -1, -1):
        if board[col][i] == ' ':
            board[col][i] = piece
            print(piece, "placed in column", str(col))
            return

def line_found(board, piece):
    # check for horizontal lines of 4
    spaces = 0
    for row in range(len(board[0])):
        for col in range(len(board)):
            if board[col][row] == ' ':
                spaces = 0
                continue
            if board[col][row] == piece:
                spaces += 1
            if spaces >= 4:
                return True

    # check for vertical lines of 4
    spaces = 0
    for col in range(len(board)):
        for row in range(len(board[0])):
            if board[col][row] == ' ':
                spaces = 0
                continue
            if board[col][row] == piece:
                spaces += 1
            if spaces >= 4:
                return True

    # check for diagonal lines of 4 (top left to bottom right)
    for col in range(len(board) - 3):
        for row in range(len(board[0]) - 3):
            if (board[col][row] + board[col + 1][row + 1] + board[col + 2][row + 2]
                + board[col + 3][row + 3] == piece * 4):
                return True

    # check for diagonal lines of 4 (bottom left to top right)
    for col in range(len(board) - 3):
        for row in range(3, len(board[0])):
            if (board[col][row] + board[col + 1][row - 1] + board[col + 2][row - 2]
                + board[col + 3][row - 3] == piece * 4):
                return True
    
    return False

def game_won(board, player1, player2):
    if line_found(board, player1):
        print("Player 1 is the winner!")
        return True
    if line_found(board, player2):
        print("Player 2 is the winner!")
        return True
    return False

def game_tied(board):
    for col in board:
        if col[0] == ' ':
            return False
    # every space has been filled
    print("The game has ended in a tie!")
    return True

def finished(board, player1, player2):
    return game_won(board, player1, player2) or game_tied(board)

def main():
    # board is in [col][row] format
    # when players make a move, they choose a column to "drop" their piece into
    board = [[' ' for i in range(6)] for j in range(7)]
    
    player1, player2 = choose_pieces()
    print_board(board)

    current_player = player1
    designation = "Player 1"

    while not finished(board, player1, player2):
        make_move(board, current_player, designation)
        print_board(board)
        if current_player == player1:
            current_player = player2
            designation = "Player 2"
        else:
            current_player = player1
            designation = "Player 1"

if __name__ == '__main__':
    main()