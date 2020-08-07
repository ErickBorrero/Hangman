import random

word_bank = ['mighty', 'eggs', 'jog', 'jelly', 'interfere', 'furniture', 'knowledge', 'acoustic', 'beneficial',
             'disarm', 'screw', 'work', 'voiceless', 'lame', 'mend', 'cautious', 'employ', 'nappy', 'brash',
             'unnatural', 'stuff', 'earth', 'complex', 'arithmetic', 'colour', 'ethereal', 'apparel', 'little',
             'therapeutic', 'lush', 'soak', 'tent', 'languid', 'eggnog', 'juicy', 'idea', 'quaint', 'record', 'tiny',
             'jittery', 'remarkable', 'drag', 'laborer', 'whirl', 'back', 'bumpy', 'join']

chances = 6
guessing_word = random.choice(word_bank)
underlines = ['_'] * len(guessing_word)
print(*underlines, sep=" ")
letter_guess = input('Choose a letter: ')

while chances >= 1:
    if letter_guess == '':
        letter_guess = input('Field cannot be blank. Choose a letter: ')
    if letter_guess in guessing_word:
        index = 0
        while index < len(guessing_word):
            index = guessing_word.find(letter_guess, index)
            if index == -1:
                break
            underlines.pop(index)
            underlines.insert(index, letter_guess)
            index += 1
        print(*underlines, sep=" ")
        if '_' not in underlines:
            print('')
            print("Congratulations! You're a winner!")
            quit()
        letter_guess = input('Very nice! Choose a letter: ')
    else:
        chances -= 1
        print(*underlines, sep=" ")
        letter_guess = input(f'Sorry, no go. You have {chances} remaining. Try again: ')
else:
    print(f'\nThe word was {guessing_word}')
    print("You've been lynched, better luck next time.")
