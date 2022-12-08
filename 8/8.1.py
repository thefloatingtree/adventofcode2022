def tree_at(grid, x, y):
    return grid[y][x]

def check_is_visible_from_top(grid, tree, x, y):
    for y_cursor in range(0, y):
        potentially_blocking_tree = tree_at(grid, x, y_cursor)
        if tree <= potentially_blocking_tree:
            return False
    return True


def check_is_visible_from_bottom(grid, tree, x, y):
    for y_cursor in range(y + 1, len(grid)):
        potentially_blocking_tree = tree_at(grid, x, y_cursor)
        if tree <= potentially_blocking_tree:
            return False
    return True


def check_is_visible_from_left(grid, tree, x, y):
    for x_cursor in range(0, x):
        potentially_blocking_tree = tree_at(grid, x_cursor, y)
        if tree <= potentially_blocking_tree:
            return False
    return True


def check_is_visible_from_right(grid, tree, x, y):
    for x_cursor in range(x + 1, len(grid[0])):
        potentially_blocking_tree = tree_at(grid, x_cursor, y)
        if tree <= potentially_blocking_tree:
            return False
    return True


with open('input.txt') as file:
    lines = list(map(lambda line: line.strip(), file.readlines()))
    tree_grid = [[int(character) for character in line] for line in lines]
    
    visible_trees_sum = 0
    for y in range(len(tree_grid)):
        for x in range(len(tree_grid[0])):
            tree = tree_at(tree_grid, x, y)
            is_visible_top = check_is_visible_from_top(tree_grid, tree, x, y)
            is_visible_bottom = check_is_visible_from_bottom(tree_grid, tree, x, y)
            is_visible_left = check_is_visible_from_left(tree_grid, tree, x, y)
            is_visible_right = check_is_visible_from_right(tree_grid, tree, x, y)
            if is_visible_top or is_visible_bottom or is_visible_left or is_visible_right:
                visible_trees_sum += 1
    print(visible_trees_sum)
