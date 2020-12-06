import random

print('Hello! What is your name?')
name = input()
print('Well, ' + name + ' I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1, 20)

for guessTaken in range(1, 7):
    print('Take a guess!')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low!')
    elif guess > secretNumber:
        print('Your guess is too high!')
    else:
        break

if guess == secretNumber and guessTaken == 1:
    print('Excellent, ' + name + '! You guessed my number in 1 guess!')
elif guess == secretNumber and guessTaken > 1:
    print('Nice, ' + name + '! You guessed my number in ' + str(guessTaken) + 'guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(guess) + '.')

