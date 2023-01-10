import random
from wordList import word_list

display = []
display_hangman = ['---\n',' | \n',' O \n','/','|','\\\n','/',' \\']
hangman = ""
life = 7

chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')

for n in range(0,len(chosen_word)):
    display.append('_')

while True:
    
    guess = input("Guess a letter: ").lower()
    
    if guess in chosen_word:    
        for n in range(len(chosen_word)):
            if chosen_word[n] == guess:
                display[n] = guess
    else:
        life -= 1
        for n in range(len(display_hangman)-life):
            hangman += display_hangman[n]
        print(hangman)
        hangman = ""
        if life == 0:
            break
        
    if not '_' in display:
        break;
    
    print(display)  

print(display)
print("Life:",life)
print("Game Over")