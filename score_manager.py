def gameresult(difficulty,score):
    print("\n" + "=" * 50)
    print("                 RESULTS")
    print("=" * 50)
    print("Difficulty:",difficulty.upper())
    print("Score:",score, "/ 5")
    if score==5:
        print("Perfect Score!")
    elif score>=3:
        print("Great job!")
    elif score>=1:
        print("Good try!")
    else:
        print("Keep practicing!")
def finalresult(gamesplayed,totalscore):
    print("\n" + "=" * 50)
    print("             GAME OVER")
    print("=" * 50)
    print("Total Games Played:",gamesplayed)
    print("Final Cumulative Score:",totalscore)
    print("Thanks for playing!")
