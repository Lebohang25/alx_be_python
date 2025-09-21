number = int(input("Enter a number to see its multiplication table: "))

for i in range(0, 11):
    result = number * i
    print(f"{number} * {i} = {result}")
