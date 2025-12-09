import re

with open("input.txt", "r") as file:
    lines = [re.split(r"\s+", l.strip()) for l in file.readlines()]

expressions = []
for x in range(len(lines[0])):
    exp = ""

    for y in range(len(lines) - 1):
        exp += f"{lines[y][x]} {lines[len(lines) - 1][x] if y < len(lines) - 2 else ''} "
    expressions.append(exp.strip())

result = 0
for exp in expressions:
    result += eval(exp)

print(result)