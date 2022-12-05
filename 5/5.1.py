from itertools import zip_longest

# https://stackoverflow.com/questions/3415072/pythonic-way-to-iterate-over-sequence-4-items-at-a-time
def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

def deserialize_crate_stacks(data):
    (crate_data, crate_stack_data) = (data[:-1], data[-1])
    stack_count = len(crate_stack_data.split('   '))
    initial_state = [[] for _ in range(stack_count)]
    for line in reversed(crate_data):
        for index, values in enumerate(grouper(4, line, ' ')):
            (_, character, _, _) = values
            if character != ' ':
                initial_state[index].append(character)
    return initial_state

def deserialize_instructions(data):
    pop_count_token = "move "
    from_index_token = "from "
    to_index_token = "to "
    end_token = "\n"
    instructions = []
    for line in data:
        pop_count_start_index = line.find(pop_count_token) + len(pop_count_token)
        pop_count_end_index = line.find(from_index_token)
        from_index_start_index = line.find(from_index_token) + len(from_index_token)
        from_index_end_index = line.find(to_index_token)
        to_index_start_index = line.find(to_index_token) + len(to_index_token)
        to_index_end_index = line.find(end_token)
        pop_count = int(line[pop_count_start_index:pop_count_end_index])
        from_index = int(line[from_index_start_index:from_index_end_index]) - 1
        to_index = int(line[to_index_start_index:to_index_end_index]) - 1
        instructions.append((pop_count, from_index, to_index))
    return instructions


def perform_instruction(crate_stacks, instruction):
    (pop_count, from_index, to_index) = instruction
    for _ in range(pop_count):
        crate = crate_stacks[from_index].pop()
        crate_stacks[to_index].append(crate)


with open('input.txt') as file:
    lines = file.readlines()
    instruction_separation_index = lines.index('\n')
    crate_stacks = deserialize_crate_stacks(lines[:instruction_separation_index])
    instructions = deserialize_instructions(lines[instruction_separation_index + 1:])

    for instruction in instructions:
        perform_instruction(crate_stacks, instruction)

    top_crates = ''.join(list(map(lambda stack: stack.pop(), crate_stacks)))
    print(top_crates)

