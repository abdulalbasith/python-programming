#list comperhension

nums = [1, 3, 4, 6, 7, 11, -15, 28]

#create a list of only the even numbers in  nums
'''
even_nums = []
for num in nums:
    if num % 2 == 0:
        even_nums.append(num)
print (even_nums)
'''
#using a list comperhension
even_nums = [num for num in nums if num % 2 == 0]

print (even_nums)

vals = [2,4,6,8]

#new list with square of vals

vals_square = [val*val for val in vals]

print (vals_square)

#create a new list with words longer than 4 characters

words = ['run', 'cat', 'hassle', 'print', 'class', 'pyth']

long_words = [word.upper() for word in words if len(word) > 4 ]

print (long_words)

#dictionary comprehension

person = {
    'name' : 'Alice',
    'address':'Toronto',
    'occupation':'engineer',
}

new_person = { item : person[item] for item in person }
new_person2 = { key:val for key, val in person.items()} #another way. .items() is a dictionary function that returns both the key and the value
print (new_person2)

colors = {'red':'Bold', 'green':'Lively', 'blue':'Calm', 'yellow':'Warm'}

#create a new dictionary with color who's values are either warm or lively

warm_lively = { key for key in colors if colors[key] == 'Warm' or colors[key] =='Lively'}
print (warm_lively)

#create a dictionary with the count of each letter in a string
string = 'string'

dict_word = {letter:string.count(letter) for letter in string}

print (dict_word)