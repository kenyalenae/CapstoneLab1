# Guess the number game
import random

guessesTaken = 0

print('Hello,  what is your name?')  # ask user their name
userName = input()

number = random.randint(1, 10)
print(userName + ', I am thinking of a number between 1 and 10.')

# create loop for user to guess up to six times on number
while guessesTaken < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

# if user guesses correctly print good job message
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + userName + '! You guessed my number in ' + guessesTaken + ' guesses!')

# if user guesses wrong all six times, tell them they're wrong and what number it was
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)





