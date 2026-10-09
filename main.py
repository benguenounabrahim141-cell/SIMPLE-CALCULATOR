print(" simple calculator")
num1 = float(input("enter the first number:"))
operator = input("enter an operation(+,-,*, /):"
                 num2 = float(input "enter the second number:"))
if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        result = None
        print("error: cannot divide by zero")
        else:
result = None
print("invalid operation !")
if result is not None:
    print("result:", result)
