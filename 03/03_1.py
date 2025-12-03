with open("input.txt", "r") as file:
    banks = file.read().split("\n")

result = 0

for bank in banks:
    # The HIGH digit is the first occurrence of the highest
    # digit in the bank
    digit_high = 0
    for i in range(9, 0, -1):
        try:
            digit_high_index = bank.index(str(i))
            digit_high = int(bank[digit_high_index])
            
            if digit_high_index != len(bank) - 1:
                break
        except ValueError:
            continue

    # The LOW digit is the highest digit after the high digit
    digit_low = 0
    for digit in bank[digit_high_index + 1:]:
        if int(digit) > digit_low or digit == "9":
            digit_low = int(digit)
    result += digit_high * 10 + digit_low

print(result)