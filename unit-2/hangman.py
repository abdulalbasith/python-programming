import random
list_of_words = ["south", "ocean", "water", "canada", "virus"]
max_number_of_guesses = 5

def HangmangameSol1():
    current_number_of_guesses = 0
    current_word = random.choice(list_of_words)
    guessed_letters = ""
    for index in range(len(current_word)):
        guessed_letters += "_"
    while current_number_of_guesses < max_number_of_guesses:
        print (guessed_letters)
        guess = input ("What is your guess ")
    #correct guesses        
        if guess in current_word:
            new_guessed_letters = ""
            for index in range (len(current_word)):
                if current_word[index] == guess:
                    new_guessed_letters += guess
                else:
                    new_guessed_letters += guessed_letters [index]
            guessed_letters = new_guessed_letters
        else:
            current_number_of_guesses += 1
            print (f"You have {max_number_of_guesses - current_number_of_guesses} guesses left, try again")
        if guessed_letters == current_word:
            print ("You win!")
            break
    if current_number_of_guesses == max_number_of_guesses:
        print ("You lose!")


def HangmangameSol2():
    current_number_of_guesses = 0
    current_word = random.choice(list_of_words)
    guessed_letters = []
    for index in range(len(current_word)):
        guessed_letters.append ("_")
    

    while current_number_of_guesses < max_number_of_guesses:
        print (guessed_letters)
        guess = input ("What is your guess? ")
      
        if guess in current_word:

            for index in range (len(current_word)):
                if current_word[index] == guess:

                     guessed_letters [index] = guess
        else:
            current_number_of_guesses += 1 
            print (f"You have {max_number_of_guesses - current_number_of_guesses} guesses left, try again")
        if "_" not in guessed_letters:
            print ("You win!")
            break
    if current_number_of_guesses == max_number_of_guesses:
        print (f"You lose!, the word was {current_word}")

HangmangameSol2()
