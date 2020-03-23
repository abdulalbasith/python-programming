temperature_readings = [25, 18, -5, 11, -3, -15, 8, -18, 6, 13]

number_negatives = 0
number_positive = 0
number_negatives = 0
sum_positive_temp = 0
sum_negative_temp = 0

for count in temperature_readings:
    if count < 0:
        number_negatives += 1
print (number_negatives)


# Calculates the averages of positive and negative numbers in the temprature readings list
'''
number_positive = 0
number_negatives = 0
sum_positive_temp = 0
sum_negative_temp = 0
'''
for temp in temperature_readings:
    if temp > 0:
        number_positive += 1
        sum_positive_temp = sum_positive_temp + temp
    elif temp < 0:
        number_negatives += 1
        sum_negative_temp = sum_negative_temp + temp


average_positive = sum_positive_temp/number_positive
average_negative = sum_negative_temp/number_negatives

print ("The average of the positive numbers is: ",average_positive)
print ("The average of the negative numbers is: ",average_negative)

titles = ["The Avengers", "Avengers age of Ultron", "Captain America, The first avenger"]

#count how many titles has "The" in it

count = 0
for title in titles:
    if "The" in title:
        count +=1

print (f"list has {count} titles with 'The'")

#how many vowels are in a string

string = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc."

for char in string:
    if char in "aeiou":
        number_of_vowels += 1
print (f"The string has {number_of_vowels} vowels")
        
