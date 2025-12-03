import math

ids = set()

with open("input.txt", "r") as file:
    ranges = file.read().split(",")
    for r in ranges:
        lower = int(r.split("-")[0])
        upper = int(r.split("-")[1])
        ids = ids.union(set(range(lower, upper + 1)))

# Splitting by a pattern that makes up a whole string
# (e.g. "abcabcabc".split("abc")) will produce a list of
# empty strings.
result = 0

for id in sorted(list(ids)):
    str_id = str(id)
    
    for i in range(1, len(str_id)):
        if len([x for x in str_id.split(str_id[:i]) if x != ""]) == 0:
            result += id
            break

print(result)