#Homework optional problem #5

def letter_count (word):
    count = {}
    for l in word:
        count[l] = count.get (l,0) +1
    return count


def possible_word (word_list, char_list):
    #which words in word list can be formed from the characters in the character list

    #iterate over word_list
    valid_words=[]
    for word in word_list:
        is_word_valid = True
        #get a count of each character in word
        char_count = letter_count(word)
        #check each character in the word
        for letter in word:
            if letter not in char_list:
               is_word_valid = False
            else:
                if char_list.count(letter) != char_count [letter]:
                    is_word_valid = False

    #Add valid words to a list 
        if is_word_valid:
            valid_words.append (word)
    return valid_words

#testing

legal_words = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
letters = ['e', 'o', 'b', 'a', 'm', 'g', 'l']

print (possible_word(legal_words,letters))