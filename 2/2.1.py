encodingLookup = {
    "X": "R",
    "Y": "P",
    "Z": "S",
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

winLookup = {
    ("R", "P"): (0, 1),
    ("P", "S"): (0, 1),
    ("S", "R"): (0, 1),
    ("P", "R"): (1, 0),
    ("S", "P"): (1, 0),
    ("R", "S"): (1, 0),
    ("R", "R"): (1, 1),
    ("S", "S"): (1, 1),
    ("P", "P"): (1, 1)
}

ourWinLookup = {
    (0, 1): "Win",
    (1, 0): "Lose",
    (1, 1): "Draw"
}

with open('input.txt') as file:
    lines = file.readlines()
    
    scoreAccumulator = 0
    for line in lines:
        (encodedFirstInput, encodedSecondInput) = line.strip().split(' ')
        
        opponentsChoice = encodingLookup[encodedFirstInput]
        ourChoice = encodingLookup[encodedSecondInput]
        
        ourWinState = ourWinLookup[winLookup[(opponentsChoice, ourChoice)]]
        scoreAccumulator += scoreLookup[ourWinState]
        scoreAccumulator += scoreLookup[ourChoice]

    print(scoreAccumulator)

