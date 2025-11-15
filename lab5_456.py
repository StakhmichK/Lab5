binary_numbers = input("Enter 4-digit binary numbers\
separated by commas: ").split(',')
divisible_by_5 = []
for b in binary_numbers:
     decimal_value = int(b, 2)
     if decimal_value % 5 == 0:
        divisible_by_5.append(b)
print(','.join(divisible_by_5))