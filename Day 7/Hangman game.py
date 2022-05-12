import random
import hangman_art
import hangman_words
stages = hangman_art.stages
word_list = hangman_words.word_list
Game_Complete = False
Blank_Chosen_Word = []
chosen_word = random.choice(word_list)
Letters_Guessed = len(chosen_word)
for i in range(0,len(chosen_word)):
    Blank_Chosen_Word += "_"

lives = 6

print(hangman_art.logo)
while not Game_Complete:
    guess = input("Guess a letter : ").lower()
    temp = Letters_Guessed
    for i in range(0,len(chosen_word)):
        if guess == chosen_word[i]:
            Blank_Chosen_Word[i] = guess
            Letters_Guessed -= 1
    if temp != Letters_Guessed:
        print("Correct guess ")  
    else:
        print("Incorrect guess ")  
        lives  -= 1
        print(stages[lives])    
    print(Blank_Chosen_Word)

    if Letters_Guessed == 0 :
        Game_Complete = True
        print("You WIN")
    elif lives == 0:
        Game_Complete = True
        print("You Lose")


