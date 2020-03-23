'''
numbers= [8, 5, 17]

#insert the number -5 at the front of the list

numbers.insert(0,-5)

print (numbers)

print (len(numbers))
last_el = numbers.pop()
print (last_el)

#print the second element in the list

print (numbers [1])
print (numbers)
'''
grades = [70, 85, 91, 23, 60, 45, 90, 56, 77, 88]

# add 5 to each grade in the list
# we have to access element (position) in the list, change the element
# we need ot access the index, we use range

range (0, len(grades))

for index in range (len(grades)):
    grades [index] += 5

print (grades)

#make each word past tense in this list 

verbs = ['like', 'hate', 'fake', 'rake']

for index in range(len(verbs)):
    verbs [index] += 'd'
    #verbs [index] = 'd' + verbs [index]

print (verbs)