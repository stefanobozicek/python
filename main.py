wlc = "Welcome to the kilometers to miles converter!"

while (True):
    try:
        distance = float(input("Enter a Number: "))
        break
    except ValueError:
        print("Invalid number")

print("{:0.3f}".format(distance * 0.621371) + str(" miles"))