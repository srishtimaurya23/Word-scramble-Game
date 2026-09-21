import random
from word_bank import WORDS
from utils import scramble_word, choose_difficulty

def play_game():
    """Executes a single round of the Word Scramble game."""
    difficulty = choose_difficulty()
    selected_words = random.sample(WORDS[difficulty], 5)
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
        print("Word", number, "of 5")
        print("Scrambled word:", scrambled)
        
        while attempts_left > 0:
            guess = input("Enter your answer: ").strip().lower()
            if guess == word:
                print("Correct!")
                score += 1
                break
            attempts_left -= 1
            if attempts_left > 0:
                print("Wrong answer! Attempts left:", attempts_left)
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