import random


def computer_choice(random_number):
    if random_number <= 3:
        return "r"
    elif random_number <= 6:
        return "p"
    else:
        return "s"


def scissors_rock_and_paper():
    while True:
        play_game = input("Play this game?(y/n): ").lower()
        if play_game == "y":
            while True:
                user_choice = input(
                    "Rock, Paper, or Scissors?(r/p/s): ").lower()
                if user_choice in ["r", "p", "s"]:
                    break
                else:
                    print("input must r/p/s")

            random_number = random.randint(1, 9)
            choice_computer = computer_choice(random_number)

            if user_choice == "r" and choice_computer == "p":
                print(
                    f"You Lose! your choice is {user_choice} and computer is {choice_computer}")
            elif user_choice == "r" and choice_computer == "s":
                print(
                    f"You win! your choice is {user_choice} and computer is {choice_computer}")
            elif user_choice == "p" and choice_computer == "s":
                print(
                    f"You Lose! your choice is {user_choice} and computer is {choice_computer}")
            elif user_choice == "p" and choice_computer == "r":
                print(
                    f"You Win! your choice is {user_choice} and computer is {choice_computer}")
            elif user_choice == "s" and choice_computer == "r":
                print(
                    f"You Lose! your choice is {user_choice} and computer is {choice_computer}")
            elif user_choice == "s" and choice_computer == "p":
                print(
                    f"You Win! your choice is {user_choice} and computer is {choice_computer}")
            else:
                print(f"You Draw! your choice is {user_choice} and computer is {choice_computer}")
        elif play_game == "n":
            print("Thanks for playing")
            break
        else:
            print('Input Invalid! please enter "y" for continue or enter "n for finish')


if __name__ == "__main__":
    scissors_rock_and_paper()
