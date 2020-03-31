#function that takes an number of parameters 
'''
*args is a special paramater that lets your functions to take multple arguments
*args is not a list but it works liks a list

'''
def multiple(*args):
    product = 1
    for num in args:
        product *= num

    return product

print (multiple(1))

'''
kewords arguments

'''

def message (name, msg="Hello"):
    print (msg + " " + name)

message ("Abdul")