print("This Program will help you in Finding the Factorial of a Number.")
Number = int(input("Enter the Number: "))
Variable = 2
Factorial = 2

while True:
    if Variable < Number:
        Variable = Variable + 1
        Factorial = Factorial * Variable

    elif Variable >= Number:
        break


print()
print("The Factorial of", Number, "is", Factorial)
