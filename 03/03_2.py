with open("input.txt", "r") as file:
    banks = file.read().split("\n")

result = 0

for bank in banks:
    # The HIGH digit is the first occurrence of the highest
    # digit in the bank
    digit_high = 0
    for i in range(9, 0, -1):
        try:
            # If our highest digit is within the last 12 chars of the
            # string, it doesn't matter b/c the number wouldn't fit
            digit_high_index = bank[:-12].index(str(i))
            digit_high = int(bank[digit_high_index])
            
            if digit_high_index != len(bank) - 12:
                break
        except ValueError:
            continue
    print(digit_high)

print(result)