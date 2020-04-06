import json
#create a person dictionary
person = {
    "name" : "Abdul",
    "address": "Toronto",
    "occupation": "Software implementation"
}

#get person name
print (person ["name"])

#change person address

person ["address"] = "North York"

#keys are unique
#keys have to be int, float, string - immutable

#add age to person information
person ["age"] = 26 #Works if the key is not already in the dictionary

#print person details

for key in person: #When we do a for in, python looks at just the keys
    print (key + ":", person [key], end="")
    print () #prints a new line


x = ["a", "b", "c"]

for item in x:
    print (type (item)) #Python will tell you what type of data is each thing in a list

cars = [
    {
        'make': 'Toyota',
        'model': 'Camry',
        'year': '2017',
        'color': 'black'
    },
    {
        'make': 'Toyota',
        'model': 'Prius',
        'year': '205',
        'color': 'white'
    },
    {
        'make': 'Mercedes Benz',
        'model': 'A 250',
        'year': '2019',
        'color': 'grey'
    },
    {
        'make': 'Hyundai',
        'model': 'Elantra',
        'year': '2007',
        'color': 'grey'
    },
    {
        'make': 'Lexus',
        'model': 'IS 300',
        'year': '2020',
        'color': 'blue'
    },
]

#adding prices to cars with a for loop
i = 0
price_list = [10000,13000,14000,15000,17000]
for car in cars:
    car['price'] = price_list[i]
    i+=1

print (json.dumps(cars, indent=2))

# Using enumerate. Enumerate takes and iterable and returns a pair of index and item in the list

for index, car in enumerate(cars):
    car['price'] = price_list[index]

def revers_lookup (dictionary, value):
    for key in dictionary:
        if value == dictionary[key]:
            return key
    return "No match"

state_capitals = {
    "Alaska" : "Juneau",
    "Colorado" : "Denver",
    "Oregon" : "Salem",
    "Texas" : "Austin"
}
print (revers_lookup(state_capitals,"Austin"))

#Write a function called frequency_counter, accepts a string. Return a dictionary with each word and the number of times each word occurs in the string

def frequency_counter (string):
    words = string.split ()
    print (words)
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1
    return json.dumps(word_count,indent=1)
        
print (frequency_counter("Here  is a simple sentence"))