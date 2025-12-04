with open("input.txt", "r") as file:
    banks = [line for line in file.read().split("\n") if line.strip() != ""]

result = 0

for bank in banks:
    digit_indices = []
    while len(digit_indices) < 12:
        search_start = 0 if len(digit_indices) == 0 else digit_indices[-1] + 1
        search_end = len(bank) - 11 + len(digit_indices)

        for i in range(9, 0, -1):
            try:
                digit_indices.append(bank[search_start:search_end].index(str(i)) + search_start)
                break
            except ValueError:
                continue
    result += int("".join([bank[index] for index in digit_indices]))

print(result)