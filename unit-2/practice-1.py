alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
    "w", "x", "y", "z"]
position = ""

string = input ('What would you like to "Encrypt": ')
index = 0
for letter in list(string):
    index += 1
    if letter in alphabet:
        alpha_numer = alphabet.index(letter)
        position = position + str(alpha_numer)
              
print (position)