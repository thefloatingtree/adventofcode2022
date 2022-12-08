def tree_at(grid, x, y):
    return grid[y][x]

def find_number_of_trees_visible_from_top(grid, tree, x, y):
    number_of_trees = 0
    for y_cursor in reversed(range(0, y)):
        number_of_trees += 1
        potentially_blocking_tree = tree_at(grid, x, y_cursor)
        if tree <= potentially_blocking_tree:
            return number_of_trees
    return number_of_trees


def find_number_of_trees_visible_from_bottom(grid, tree, x, y):
    number_of_trees = 0
    for y_cursor in range(y + 1, len(grid)):
        number_of_trees += 1
        potentially_blocking_tree = tree_at(grid, x, y_cursor)
        if tree <= potentially_blocking_tree:
            return number_of_trees
    return number_of_trees


def find_number_of_trees_visible_from_left(grid, tree, x, y):
    number_of_trees = 0
    for x_cursor in reversed(range(0, x)):
        number_of_trees += 1
        potentially_blocking_tree = tree_at(grid, x_cursor, y)
        if tree <= potentially_blocking_tree:
            return number_of_trees
    return number_of_trees


def find_number_of_trees_visible_from_right(grid, tree, x, y):
    number_of_trees = 0
    for x_cursor in range(x + 1, len(grid[0])):
        number_of_trees += 1
        potentially_blocking_tree = tree_at(grid, x_cursor, y)
        if tree <= potentially_blocking_tree:
            return number_of_trees
    return number_of_trees


with open('input.txt') as file:
    lines = list(map(lambda line: line.strip(), file.readlines()))
    tree_grid = [[int(character) for character in line] for line in lines]
    
    scenic_scores = []
    for y in range(len(tree_grid)):
        for x in range(len(tree_grid[0])):
            tree = tree_at(tree_grid, x, y)
            number_of_trees_visible_from_top = find_number_of_trees_visible_from_top(tree_grid, tree, x, y)
            number_of_trees_visible_from_bottom = find_number_of_trees_visible_from_bottom(tree_grid, tree, x, y)
            number_of_trees_visible_from_left = find_number_of_trees_visible_from_left(tree_grid, tree, x, y)
            number_of_trees_visible_from_right = find_number_of_trees_visible_from_right(tree_grid, tree, x, y)
            scenic_score = (
                number_of_trees_visible_from_top *
                number_of_trees_visible_from_bottom *
                number_of_trees_visible_from_left *
                number_of_trees_visible_from_right
            )
            scenic_scores.append(scenic_score)
    print(max(scenic_scores))
