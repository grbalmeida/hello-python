secret_word = 'perfume'
typed_letters = []
chances = 3

while True:
  if chances <= 0:
    print('You lost')
    break

  letter = input('Enter a letter: ')

  if len(letter) > 1:
    print('Enter only one letter')
    continue

  typed_letters.append(letter)
  
  if letter in secret_word:
    print(f'The letter {letter} exists in the secret word')
  else:
    print(f'The letter {letter} doest not exist in the secret word')
    typed_letters.pop()

  temporary_secret_word = ''

  for secret_letter in secret_word:
    if secret_letter in typed_letters:
      temporary_secret_word += secret_letter
    else:
      temporary_secret_word += '*'
  
  if temporary_secret_word == secret_word:
    print(f'The secret word is {secret_word}. You won the game')
    break
  else:
    print(f'Almost there. This is the secret word: {temporary_secret_word}')

  if not letter in secret_word:
    chances -= 1

  print(f'You still have {chances} chances')