import random

def guess_random_number(tries, start, stop):
    number_to_guess = random.randint(start, stop)
    while tries != 0:
        print(f"Tries remaining: {tries}")
        guess = int(input(f"Guess a number between {start} and {stop}: "))
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
            return


guess_random_number_linear(5, 0, 10)

# guess_random_number(5, 1, 100)
