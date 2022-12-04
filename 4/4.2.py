with open('input.txt') as file:
    lines = map(lambda line: line.strip(), file.readlines())
    overlapsCount = 0
    for line in lines:
        [sectionRangeOne, sectionRangeTwo] = line.split(',')
        [sectionOneStart, sectionOneEnd] = map(lambda x: int(x), sectionRangeOne.split('-'))
        [sectionTwoStart, sectionTwoEnd] = map(lambda x: int(x), sectionRangeTwo.split('-'))
        sectionOneSet = set(range(sectionOneStart, sectionOneEnd + 1))
        sectionTwoSet = set(range(sectionTwoStart, sectionTwoEnd + 1))
        if len(sectionOneSet.intersection(sectionTwoSet)):
            overlapsCount += 1

    print(overlapsCount)
    