import random


def computer_choice(random_number):
    if random_number <= 3:
        return "r"
    elif random_number <= 6:
        return "p"
    else:
        return "s"


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
            print('Input Invalid! please enter "y" for continue or enter "n for finish')


if __name__ == "__main__":
    scissors_rock_and_paper()
