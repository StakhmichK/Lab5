import math
numbers = input("Enter x1, y1, x2, y2 separated by a space: ").split()
if len(numbers) != 4:
    print("Error: You must enter exactly 4 numbers!")
else: 
     x1, y1, x2, y2 = map(int, numbers)
     dis = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The distance is: {dis:.2f}")