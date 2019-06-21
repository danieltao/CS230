# import only standard Python 3 libraries here.
import math
import itertools

def f_test(xs):
    """ This is an example Boolean function which computes "x1 or not x2" where
        x1 and x2 are the first and second values in the given list 'xs'.
    """
    return (xs[0] or not xs[1])

def generateTable(n,f):
    # THIS FUNCTION IS COMPLETE. DO NOT MODIFY THIS FUNCTION.
    # The autograder will run an unmodified version of this against your DNF converter!

    """ This function computes and returns truth table for a Boolean function, f,
            which has n Boolean variables.

        Args:
            n: the number of Boolean variables in the Boolean function f.
            f: a function (method) which computes a Boolean function over a LIST of Boolean values,
                e.g. f_test(xs) above

        Returns:
            a truth table for function f with n variables, represented as
                a tuple of 2^n tuples (truth table rows) of length n+1. The first n values of
                each tuple denote the truth values of the n variables x0,x1,...,x(n-1) and
                the last value is the truth value of f([x0,x1,...,x(n-1)]).

        Example: generateTable(2,f_test) returns a tuple of 4 tuples of length 3:
            ((True,True,True),
             (True,False,True),
             (False,True,False),
             (False,False,True))

            which corresponds to the truth table:

            | x0 | x1 |f_test([x0,x1])|
            ---------------------------
            | T  |  T |       T       |
            | T  |  F |       T       |
            | F  |  T |       F       |
            | F  |  F |       T       |
    """
    truths = itertools.product([True,False], repeat=n)
    table = ()
    for truth in truths:
        result = f(truth)
        truth_with_result = truth + (result,)
        table += (truth_with_result,)
    return table

def convertToDNF(n, table):
    """ This function computes and returns a DNF formula, represented as a string,
            that is equivalent to the input truth table "table" with n variables.
        Args:
            n: the number of Boolean variables (this should also be one less than
                the length of each row in "table" if "table" is in the right format)
            table: A tuple of tuples of True and False (the Boolean values in Python)
            representing a Boolean function. The format is expected to be EXACTLY the format
            used by the given method "generateTable(n,f)" above.

        Returns:
            A string that is the DNF formula equivalent to that represented by "table" with
            the following specifications:

            1) the OR symbol is represented by the letter 'v'
            2) the AND symbol is represented by the carat, '^'
            3) the NEG symbol is represented by the letter 'n'
            4) parentheses enclose every conjunction, even if there is only one conjunction
                and/or one literal in a conjunction
            5) the first variable has index 0 (zero), and the n'th variable has index n-1
            6) ordering of the literals in each conjunction does NOT matter (but for your sake,
                put them in numerical order)
            7) ordering of the conjunctions does NOT matter
            8) spacing does NOT matter (but for your sake, use spaces for readability and testing)
            9) a DNF formula for which there are no conjunctions is represented by the empty string: ''

            For example, the following are valid DNF formulae to be output (for some input truth tables)
            - ''
            - '(x0)'
            - '(x0 ^ nx1 ^ x2)'
            - '(x0 ^ nx1 ^ x2) v (x2 ^ nx0 ^ x1)'

        Examples:
            convertToDNF(2,generateTable(2,f_test)) returns a string according to the specifications above
            such as '(x0 ^ x1) v (x0 ^ nx1) v (nx0 ^ nx1)'
    """
    # TODO: Finish this function!
    # YOUR CODE HERE
    res = ''
    for row in table:
        result = row[-1]
        if result:
            res += "("
            for i in range(0, n):
                if not row[i]:
                    res += "n"
                res += "x"+ str(i) + " ^ "
            res = res[:-3] + ") v "
    return res[:-3]



if __name__ == '__main__':
    '''Nothing IN THIS IF-BLOCK will be executed by the autograder ---
        use this space to test your code!'''
    table = generateTable(100, f_test)
    print(table)
    print(convertToDNF(100, table))