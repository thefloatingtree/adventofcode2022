alphabet = "abcdefghijklmnopqrstuvwxyz"

def item_priority(item):
    score = alphabet.find(item.lower()) + 1
    return score + 26 if item.isupper() else score

with open('input.txt') as file:
    lines = map(lambda line: line.strip(), file.readlines())
    priority_accumulator = 0
    for line in lines:
        halfway_index = len(line) // 2
        small_compartment = line[:halfway_index]
        large_compartment = line[halfway_index:]

        item_set = set(small_compartment)

        for item in large_compartment:
            if item in item_set:
                priority_accumulator += item_priority(item)
                break

    print(priority_accumulator)
        