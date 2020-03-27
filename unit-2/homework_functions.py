#Problem 1

def letter_count (string, letter):
    count = 0
    for index in range(len(string)):
        if string [index] == letter:
            count += 1
    return count


print (letter_count("aaaabcde","a"))

