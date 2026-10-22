a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

for i in range(1, 1001):
    if i % a == 0 and i % b == 0:
        print("first number is that can divide both is", i)
        break