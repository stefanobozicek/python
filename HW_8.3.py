first_num = int(input("Enter the first number: "))

operation = input("Enter which operation parameter to use (+ - / *)")

second_num = int(input("Enter the second number: "))

if operation == "+":
    print(first_num + second_num)

elif operation == "-":
    print(first_num - second_num)

elif operation == "/":
    print(first_num / second_num)

elif operation == "*":
    print(first_num * second_num)

else:
    print("something went wrong.")