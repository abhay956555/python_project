num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
op = input("Enter operator (+,-,*,/) : ")

if op == "+":
    print("Result =", num1 + num2 )
elif op == "-":
    print("Result =", num1 - num2 )

elif op =="/":
    print("Result =", num1 / num2 )

elif op == "*":
    print("Result =", num1 * num2 )

elif op == "/":
    if num2 != 0:

        print("REsult =", num1 / num2)

    else:
        print("cannot divided by zero")

    else:
print("Invalid operator")s