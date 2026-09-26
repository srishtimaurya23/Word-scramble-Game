def answer():
    return input("Enter your answer: ").strip().lower()
def validchoice(choice):
    return choice in ("buffer", "total")
def replaychoice():
    while True:
        choice=input("\nDo you want to play again? (y/n): ").strip().lower()
        if validchoice(choice):
            return choice
        print("Invalid choice. Please enter y or n.")
