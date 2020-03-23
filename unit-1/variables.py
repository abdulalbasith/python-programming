car_total = 12

#check if car total is even
if car_total % 2 == 0:
    print ("Car total is even")
else:
    print ('Car total is odd')

'''
 80 - 100 > A
 60 - 79 > B
  50 - 59 > C
 Less than 50 > D
''' 

#using elif with multiple conditions
score = 65

if score >= 80:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >=50:
    grade = "C"
else:
    grade = "D"

print (grade)   

'''
If number is divisible by 3 print fizz
if its divisible by 5 print buzz
if its divisible by 15, print fizzbuzz

'''


for num in range(1,51):
#    num = num + 1
    if num % 15 == 0:
        print ("fizzbuzz")
    elif num % 5 == 0:
        print ("buzz")
    elif num % 3 == 0:
        print ("fizz")
    else:
        print (num)


'''
Find the sum of even numbers between 1 and 10
'''

total = 0
for num in range (1,11):
    if num % 2 == 0:
       total += num
print (total)
        