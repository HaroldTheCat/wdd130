
hidden_word='corn'
attempt = 6
print('Time to guess the Grass! I mean word!')

while attempt > 0:
    guess = str(input("Guess the word: "))
    if guess == hidden_word:
      print("You guessed the words correctly!")
      print('It took you {attempt}')
      break 
    else:
      attempt = attempt - 1
      print(f"you have {attempt} attempt(s) ,, \n ")
      for char, word in zip(hidden_word, guess):
            if word in hidden_word and word in char:
                print(word)
            elif word in hidden_word:
                print(word + " ➕ ")
            else:
                print(" _ ")
      if attempt == 0:
        print("Game over!")