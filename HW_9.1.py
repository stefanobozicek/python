wlc = "Welcome to the kilometers to miles converter!"

while True:
    distance = float(input("Enter the distance in kilometers: "))
    print("{:0.3f}".format(distance * 0.621371) + " miles")

    again = str(input("Do you want to do another calculation? If yes, type 'YES'."))

    if again == "YES":
        distance = float(input("Enter the distance in kilometers: "))
        print("{:0.3f}".format(distance * 0.621371) + " miles")
        print("Goodbye!")
    else:
        print("Goodbye!")
    break
