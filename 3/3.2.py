alphabet = "abcdefghijklmnopqrstuvwxyz"

# https://stackoverflow.com/questions/312443/how-do-i-split-a-list-into-equally-sized-chunks
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def item_priority(item):
    score = alphabet.find(item.lower()) + 1
    return score + 26 if item.isupper() else score


with open("input.txt") as file:
    lines = list(map(lambda line: line.strip(), file.readlines()))

    priority_accumulator = 0
    groups = chunks(lines, 3)
    for group in groups:
        [first, second, third] = group
        first_set = set(first)
        second_set = set(second)
        third_set = set(third)
        [common_item] = list(first_set.intersection(second_set, third_set))
        priority_accumulator += item_priority(common_item)

    print(priority_accumulator)

