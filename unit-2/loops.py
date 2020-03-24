'''
num = 5

while num < 10:
    print ("Yeah")
    num += 1
'''

'''

secret = 7

guess = int(input ("What is the secret value: "))

while guess != secret:
    
    guess = int(input ("Wrong! Guess again! "))

print ("You got it!")

'''
#check if a string is a palindrome
#same forwards and backwards 

string = input ("Type in the string you'd like to check ")
index = len(string) -1
reversed_string = ""
while index >=0:
    reversed_string += string[index]
    index -= 1

if string == reversed_string:
    print ("The string is a palindrome")
else:
    print ("The string is not a palindrome")

