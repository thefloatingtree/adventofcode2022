with open('test_input.txt') as file:
    lines = map(lambda line: line.strip(), file.readlines())
    fullyContainedCount = 0
    for line in lines:
        [sectionRangeOne, sectionRangeTwo] = line.split(',')
        [sectionOneStart, sectionOneEnd] = map(lambda x: int(x), sectionRangeOne.split('-'))
        [sectionTwoStart, sectionTwoEnd] = map(lambda x: int(x), sectionRangeTwo.split('-'))
        if (sectionOneStart >= sectionTwoStart and sectionOneEnd <= sectionTwoEnd):
            fullyContainedCount += 1
            continue
        if (sectionTwoStart >= sectionOneStart and sectionTwoEnd <= sectionOneEnd):
            fullyContainedCount += 1
            continue
    print(fullyContainedCount)
        
        