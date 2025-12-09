with open("input.txt", "r") as file:
    content = file.read()
    ranges = content.split("\n\n")[0].split("\n")
    ids = [int(id) for id in content.split("\n\n")[1].split("\n") if id != ""]

result = 0
for id in ids:
    for fresh_range in ranges:
        line_split = fresh_range.split("-")
        if id >= int(line_split[0]) and id <= int(line_split[1]):
            result += 1 
            break

print(result)