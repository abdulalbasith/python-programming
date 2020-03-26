def add_two():
    result = 5 + 5
    print (result)

add_two()

#passing arguments

def add_two2 (a, b):
    result = a + b
    print (result)

add_two2(5 , 4)

#Returning a value

def add_two3 (a, b):
    result = a+b
    return result

add_two3 (3,10)

# Function that adds up integers in a list

def sum_list (a_list):
    total = 0
    for i in a_list:
        total += i
    return total 

print (sum_list([2,4,6]))

#write a function that reverses a sting

def rev_string (my_string):
    index = len(my_string) -1
    reversed_string = ""
    while index >=0:
        reversed_string += my_string[index]
        index -= 1
    return reversed_string

print (rev_string("Jane"))

def rev_string2(my_string):
    string = ''
    for i in my_string:
        string = i + string
    return string

print(rev_string2('nohtyP'))

#write a function that finds the intersaction of two lists 
#return the items that are in both list 1 and 2, in a new list

def intersect_list (list_1, list_2):
    
    new_list = []
    for item in list_1:
        if item in list_2:
            new_list.append(item)
    return new_list

print (intersect_list(["a",2,3],[1,"a",5]))
