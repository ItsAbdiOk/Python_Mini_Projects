from collections import deque
import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Caesar(direction,Text,shift):
    Shifted = deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    if direction == "encode":
        shift *= -1
    Shifted.rotate(shift)
    for i in range(0,len(Text)):
        if Text[i] in alphabet :
            temp = alphabet.index(Text[i])
            Text [i] = Shifted[temp]
    print("".join(Text))
    
Game = True
while Game == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    Text = list(input("Type your message:\n").lower())
    shift = int(input("Type the shift number:\n"))
    Caesar(direction,Text,shift)
    Again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if Again != "yes":
        print("Good Bye")
        Game = False