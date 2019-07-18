import random

mysterio = random.randint(1,10000)
print("A number has been generated from 1 to 10,000.")
guess = 0.0
while guess != mysterio:
    guess = 0.0
    while type(guess) != int:
        try:
            guess = input("Please place your guess: ")
            guess = int(guess.replace(',', ''))
        except ValueError:
            print ("That is not an integer.")

    if guess <= 0:
        print ("That shit is 0 or a negative number man. Guess from 1 to 10,000")
    elif guess > 10000:
        print ("That is above 10,000. Guess again.")
    elif guess < mysterio and guess > 0:
        print ("That shit is too small. Guess bigger")
    elif guess > mysterio and guess < 10000:
        print ("That shit was too big. Guess Smaller.")

print ("You guessed right!")