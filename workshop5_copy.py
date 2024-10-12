import random

def guess_random_number(tries, start, stop):
    number_to_guess = random.randint(start, stop)
    print(f"The nu")
    while tries != 0:
        print(f"Tries remaining: {tries}")

        # Input validation to ensure the guess is an integer within the given range
        while True:
            try:
                guess = int(input(f"Guess a number between {start} and {stop}: "))
                if start <= guess <= stop:
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
    print(f"The number to guess is: {number_to_guess}")
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
    print(f"Random number to guess is: {number_to_guess}")
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





#guess_random_num_binary(5, 0, 100)

#guess_random_number_linear(5, 0, 10)

guess_random_number(5, 1, 100)
