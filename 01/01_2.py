def wrap(position: int) -> int:
    if position < 0:
        return 99
    elif position > 99:
        return 0
    else:
        return position


with open("input.txt", "r") as file:
    lines = file.read().split("\n")

position = 50
password = 0

for line in lines:
    if line.strip() == "":
        continue

    offset = int(line[1:])
    direction = 1 if line[0] == "R" else -1

    # this is probably the worst way to do this but i might go back
    # and make it better later
    for i in range(offset):
        position = wrap(position + direction)
        if position == 0:
            password += 1
            
print(password)