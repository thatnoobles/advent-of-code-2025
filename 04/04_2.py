def get_num_adjacent(grid: list[str], x: int, y: int):
    result = 0
    x_bound = len(grid[y]) - 1
    y_bound = len(grid) - 1

    if x < x_bound:
        result += 1 if grid[y][x + 1] == "@" else 0
    if x > 0:
        result += 1 if grid[y][x - 1] == "@" else 0
    if y < y_bound:
        result += 1 if grid[y + 1][x] == "@" else 0
    if y > 0:
        result += 1 if grid[y - 1][x] == "@" else 0
    if x > 0 and y > 0:
        result += 1 if grid[y - 1][x - 1] == "@" else 0
    if x < x_bound and y < y_bound:
        result += 1 if grid[y + 1][x + 1] == "@" else 0
    if x > 0 and y < y_bound:
        result += 1 if grid[y + 1][x - 1] == "@" else 0
    if x < x_bound and y > 0:
        result += 1 if grid[y - 1][x + 1] == "@" else 0
    
    return result


def get_accessible_rolls(grid: list[str]):
    result = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == ".":
                continue
            if get_num_adjacent(grid, x, y) < 4:
                result.append((x, y))
    return result


def remove_rolls(grid: list[str], rolls: list[tuple]):
    result = []
    for y in range(len(grid)):
        new_row = ""
        for x in range(len(grid[y])):
            if grid[y][x] == "." or (x, y) in rolls:
                new_row += "."
            else:
                new_row += "@"
        result.append(new_row)
    return result



with open("input.txt", "r") as file:
    rows = [l.strip() for l in file.readlines()]

total_removed = 0

while len(get_accessible_rolls(rows)) > 0:
    accessible_rolls = get_accessible_rolls(rows)
    total_removed += len(accessible_rolls)
    rows = remove_rolls(rows, accessible_rolls)
        
print(total_removed)