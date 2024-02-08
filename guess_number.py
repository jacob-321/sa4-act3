number = 10
guesses = 3
print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

while True:
    if guess == number:
        print("Congratulations! You guessed the right number.")
    else:
        guesses -= 1
        print(f"Sorry! The number was {number}. You have {guesses} guesses left.")
        if guesses == 0:
            break
        choice = input("Would you like to continue? (Insert 'q' to quit):  ")
        if guess == "q":
            break
    guess = int(input("What number am I thinking of? "))
