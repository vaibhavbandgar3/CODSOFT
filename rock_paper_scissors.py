import random

def rock_paper_scissors():
    player_name = input("Enter player's name: ")
    user_wins = 0
    bot_wins = 0

    while True:
        print("\nRock Paper Scissor".center(60))
        print("Choose your option:")
        print("\t\t1. Rock")
        print("\t\t2. Paper")
        print("\t\t3. Scissor")
        print("\t\t4. Exit")

        choice = input(f"{player_name},\nenter your choice (1/2/3/4): ")

        if choice == "4":
            print("")
            print("EXITED SUCCESSFULLY !!!")
            print("")
            print(f"Total {player_name} Wins: {user_wins}")
            print(f"Total BOT Wins: {bot_wins}")

            if user_wins > bot_wins:
                print("")
                print(f"Final Winner: {player_name}")
                print("Congratulations, you won the game!")
            elif bot_wins > user_wins:
                print("")
                print("Final Winner: BOT")
                print("Better luck next time...")
            else:
                print("")
                print("It's a Tie!")
            break

        options = {"1": "Rock", "2": "Paper", "3": "Scissor"}

        if choice in options:
            user_choice = options[choice]
            bot_choice = random.choice(list(options.values()))
            print("")
            print(f"{player_name}'s Choice:", user_choice)
            print("BOT's Choice:", bot_choice)

            if user_choice == bot_choice:
                print("")
                print("RESULT: Tie")
            elif (user_choice == "Rock" and bot_choice == "Scissor") or \
                 (user_choice == "Paper" and bot_choice == "Rock") or \
                 (user_choice == "Scissor" and bot_choice == "Paper"):
                print("RESULT: "f"{player_name} Wins")
                user_wins += 1
            else:
                print("RESULT: BOT Wins")
                bot_wins += 1
        else:
            print("Please enter a valid choice...")

rock_paper_scissors()
