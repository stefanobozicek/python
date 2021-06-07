wlc = "welcome to the game Guess the secret number. It is a question for 1 million dollars!"
secret = int("26")

print(wlc)

guess = int(input("guess the number!"))

if  guess == secret:
    print("Congrats! YOU WON 1,0000,0000 USD!")
else:
    print("Try your luck next time!")


