encodingLookup = {
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win",
    "A": "R",
    "B": "P",
    "C": "S"
}

scoreLookup = {
    "R": 1,
    "P": 2,
    "S": 3,
    "Lose": 0,
    "Draw": 3,
    "Win": 6
}

ourChoiceLookup = {
    ("R", "Win"): "P",
    ("P", "Win"): "S",
    ("S", "Win"): "R",
    ("R", "Lose"): "S",
    ("P", "Lose"): "R",
    ("S", "Lose"): "P",
    ("R", "Draw"): "R",
    ("P", "Draw"): "P",
    ("S", "Draw"): "S",
}

with open('input.txt') as file:
    lines = file.readlines()
    
    scoreAccumulator = 0
    for line in lines:
        (encodedFirstInput, encodedSecondInput) = line.strip().split(' ')
        
        opponentsChoice = encodingLookup[encodedFirstInput]
        winState = encodingLookup[encodedSecondInput]
        ourChoice = ourChoiceLookup[(opponentsChoice, winState)]
        
        scoreAccumulator += scoreLookup[winState]
        scoreAccumulator += scoreLookup[ourChoice]

    print(scoreAccumulator)

