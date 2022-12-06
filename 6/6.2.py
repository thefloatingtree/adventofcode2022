def is_all_characters_unique(data):
    return len(data) == len(set(data))

with open('input.txt') as file:
    data_stream = file.readline().strip()
    start_of_packet = None
    for cursor in range(len(data_stream) - 13):
        possible_start_of_packet = data_stream[cursor:cursor + 14]
        if is_all_characters_unique(possible_start_of_packet):
            start_of_packet = cursor + 14
            break
    print(start_of_packet)
