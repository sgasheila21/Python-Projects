import random

while True:
    secret_number = random.randint(0, 100)
    guess_number = None
    attempts = 0

    while guess_number != secret_number:
        guess_number = input("Enter the number you guessed [0-100]: ")
        try:
            guess_number = int(guess_number)
        except ValueError:
            print("Invalid number. Please try again!")
            continue

        if guess_number < 0 or guess_number > 100:
            print("Please enter a number between 0 - 100!")
            continue

        attempts += 1
        if guess_number < secret_number:
            print("Too low.", end=" ")
        elif guess_number > secret_number:
            print("Too high.", end=" ")

        if abs(guess_number - secret_number) <= 5 and guess_number != secret_number:
            print("You are very close!")
        elif guess_number != secret_number:
            print("Please try again!")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break

    while True:
        again = input(
            "Do you want to replay the game? (y/n): ").strip().lower()
        if again in ['y', 'n']:
            break
        else:
            print("Invalid input! Please enter 'y' or 'n'.")

    if again == 'n':
        print("Goodbye")
        break
