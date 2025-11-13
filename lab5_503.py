roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
roman = input("Enter the roman number: ")
symbols = list(roman)
total = 0
for i in range(len(symbols)):
    if i + 1 < len(symbols) and \
    roman_values[symbols[i]] < roman_values[symbols[i + 1]]:
        total -= roman_values[symbols[i]]
    else:
        total += roman_values[symbols[i]]
print(total)