# Write your code here
import random

print("H A N G M A N\n")
print('Type "play" to play the game, "exit" to quit:')
while input() == 'play':
    word_bank = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(word_bank)
    dash_string = len(word) * '-'
    dash_list = list(dash_string)

    lives = 8
    used = set()
    while True:
        print(''.join(dash_list))
        correct = ''.join(dash_list)
        if correct == word:
            print("You guessed the word!\nYou survived!")
            break

        letter = input('Input a letter: ')
        if not letter.isalpha() or not letter.islower() or len(letter) != 1:
            if len(letter) != 1:
                print("You should input a single letter")
            else:
                print("Please enter a lowercase English letter")

        elif letter in used and letter not in word:
            print("You've already guessed this letter")

        elif letter in word:
            for letter_index in range(len(word)):
                if word[letter_index] == letter:
                    dash_list[letter_index] = letter
                    if letter in used:
                        print("You've already guessed this letter")
            used.add(letter)
        else:
            if letter in used:
                print("You've already guessed this letter")
            else:
                lives -= 1
                print("That letter doesn't appear in the word")
                used.add(letter)
                if lives == 0:
                    break
        print()
    if lives == 0:
        print("You lost!")
