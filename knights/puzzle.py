from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # What A says
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave))),
    # Rules of the game
    And(Or(AKnight, AKnave), Not(And(AKnave, AKnight)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # What A says
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave))),
    # Rules of the game
    And(Or(AKnight, AKnave), Not(And(AKnave, AKnight))),
    And(Or(BKnight, BKnave), Not(And(BKnave, BKnight))),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # What A says
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    # What B says
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # Rules of the game
    And(Or(AKnight, AKnave), Not(And(AKnave, AKnight))),
    And(Or(BKnight, BKnave), Not(And(BKnave, BKnight))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    # B says "A said 'I am a knave'."
    Implication(And(BKnight, AKnight), AKnave),
    Implication(And(BKnight, AKnave), AKnight),
    Implication(And(BKnave, AKnight), AKnight),
    Implication(And(BKnave, AKnave), AKnave),
    # B says "C is a knave."
    Implication(BKnight, CKnave),
    Implication(BKnave, CKnight),
    # C says "A is a knight."
    Implication(CKnight, AKnight),
    Implication(CKnave, AKnave),
    # Rules of the game
    And(Or(AKnight, AKnave), Not(And(AKnave, AKnight))),
    And(Or(BKnight, BKnave), Not(And(BKnave, BKnight))),
    And(Or(CKnight, CKnave), Not(And(CKnave, CKnight))),

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
