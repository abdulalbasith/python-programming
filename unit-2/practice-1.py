alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
    "w", "x", "y", "z"]
position = []

string = input ('What would you like to "Encrypt": ')
index = 0
for letter in list(string.lower()):
    if letter in alphabet:
        alpha_number = alphabet.index(letter) + 1 
        position = position.append(alpha_number)
        #position = position.split("").join(" ")      
print (position)

