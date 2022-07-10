import art
import random

print(art.logo)

num_to_guess = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
  num_of_lives = 10
elif difficulty == 'hard':
  num_of_lives = 5
else:
  print("Not a difficulty level.")

while num_of_lives > 0:
  user_guess = int(input("Make a guess: "))
  if user_guess > num_to_guess:
    print("Too high.")
    num_of_lives -= 1
  elif user_guess < num_to_guess:
    print("Too low.")
    num_of_lives -= 1
  else:
    print("You got it right!")
    break

if num_of_lives == 0:
  print("You've run out of guesses. You lose.")
  print(f"The number was: {num_to_guess}")