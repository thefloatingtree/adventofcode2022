with open('input.txt') as file:
    lines = file.readlines()

    sums = [0]
    for line in lines:
        if line == "\n":
            sums.append(0)
        else:
            sums[-1] += int(line)
    print(max(sums))