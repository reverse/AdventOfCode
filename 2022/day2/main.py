from enum import Enum

class Result(Enum):
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"


class Game(Enum):
    ROCK = "X" 
    PAPER = "Y"
    SCISSORS = "Z"

class Other(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"

map = {
        Other.ROCK: Game.ROCK,
        Other.PAPER: Game.PAPER,
        Other.SCISSORS: Game.SCISSORS,
        }
wins = {
        Game.ROCK: Game.SCISSORS,
        Game.PAPER: Game.ROCK,
        Game.SCISSORS: Game.PAPER,
        }

def moveCost(move):
    if move == Game.ROCK:
        return 1
    elif move == Game.PAPER:
        return 2
    else:
        return 3

def figureOutMove(p1, p2):
    if p1 == Result.DRAW:
        return map[p2]
    elif p1 == Result.WIN:
        return list(wins.keys())[list(wins.values()).index(map[p2])]
    else:
        return wins[map[p2]]

def checkP1Win(p1, p2):
    move = moveCost(p1)
    if p1 == Game.ROCK:
        if (p2 == Other.PAPER):
            return 0 + move
        elif (p2 == Other.SCISSORS):
            return 6 + move
        else:
            return 3 + move

    elif p1 == Game.PAPER:
        if (p2 == Other.ROCK):
            return 6 + move
        elif (p2 == Other.SCISSORS):
            return 0 + move 
        else:
            return 3 + move

    else:
        # scissors
        if (p2 == Other.ROCK):
            return 0 + move
        elif (p2 == Other.PAPER):
            return 6 + move
        else:
            return 3 + move


score = 0
with open("input.txt", "r") as f:
    for item in f.readlines():
        if item == "\n":
            continue
        moves = item.split(" ")
        score += checkP1Win(figureOutMove(Result(moves[1].strip()), Other(moves[0].strip())), Other(moves[0].strip()))

print(score)
        
