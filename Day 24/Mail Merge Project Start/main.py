#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("C:\\Users\\FiercePC\\Documents\\GitHub\\100-Days-of-Code-Challange\\Day 24\\Mail Merge Project Start\\Input\\Names\\invited_names.txt") as names:
    names = names.readlines()
    print(names)

Names_Cleaned = []
for name in names:
    Names_Cleaned.append(name.strip())


with open("C:\\Users\\FiercePC\\Documents\\GitHub\\100-Days-of-Code-Challange\\Day 24\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt") as letter:
    letter = letter.read()
    print(letter)

for name in Names_Cleaned:
    new_letter = letter.replace("[name]", name)
    with open(f"C:\\Users\\FiercePC\\Documents\\GitHub\\100-Days-of-Code-Challange\\Day 24\\Mail Merge Project Start\\Output\\ReadyToSend\\letter_for_{name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)