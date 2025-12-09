def in_range(x: int, low: int, high: int) -> bool:
    return x >= low and x <= high


def count_symmetric_difference(ranges: list[tuple[int, int]], low: int, high: int) -> int:
    for rng in ranges:
        # [low, high] is fully consumed by an existing range
        if high - low <= 0:
            return 0

        # [low, high] overlaps the current range on the high end
        if in_range(low, rng[0], rng[1]):
            low = rng[1] + 1

        # [low, high] overlaps the current range on the low end
        if in_range(high, rng[0], rng[1]):
            high = rng[0] - 1

    return high - low + 1


with open("input.txt", "r") as file:
    content = file.read()
    ranges = [(int(line.split("-")[0]), int(line.split("-")[1])) for line in content.split("\n\n")[0].split("\n")]

ranges.sort(key=lambda x: x[0] - x[1])

result = 0
checked_ranges = []
for rng in ranges:
    result += count_symmetric_difference(checked_ranges, rng[0], rng[1])
    checked_ranges.append(rng)

print(result)