import random


def guess_random_number(tries, start, stop):
    number_to_guess = random.randint(start, stop)
    print(f"The random number to guess is: {number_to_guess}")

    guessed_numbers = set()

    while tries != 0:
        print(f"Tries remaining: {tries}")

        while True:
            try:
                guess = int(input(f"Guess a number between {start} and {stop}: "))
                if guess in guessed_numbers:
                    print("You've already guessed that number! Try again.")
                    continue

                if start <= guess <= stop:
                    guessed_numbers.add(guess)
                    break
                else:
                    print(f"Please enter a number between {start} and {stop}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        if guess < number_to_guess:
            print("Guess Higher!")
        elif guess > number_to_guess:
            print("Guess Lower!")
        else:
            print("You guessed it!")
            return

        tries -= 1

    print("Sorry, you ran out of tries. The number was", number_to_guess)


def guess_random_number_linear(tries, start, stop):
    number_to_guess = random.randint(start, stop)
    print(f"The random number to guess is: {number_to_guess}")
    for i in range(start, stop + 1):
        tries -= 1
        print(f"Tries remaining: {tries}")
        print(f"Guess the number: {i}")
        if tries == 0:
            print("Sorry, you ran out of tries. The number was", number_to_guess)
            return
        if i == number_to_guess:
            print("You guessed it!")

def guess_random_num_binary(tries, start, stop):
    number_to_guess = random.randint(start, stop)
    print(f"The random number to guess is: {number_to_guess}")
    low = start
    high = stop
    while tries != 0:
        print(f"Tries remaining: {tries}")
        guess = (low + high) // 2
        print(f"Guess the number: {guess}")
        if guess < number_to_guess:
            print("Guess Higher!")
            low = guess + 1
        elif guess > number_to_guess:
            print("Guess Lower!")
            high = guess - 1
        else:
            print("You guessed it!")
            return
        tries -= 1
    print("Sorry, you ran out of tries. The number was", number_to_guess)

def play_guessing_game():
    while True:
        try:
            tries = int(input("Enter the number of tries: "))
            start = int(input("Enter the start of the range: "))
            stop = int(input("Enter the end of the range: "))
            if start < stop:
                break
            else:
                print("The start of the range must be less than the stop.")
        except ValueError:
            print("Please enter valid integers for tries, start, and stop.")

    print("\nChoose the guessing method:")
    print("1. Manual guess")
    print("2. Linear search")
    print("3. Binary search")

    while True:
        try:
            choice = int(input("Enter your choice (1, 2, or 3): "))
            if choice in [1, 2, 3]:
                break
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if choice == 1:
        guess_random_number(tries, start, stop)
    elif choice == 2:
        guess_random_number_linear(tries, start, stop)
    elif choice == 3:
        guess_random_num_binary(tries, start, stop)


# guess_random_num_binary(5, 0, 100)

# guess_random_number_linear(5, 0, 10)

#guess_random_number(5, 1, 100)

play_guessing_game()
