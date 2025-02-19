import random


level = ""


def greeting():
   """Prompt for the beginning of the game and level selection """
   print("Welcome to the Game!\nI'm thinking of a number between 10 and 100")
   global level
   level  = input("Choose a difficulty level. Type 'easy' of 'hard': ").lower()


greeting()




def easy_level():
   """Guessing option if the level chosen is easy The user will be given 10 attempts to choose given number"""
   attempts = 10
   guessed_number =random.randint(1, 100)
   #print(guessed_number)


   #create a loop that goes until attempt is = 0


   while attempts != 0:
       print(f"You have {attempts} attempts remaining to guess the number.")
       attempt_made = int(input("Make a guess: "))
       if attempt_made == guessed_number:
           print("You got it! The answer was 100")
       elif attempt_made != guessed_number:
           if attempt_made > guessed_number:
               print("Too high")
           elif attempt_made < guessed_number:
               print("Too low")
           print("Guess again")
           attempts -=1


       if attempts == 0:
           print(f"You have ran out of attempts. The correct number is {guessed_number}")


def hard_level():
   """Guessing option if the level chosen is hard The user will be given 10 attempts to choose given number"""
   attempts = 4
   guessed_number =random.randint(1, 100)
   print(guessed_number)


   #create a loop that goes until attempt is = 0


   while attempts != 0:
       print(f"You have {attempts} attempts remaining to guess the number.")
       attempt_made = int(input("Make a guess: "))
       if attempt_made == guessed_number:
           print("You got it! The answer was 100")
           
       elif attempt_made != guessed_number:
           if attempt_made > guessed_number:
               print("Too high")
           elif attempt_made < guessed_number:
               print("Too low")
           if attempts >0:
               print("Guess again")
           attempts -=1


       if attempts == 0:
           print(f"You have ran out of attempts. The correct number is {guessed_number}")


if level == "easy":
   easy_level()


if level == "hard":
   hard_level()

