with open("input.txt", "r") as file:
    lines = file.read().split("\n")

position = 50
password = 0

for line in lines:
    if line.strip() == "":
        continue

    position = (position + int(line[1:]) * (1 if line[0] == "R" else -1)) % 100

    if position == 0:
        password += 1

print(password)