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


with open("input.txt", "r") as file:
    rows = [l.strip() for l in file.readlines()]

accessible_rolls = 0

for y in range(len(rows)):
    for x in range(len(rows[y])):
        if rows[y][x] == ".":
            continue
        accessible_rolls += 1 if get_num_adjacent(rows, x, y) < 4 else 0
        
print(accessible_rolls)