# import only standard Python 3 modules here

'''
INSTRUCTIONS.
========================================================
For each for the following six functions, the input
consists of a set, A, and a relation R on set A. Function
"isPropertyX(A,R)" returns True if R has property X, and
False otherwise. You can assume A is a finite list of ints,
e.g. [1,3,5,7,9], and R is valid relation on A, e.g. [(1,3),
(3,1),(3,7)].
========================================================
'''


def isReflexive(A, R):
    '''TODO: Your code here'''
    for a in A:
        if (a, a) not in R:
            return False
    return True


def isIrreflexive(A, R):
    '''TODO: Your code here'''
    for a in A:
        if (a,a) in R:
            return False
    return True

def isTransitive(A, R):
    '''TODO: Your code here'''
    for a,b in R:
        for c,d in R:
            if b==c:
                if (a,d) not in R:
                    return False
    return True

def isAntisymmetric(A, R):
    '''TODO: Your code here'''
    for a, b in R:
        if a==b:
            continue
        if (b,a) in R:
            return False
    return True


def isSymmetric(A, R):
    '''TODO: Your code here'''
    for a, b in R:
        if (b,a) not in R:
            return False
    return True

def isAsymmetric(A, R):
    '''TODO: Your code here'''
    for a,b in R:
        if (b,a) in R:
            return False
    return True

if __name__ == '__main__':
    A = [0, 1, 2]
    R =[]
    print(isReflexive(A,R))
    print(isAntisymmetric(A,R))
    print(isAsymmetric(A,R))
    print(isIrreflexive(A,R))
    print(isSymmetric(A,R))
    print(isTransitive(A,R))
