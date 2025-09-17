import random


def computer_choice(random_number):
    if random_number <= 3:
        return "r"
    elif random_number <= 6:
        return "p"
    else:
        return "s"
    

def input_player():
    while True:
        player_choice = input("Rock, Paper, or Scissors?(r/p/s): ").lower()
        if player_choice in ["r","p","s"]:
            return player_choice
        else:
            print("you must input r/p/s")


def scissors_rock_and_paper():
    how_many_computer_win = 0
    how_many_user_win = 0

    while True:
        user_poin = 0
        computer_poin = 0

        play_game = input("Play this game?(y/n): ").lower()
        if play_game == "y":
            while True:
                random_number = random.randint(1, 9)
                choice_computer = computer_choice(random_number)

                while True:
                    user_choice = input(
                        "Rock, Paper, or Scissors?(r/p/s): ").lower()
                    if user_choice in ["r", "p", "s"]:
                        break
                    else:
                        print("input must r/p/s")

                if user_choice == "r" and choice_computer == "p":
                    computer_poin += 1
                    print(
                        f"You Lose! your choice is {user_choice} and computer is {choice_computer}. Computer's poin = {computer_poin} and user's poin = {user_poin}")
                elif user_choice == "r" and choice_computer == "s":
                    user_poin += 1
                    print(
                        f"You win! your choice is {user_choice} and computer is {choice_computer}. Computer's poin = {computer_poin} and user's poin = {user_poin}")
                elif user_choice == "p" and choice_computer == "s":
                    computer_poin += 1
                    print(
                        f"You Lose! your choice is {user_choice} and computer is {choice_computer}. Computer's poin = {computer_poin} and user's poin = {user_poin}")
                elif user_choice == "p" and choice_computer == "r":
                    user_poin += 1
                    print(
                        f"You Win! your choice is {user_choice} and computer is {choice_computer}. Computer's poin = {computer_poin} and user's poin = {user_poin}")
                elif user_choice == "s" and choice_computer == "r":
                    computer_poin += 1
                    print(
                        f"You Lose! your choice is {user_choice} and computer is {choice_computer}. Computer's poin = {computer_poin} and user's poin = {user_poin}")
                elif user_choice == "s" and choice_computer == "p":
                    user_poin += 1
                    print(
                        f"You Win! your choice is {user_choice} and computer is {choice_computer}. Computer's poin = {computer_poin} and user's poin = {user_poin}")
                else:
                    print(
                        f"You Draw! your choice is {user_choice} and computer is {choice_computer}")

                if user_poin == 3:
                    print("Conggratulation1 You Win")
                    how_many_user_win += 1
                    break
                elif computer_poin == 3:
                    how_many_computer_win += 1
                    print("You Lose!")
                    break

        elif play_game == "n":
            print(
                f"Thanks for playing. match overview: you has {how_many_user_win} win and computer has {how_many_computer_win} win")
            break
        else:
            print('Input Invalid! please enter "y" for continue or enter "n" for finish')

def two_player():
    many_player1_win = 0
    many_player2_win = 0

    while True:
        player1_poin = 0
        player2_poin = 0
        play_game = input("Play the game?(y/n): ").lower()
        if play_game == "y":
            while True:
                player1 = input_player()
                player2 = input_player()

                if player1 == "p" and player2 == "s":
                    player2_poin += 1
                    print(f'You Lose! Player 1 is {player1} and player 2 is {player2}. Player 1 poin is {player1_poin} and player 2 poin is {player2_poin}')
                if player1 == "p" and player2 == "r":
                    player1_poin += 1
                    print(f'You Win! Player 1 is {player1} and player 2 is {player2}. Player 1 poin is {player1_poin} and player 2 poin is {player2_poin}')
                if player1 == "r" and player2 == "s":
                    player1_poin += 1
                    print(f'You Win! Player 1 is {player1} and player 2 is {player2}. Player 1 poin is {player1_poin} and player 2 poin is {player2_poin}')
                if player1 == "r" and player2 == "p":
                    player2_poin += 1
                    print(f'You Lose! Player 1 is {player1} and player 2 is {player2}. Player 1 poin is {player1_poin} and player 2 poin is {player2_poin}')
                if player1 == "s" and player2 == "r":
                    player2_poin += 1
                    print(f'You Lose! Player 1 is {player1} and player 2 is {player2}. Player 1 poin is {player1_poin} and player 2 poin is {player2_poin}')
                if player1 == "s" and player2 == "p":
                    player1_poin += 1
                    print(f'You Win! Player 1 is {player1} and player 2 is {player2}. Player 1 poin is {player1_poin} and player 2 poin is {player2_poin}')
                else:
                    print(f"Draw! player 1 is {player1} and player 2 is {player2}. Player 1 poin is {player1_poin} and player 2 poin is {player2_poin}")
                
                if player1_poin == 3:
                    many_player1_win += 1
                    print(f'Player 1 is the winner!')
                    break
                elif player2_poin == 3:
                    many_player2_win += 1
                    print(f'Player 2 is the winner!')
                    break
        elif play_game == "n":
            print(f"Thanks for playing. Overview this match: Player 1 has {many_player1_win} and Player 2 has {many_player2_win}")
        else:
            print('invalid input! plase enter "y" for continue or enter "n" for finnish')


while True:
    user_choice = input("Are you play with computer or friends?(c/f): ").lower()
    if user_choice in ["c","f"]:
        break
    else:
        print("input must c/p")

if user_choice == "c":
    scissors_rock_and_paper()
else:
    two_player()