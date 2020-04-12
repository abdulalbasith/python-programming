my_name= {
    "a":1,
    "b":1,
    "d":1,
    "u":1,
    "l":1
    }

for letter in my_name:
    print (f"The letter {letter} appears {my_name[letter]} time in my name")
    
def reverse_lookup(state_capitals,value):
    result = ""
    for state in state_capitals:
        if state_capitals [state] == value:
            result = state 
    return result


state_capitals = {
  "Alaska" : "Juneau",
  "Colorado" : "Denver",
  "Oregon" : "Salem",
  "Texas" : "Austin"
  }

print(reverse_lookup(state_capitals,"Denver"))