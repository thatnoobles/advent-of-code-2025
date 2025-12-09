def get_num_for_col(lines: list[str], col: int) -> int:
    result = ""
    for i in range(len(lines) - 1):
        result += lines[i][col] if lines[i][col] != " " else ""
    
    return int(result) if result != "" else 0


with open("input.txt", "r") as file:
    lines = [f" {line}" for line in file.read().split("\n")]

result = 0
operands = []

for i in range(-1, -len(lines[-1]) - 1, -1):
    operand = get_num_for_col(lines, i)
    
    if operand == 0:
        expression = f" {lines[-1][i + 1]} ".join([str(op) for op in operands])
        result += eval(expression)
        operands.clear()
    else:
        operands.append(operand)

print(result)