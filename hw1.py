# import only standard Python 3 libraries here.

"""Implement all the TODOs"""


# input: positive integer x
# output: True or False
def isDivBySeven(x):
    print(x)  # do not remove this line
    """ TODO: finish implementing the function as described on the HW1 handout."""
    if x<10: return True if x==7 or x==0 else False
    else:
        return isDivBySeven((x-21*int(str(x)[-1]))//10)


# input: positive integer x
# output: True or False
def isPrime(x):
    """ TODO: finish implementing the function as described on the HW1 handout."""
    for i in range(2, int(x**0.5)+1):
        if x %i ==0:
            return False
    return True



if __name__ == '__main__':
    '''Nothing below this line will be executed by the autograder ---
            use this space to test your code!'''
    # i dont need test