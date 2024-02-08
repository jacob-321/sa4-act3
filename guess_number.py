number = 5
choice = ""

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

while True or (choice == "q"):
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break

    elif guess > number:
        print("You're guess was too high!")

    elif guess < number:
        print("You're guess was too low!")

    else:
        print(f"Sorry! The number was {number}.")
    choice = input("Would you like to continue? (Insert 'q' to quit): ")
    if choice == "q":
        break
    guess = int(input("What number am I thinking of? "))

