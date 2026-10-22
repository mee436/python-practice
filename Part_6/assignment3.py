def check_prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

num = int(input("Enter a number"))
check_prime_number(num)