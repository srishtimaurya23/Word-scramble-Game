from utils import scramble_word
from word_bank import WORDS
from input_handler import validchoice
def testletters():
    word="garden"
    scrambled=scramble_word(word)
    assert sorted(word)==sorted(scrambled)
def testlevels():
    assert "easy" in WORDS
    assert "medium" in WORDS
    assert "hard" in WORDS
def testwords():
    assert len(WORDS["easy"])>=5
    assert len(WORDS["medium"])>=5
    assert len(WORDS["hard"])>=5
def testvalidation():
    assert validchoice("y")
    assert validchoice("n")
    assert not validchoice("x")
if __name__=="__main__":
    testletters()
    testlevels()
    testwords()
    testvalidation()
    print("All tests passed.")
