#This code makes a dictionary of NATO phonetic alphabet
#and then asks the user to enter a word and prints the phonetic alphabet for that word
import pandas as pd
data = pd.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()

#TODO 3. Print the output.

