# Tic Tac Toe Game
# by Ilai
import random

def print_board(current_board):

    print("\nBoard:")
    for i, card in enumerate(current_board):
        if current_board[i] == 'x':
            print(f"[x]", end=' ')
        elif current_board[i] == 'o':
            print(f"[o]", end=' ')
        else:
            print(f"[]", end=' ')

        if (i + 1) % 3 == 0:
            print()


def get_player_data(p_choice=None):
    symbols = ['x', 'o']
    # player_dat = []
    name = input("\nPlease enter your name: ")
    name = name.lower()
    while True:
        try:
            if p_choice == "x":
                choice = "o"
                player_dat = [name, choice]
                return player_dat

            if p_choice == "o":
                choice = "x"
                player_dat = [name, choice]
                return player_dat

            choice = input(f"\n{name} Please choose (X\O).\nif you want a random symbol press 'enter'\n your choice: ")
            choice = choice.lower()
            if choice == "":
                random.shuffle(symbols)
                choice = random.choice(symbols)
                player_dat = [name, choice]
                return player_dat

            elif choice not in symbols:
                raise Exception("\nInvalid symbol please try again.")
            player_dat = [name, choice]
            return player_dat

        except Exception as e:
            print(e)



def player_1():
    print("\nPlayer 1 pick.")
    p_1 = get_player_data()
    print(f"\nwelcome {p_1[0]} you are Player_1\n"
          f"your chosen symbol is: {p_1[1]}.\n")
    return p_1


def player_2(p_1):
    print("\nPlayer 2 pick,\n"
          "(if you are lonely and have no one to play with for play vs 'computer' press 'enter' for name.")
    p_2 = get_player_data(p_1[1])
    if p_2[0] == "":
        p_2 = ["computer", p_2[1]]
        print(f"\nwelcome {p_2[0]} you are Player_2\n"
              f"your chosen symbol is: {p_2[1]}.\n")
        return p_2
    print(f"\nwelcome {p_2[0]} you are Player_2\n"
          f"your chosen symbol is: {p_2[1]}.\n")

    return p_2


def winning_condition(board):
    winners_list = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]]

    for winner in winners_list:
        if board[winner[0]] == board[winner[1]] == board[winner[2]] != '':
            return True

    return False


def game_order():
    current_board = ['', '', '', '', '', '', '', '', '']
    p_1 = player_1()
    p_2 = player_2(p_1)
    chosen_indexes = []
    while True:
        print()
        print_board(current_board)
        index_1 = player_choice(p_1, chosen_indexes)
        chosen_indexes.append(index_1 + 1)
        current_board[index_1] = p_1[1]
        found = winning_condition(current_board)
        print_board(current_board)
        if found:
            return p_1

        if len(chosen_indexes) >= len(current_board):
            break

        index_2 = player_choice(p_2, chosen_indexes)
        chosen_indexes.append(index_2 + 1)
        current_board[index_2] = p_2[1]
        found = winning_condition(current_board)
        if found:
            print_board(current_board)
            return p_2


    print_board(current_board)
    return "\nits a draw."


def play_game():
    print("-------------------------")
    print("Welcome to Tic-Tac-Toe!")
    print("-------------------------")
    while True:
        final_outcome = game_order()
        while True:
            try:
                if type(final_outcome) == list:
                    print(f"\ncongrats {final_outcome[0]} won!."
                            f"\nif you would like to play again press 'R', to end the game press 'Q'.")
                    game_status = input("your choice: ")
                    game_status = game_status.lower()
                    print(game_status)
                    if game_status != "r" and game_status != "q":
                        raise Exception("\nInvalid choice please try again.")

                    else:
                        break
                else:
                    print(f"{final_outcome}\n"
                            f"\nif you would like to play again press 'R', to end the game press 'Q'.")
                    game_status = input("your choice: ")
                    game_status = game_status.lower()
                    print(game_status)
                    if game_status != "r" and game_status != "q":
                        raise Exception("\nInvalid choice please try again.")

                    else:
                        break
            except Exception as e:
                print(e)

        if game_status == "r":
            print("restarting game. . .")
            continue
        if game_status == "q":
            print("\nThank you for playing!")
            break


def player_choice(p_data, chosen_indexes):
    while True:
        try:
            print(f"\nits {p_data[0]} turn.")
            if p_data[0] == "computer":
                p_choice = random.randint(1, 9)
                if p_choice in chosen_indexes or p_choice < 1 or p_choice > 9:
                    raise Exception("Invalid index please try again.")

                return p_choice - 1

            else:
                p_choice = int(input(f"your symbol is {p_data[1]}."
                                     f"\nplease choose index 1 - 9: "))


                if p_choice in chosen_indexes or p_choice < 1 or p_choice > 9:
                    raise Exception("Invalid index please try again.")

                return p_choice - 1

        except Exception as e:
            print(e)


if __name__ == '__main__':
    play_game()