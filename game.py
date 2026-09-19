import random
words = {
    "easy": [
        "cat",
        "book",
        "fish",
        "tree",
        "moon",
        "star",
        "milk",
        "rain",
        "bird",
        "cake"
    ],
    "medium": [
        "garden",
        "planet",
        "rabbit",
        "school",
        "flower",
        "bridge",
        "forest",
        "bottle",
        "summer",
        "winter"
    ],
    "hard": [
        "adventure",
        "education",
        "knowledge",
        "technology",
        "confidence",
        "motivation",
        "creativity",
        "leadership",
        "experience",
        "beautiful"
        ]}
def scramble_word(word):
    letters = list(word)
    while True:
        random.shuffle(letters)
        scrambled = "".join(letters)
        if scrambled != word:
            return scrambled
def choose_difficulty():
    print("\nChoose Difficulty")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    while True:
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            return "easy"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "hard"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
def play_game():
    difficulty = choose_difficulty()
    # Select 5 random words from the selected difficulty
    selected_words = random.sample(words[difficulty], 5)
    score = 0
    print("\n" + "=" * 50)
    print("        WORD SCRAMBLE CHALLENGE")
    print("=" * 50)
    print("Difficulty:", difficulty.upper())
    print("Unscramble the letters to find the correct word.")
    print("You have 3 attempts for each word.")
    for number, word in enumerate(selected_words, 1):
        scrambled = scramble_word(word)
        attempts_left = 3
        print("\n" + "-" * 50)
        print("Word", number)
        print("Scrambled word:", scrambled)
        while attempts_left > 0:
            guess = input("Enter your answer: ").strip().lower()
            if guess == word:
                print("Correct!")
                score += 1
                break
            attempts_left -= 1
            if attempts_left > 0:
                print("Wrong answer!")
                print("Attempts left:", attempts_left)
            else:
                print("Wrong answer!")
                print("The correct word was:", word)
    print("\n" + "=" * 50)
    print("                 RESULTS")
    print("=" * 50)
    print("Difficulty:", difficulty.upper())
    print("Score:", score, "/ 5")
    if score == 5:
        print("Perfect Score!")
    elif score >= 3:
        print("Great job!")
    elif score >= 1:
        print("Good try!")
    else:
        print("Keep practicing!")
    return score
def main():
    total_score = 0
    games_played = 0
    print("=" * 50)
    print("       WELCOME TO WORD SCRAMBLE GAME")
    print("=" * 50)
    while True:
        score = play_game()
        total_score += score
        games_played += 1
        print("\nGames played:", games_played)
        print("Total score:", total_score)
        again = input(
            "\nDo you want to play again? (y/n): "
        ).strip().lower()
        if again != "y":
            break
    print("\n" + "=" * 50)
    print("             GAME OVER")
    print("=" * 50)
    print("Games played:", games_played)
    print("Final score:", total_score)
    print("Thanks for playing!")
if __name__ == "__main__":
    main()


