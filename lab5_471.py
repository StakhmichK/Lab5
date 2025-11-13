nums = input("Enter the numbers: ")
numbers = []

for x in nums.split():
    numbers.append(int(x))

positives = []
negatives = []
for num in numbers:
    if num > 0:
        positives.append(num)
    elif num < 0:
        negatives.append(num)

positives.sort(reverse=True)
negatives.sort(reverse=True)

result = positives + negatives
print(*result)