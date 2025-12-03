ids = set()

with open("input.txt", "r") as file:
    ranges = file.read().split(",")
    for r in ranges:
        lower = int(r.split("-")[0])
        upper = int(r.split("-")[1])
        ids = ids.union(set(range(lower, upper + 1)))

# An ID is invalid if it's a pattern repeating twice -
# i.e. we can split it in half and the halves are equal
result = 0

for id in ids:
    str_id = str(id)
    if str_id[: len(str_id) // 2] == str_id[len(str_id) // 2 :]:
        result += id

print(result)