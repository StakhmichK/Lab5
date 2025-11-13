numbers = list(map(int, input("Enter digits \
separated by spaces: ").split()))
n = int(input("Enter the number to determine the amount: "))
count_n = numbers.count(n)
print(f"Number {n} occurs {count_n} times.")