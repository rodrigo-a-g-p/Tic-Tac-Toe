def show_board(board):
    print(f'{board[1]}|{board[2]}|{board[3]}')
    print('-+-+-')
    print(f'{board[4]}|{board[5]}|{board[6]}')
    print('-+-+-')
    print(f'{board[7]}|{board[8]}|{board[9]}')


def place_move(board, player):
    print(f"Player {player}, make your move.")
    made_move = False
    while not made_move:
        move = input()
        valid_move = is_move_valid(board, move)
        if valid_move is not None:
            if board[valid_move] == ' ':
                board[valid_move] = player
                made_move = True
            else:
                print("That place is already filled.\nChoose another square.")
    show_board(board)
    return board


def is_move_valid(board, user_input):
    invalid_move_message = 'This move is not valid. Please, write a number between 1 and 9.'
    try:
        user_input = int(user_input)
        if user_input in board.keys():
            return user_input
        else:
            print(invalid_move_message)
            return None
    except ValueError:
        print(invalid_move_message)
        return None


def change_player_turn(player):
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player


def check_for_winner(board, player):
    # across top (first row)
    if board[1] == board[2] == board[3] != ' ':
        return player_won_statement(player)

    # across the middle (second row)
    if board[4] == board[5] == board[6] != ' ':
        return player_won_statement(player)

    # across the bottom (third row)
    if board[7] == board[8] == board[9] != ' ':
        return player_won_statement(player)

    # down the left side (first column)
    if board[1] == board[4] == board[7] != ' ':
        return player_won_statement(player)

    # down the middle (second column)
    if board[2] == board[5] == board[8] != ' ':
        return player_won_statement(player)

    # down the right side (third column)
    if board[3] == board[6] == board[9] != ' ':
        return player_won_statement(player)

    # top-down diagonal
    if board[1] == board[5] == board[9] != ' ':
        return player_won_statement(player)

    # down-top diagonal
    if board[3] == board[5] == board[7] != ' ':
        return player_won_statement(player)


def is_game_tied(board, winner):
    if ' ' not in board.values() and not winner:
        print("\nGame Over.\n")
        print("It's a Tie!!")
        return True


def player_won_statement(player):
    print("\nGame Over.\n")
    print(f" ***** Player {player} won the game  ***** ")
    return True


def endgame_question(board, start_player):
    restart = input("Do want to play Again?(y/n) ")
    if restart == "y" or restart == "Y":
        for each_key in board.keys():
            board[each_key] = " "
        play_game(start_player, board)
    else:
        print("Ok, bye!")


def play_game(player_to_make_move, board):
    show_board(board)

    possible_winner = False
    possibly_tied_game = False

    while not possible_winner and not possibly_tied_game:

        # making a move and return the altered board
        current_board = place_move(board, player_to_make_move)

        # is game over?
        possible_winner = check_for_winner(current_board, player_to_make_move)
        possibly_tied_game = is_game_tied(current_board, possible_winner)

        # changing player's turn
        player_to_make_move = change_player_turn(player_to_make_move)

    endgame_question(board, player_to_make_move)


def init():
    starting_player = 'X'  # player variable is either "X" or "O"
    board_layout = {1: ' ', 2: ' ', 3: ' ',
                    4: ' ', 5: ' ', 6: ' ',
                    7: ' ', 8: ' ', 9: ' '}
    play_game(starting_player, board_layout)


# start game
init()
