# main.py - Main entry point of the application
from game_logic import play_game

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
        print("Total score accrued:", total_score)
        
        again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if again != "y":
            break
            
    print("\n" + "=" * 50)
    print("             GAME OVER")
    print("=" * 50)
    print("Total Games Played:", games_played)
    print("Final Cumulative Score:", total_score)
    print("Thanks for playing!")

if __name__ == "__main__":
    main()