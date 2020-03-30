#Problem 1

def letter_count (string, letter):
    count = 0
    for index in range(len(string)):
        if string [index] == letter:
            count += 1
    return count


print (letter_count("aaaabcde","a"))

#Problem 2

def count_words (string):
    word_count = 1
    index = 0
    while index < len(string):
        if string [index] == " ":
            word_count += 1
        index += 1
    return word_count

print (count_words("I'm staying home because of the epidemic"))

#Problem 3

def reverse_list (old_list):
    new_list = []
    for item in old_list:
        new_list.insert(0,item)

    return new_list

print (reverse_list(["This", "is", "cool"]))    

#Problem 4

def split_list (integer_list,integer):
    list_1 = []
    list_2 = []
    for item in integer_list:
        if item < integer:
            list_1.append(item)
        if item >= integer:
            list_2.append(item)
    return list_1,list_2

print (split_list([4, 5, 11, 8, 19], 10))

#Problem 5

def is_isogram (string):
    index = 0

    while index < len(string):
        if string [index] == string [index+1]:
            result = "False"
        else:
            result = "True"
    index + 1
    return result

print (is_isogram("abc"))