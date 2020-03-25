list_of_numbers = [12,77,83,29,10,39,2,100,200,267,75,98]
index = 0
largest_number = list_of_numbers [index]


while index < len(list_of_numbers):
    if list_of_numbers [index] > largest_number:
        largest_number = list_of_numbers [index]
    index += 1

print (largest_number)
