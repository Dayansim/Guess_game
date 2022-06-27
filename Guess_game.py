import time
import random

def get_guess():
  guess = int(input('take your guess:'))
  return guess
def play_again():
  answer = input('Play again? Y/N ')
  return answer == 'Y' or answer == 'y'
def guess_game():
  count = 0
  number = random.randint(1,20)
  name = input('What is your name? ')
  print('well, ' + name + ', i am thinking of a number from 1 to 20')
  print('Take a guess: ')
  while count < 6:
    #count += 1
    count = count + 1
    print(count)
    guess = get_guess()
    if guess == number:
      print(f'good job {name}, you guessed the number within {count} guesses !')
      break
    elif guess > number:
      print('your guess is to high')
    elif guess < number:
      print('your guess is to low')
    time.sleep(1)

  if count == 6 and guess != number:
    print(f'you were not successful =( the number is {number}')

while True:
  guess_game()
  if not play_again():
    break
