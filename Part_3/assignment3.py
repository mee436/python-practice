print("Here we are creating the calculator so you need to add 2 numbers and an operator")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operatorr = input("Enter the operator you want to use (+, -, *, /): ")

if operatorr == '+':
    print("Your Addition is: ", a+b)

elif operatorr == '-':
    print("Your Subtraction is: ", a-b)

elif operatorr == '*':
    print("Your Multiplication is: ", a*b)

elif operatorr == '/':
    print("Your Division would be: ", a/b)

else:
    print("The operator you have entered is wrong. Please check and try once again. Have a great day!")
