board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]

def print_board():
    for row in board:
        print(row)

def player_move(player):
    while True:
        try:
            row = int(input("Enter row for {} (0, 1, 2): ".format(player)))
            col = int(input("Enter column for {} (0, 1, 2): ".format(player)))
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("That space is already occupied. Please try again.")
        except:
            print("Invalid input. Please try again.")

def check_win(player):
    for i in range(3):
        # check rows
        if board[i] == [player, player, player]:
            return True
        # check columns
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    # check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def play_game():
    for i in range(9):
        if i % 2 == 0:
            player = 'X'
        else:
            player = 'O'

        print_board()
        player_move(player)
        if check_win(player):
            print("{} wins!".format(player))
            print_board()
            break
    else:
        print("It's a tie!")

play_game()
