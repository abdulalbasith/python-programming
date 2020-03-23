#Print hello world

#print ('Hello world')

#Creating a variable to store first and last name

first_name = "Abdul"
last_name = "Al-Basith"
age = 26

#string concatenation
full_name = first_name + " " + last_name

#print (first_name)
#print (full_name)

#Use format string to print 

#print ("Hello, my name is " + first_name + " and I am " + str(age) + " years old") 

#format string - Easy way to format a lot of string with variables in it

#print(f"Hello, my name is {first_name} and I am {age} years old")

#create variables to store the names of all  your classmates
#print all the names in the following message

'''
name1 = "Justin"
name2 ="Harrison"
name3 = "Abdul"
name4 = "Long"
name5 = "Griffen"
name6 = "Thanujan"
name7 = "Amelia"
print (f"The members of my cohort are {name1}, {name2}, {name3}, {name4}, {name5}, {name6}, and {name7}, and they are all awesome!")
'''

member_list = ["Justin","Harrison","Abdul","Long","Griffen", "Thanujan", "Amelia", "Claudia", "Nima"]

print (f"The members of my cohort are {', '.join(member_list)} and they are all awesome!")