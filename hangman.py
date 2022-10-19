import random, time, os
print("HANGMAN\n")

wordList = ["BRAILLE", "VISION", "CODE", "SUBROUTINE", "DANCE", "LIBRARY", "SUMMER", "MOUNTAIN", "PYTHON", "CHALLENGE"]
word = random.choice(wordList)
temp_word = "_" * len(word)
print(f'''
{temp_word}

  +---+
  |   |
      |
      |
      |
      |
=========
''')

letterPicked = []
lives = 6


while True:
  letter = input("Choose a letter: ").upper()
  
  if letter in letterPicked:
    print("\nYou've tried that one before!\n")
    continue
  
  letterPicked.append(letter)
  
  if letter in word:
    print("You found a letter!\n")
  else:
    print("Nope, not in there!\n")
    lives -= 1
  
  time.sleep(2)
  os.system("cls")
  print("HANGMAN\n")
  
  allLetters = True
  print()
  for i in word:
    if i in letterPicked:
      print(i, end="")
    else:
      print("_", end="")
      allLetters = False
  print()

  if allLetters:
    print(f'''          
  O  
 /|\ 
 / \   
 
    You won with {lives} lives left
    ''')
    break
  
  if lives <= 0:
    print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
    ''')
    print(f"You ran out of lives!\n The answer was {word}")
    break
  elif lives == 6:
    print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
    print("You have 6 lives left")
  elif lives == 5:
    print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
    print("You have 5 lives left")
  elif lives == 4:
    print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
    print("You have 4 lives left")
  elif lives == 3:
    print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
    print("You have 3 lives left")
  elif lives == 2:
    print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
    print("You have 2 lives left")
  elif lives == 1:
    print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
    print("You have 1 life left")
  