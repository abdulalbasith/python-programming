def dict_merge(dict1,dict2):
    new_dict = {}
    for key in dict1:
        if dict1[key] not in new_dict:
            new_dict [key] = (dict1[key])
        

    return (new_dict)


print (dict_merge({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))

#Problem 3

def reverse_dict (dict1):
    new_dict = {}
    for key,value in dict1.items():
        new_dict = {value:key}
    return new_dict

print (reverse_dict({'name': 'alicia', 'job':'Engineer', 'city': 'Toronto'}))

