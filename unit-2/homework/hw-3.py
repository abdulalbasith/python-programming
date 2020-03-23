odd_strings = ['abba', '111', 'canal', 'level', 'abc', 'racecar',
'123451' , '0.0', 'papa', '-pq-']
number_of_strings = 0

for string in odd_strings:
    string_length = len(string)
    first_char= string [0]
    last_char= string [-1]
    if string_length > 3 and first_char == last_char:
        number_of_strings += 1
print (number_of_strings)





