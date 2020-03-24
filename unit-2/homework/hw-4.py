import random
# Generate range of individuals in sample

# 1 - 14 20%
# 15 - 64 60%
# 65 - 99 20%

one_to_14 = range(1, 15)
fifteen_to_64 = range (15, 65)
sixty_five_and_over = range (65, 100)

population = []

for num in range (1, 190000):
    val = random.random() #generates a number between 0.0 and 1.0
    if val >= 0.8:
        #add age group over 65
        population.append(random.choice(sixty_five_and_over))
    elif val >= 0.21:
        # add 15-65 age group
        population.append(random.choice(fifteen_to_64))
    else:
        #add 1-14 age group
        population.append(random.choice(one_to_14))


count = 0
for age in population:
    if age >= 65:
        count += 1

print (count)

over_80 = 0

for age in population:
    if age >= 80:
        over_80 += 1

number_of_people_dying = (over_80 * 0.15) * 10
print (f"# of people over 80 who might die is {number_of_people_dying}")