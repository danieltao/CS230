import itertools


##################### EXAMPLE GRAPH CONSTRUCTIONS ####################

def createEmptyGraph(n):
    '''
    This function returns an empty graph of n vertices represented by a list V,
    whose elements are integers ranging from 0 to n-1 (inclusive), and an empty list E.

    input: n (int): a number of vertices

    output: V (list(int)), E (list(set(int)): representation of n-vertex
        undirected complete graph G = (V,E).
    '''

    V = list(range(n))
    E = list()
    return (V, E)


def createCompleteGraph(n):
    '''
    This function returns a complete graph of n vertices represented by a list V,
    whose elements are integers ranging from 0 to n-1 (inclusive), and a list E,
    whose elements are 2-element subsets of V.

    input: n (int): a number of vertices

    output: V (list(int)), E (list(set(int)): representation of n-vertex
        undirected complete graph G = (V,E).
    '''
    V = list(range(n))
    E = list(map(set, itertools.combinations(V, 2)))
    return (V, E)


def createExampleGraph():
    '''
    This function returns a graph with 4 vertices represented by a list V,
    whose elements are integers ranging from 0 to 3 (inclusive), and a list E,
    whose elements are 2-element subsets of V, [ {0,1}, {1,2}, {2,3}, {0,3} ].

    input: n (int): a number of vertices

    output: V (list(int)), E (list(set(int)): representation of n-vertex
        undirected complete graph G = (V,E).
    '''

    V = list(range(4))
    E = [
        set([0, 1]),
        set([0, 2]),
        set([0, 3]),
        set([1, 2]),
        set([2, 3]),
    ]

    return (V, E)


########################## HELPER FUNCTIONS ###########################
def printGraph(V, E):
    '''
    This function prints the lists V and E to the terminal for easy testing/debugging purposes.

    input:  V (list(int)): a list of ints of the form [0, 1, 2, ..., len(V)-1]
            E (list(set(int))): a list of two-element subsets of V

    output: none
    '''
    E_strings = ['{%d, %d}' % (u, v) for u, v in map(list, E)]

    print('Vertices: {%s}' % ', '.join(map(str, V)))

    # print at most 5 edges per line for readability
    step = 5
    if len(E) == 0:
        print('Edges: {}')
    else:
        print('Edges: {')
        for i in range(0, len(E_strings), step):  # for every fifth index in the list
            print('    ' + ', '.join(E_strings[i:i + step]) + ',')

        print('}')


def convertToList(s):
    '''
    This function simply casts a given object (e.g. a set) s to a list which might be useful
        since sets are NOT accessible by index (sets are unordered).
        Of course, you can simply use the list() function in your code directly
        instead of using this one.
    '''
    return list(s)


def convertToSet(s):
    '''
    This function simply casts a given object (e.g. a list) s to a set which might be useful
        since the graph functions assume vertices and edge sets to be represented as sets.
        Of course, you can simply use the set() function in your code directly
        instead of using this one.
    '''
    return set(s)


####################### INCOMPLETE FUNCTIONS ##########################

def getAdjacencyList(V, E):
    '''
    This function converts an undirected simple graph represented by lists V and E to an adjacency list
    representation. In this assignment, we will assume V is of the form [0, 1, 2, ..., len(V)-1].

    input:  V (list(int)): a list of ints of the form [0, 1, 2, ..., len(V)-1]
            E (list(set(int))): a list of two-element subsets of V

    output: L (list(list(int)): a len(V)-length list of lists of ints such that L[i] contains the
                vertices adjacent to vertex i in undirected graph G = (V,E). Note
                this implies isolated vertices should have EMPTY lists. The ordering
                of each vertex's list does not matter.

    example:   getAdjacencyList(*createExampleGraph()) =
                    [[1,2,3],
                     [0,2],
                     [0,1,3],
                     [0,2]]

                (Note that since createExampleGraph returns a TUPLE containing V and E,
                    the * is required to 'unpack' the tuple and input V and E individually
                    into graphToAdjacencyList.)
    '''
    r = [[] for i in V]
    for a, b in E:
        r[a].append(b)
        r[b].append(a)
    return r



def getAdjacencyMatrix(V, E):
    '''
    This function converts an undirected simple graph represented by lists V and E to an adjacency matrix
    representation. In this assignment, we will assume V is of the form {0, 1, 2, ..., len(V)-1}.

    input:  V (list(int)): a list of ints of the form [0, 1, 2, ..., len(V)-1]
            E (list(set(int))): a list of two-element subsets of V

    output: M (list(list(int)): a len(V)-length list of len(V)-length lists of ints such that
                M[i][j] is 1 if vertex i is adjacent to vertex j in undirected graph G = (V,E),
                and 0 otherwise.

    examples:   getAdjacencyMatrix(*createExampleGraph()) =
                    [[0,1,1,1],
                     [1,0,1,0],
                     [1,1,0,1],
                     [1,0,1,0]]

                (Note that since createExampleGraph returns a TUPLE containing V and E,
                    the * is required to 'unpack' the tuple and input V and E individually
                    into graphToAdjacencyMatrix.)
    '''
    this_question_is_shit = [[0 for i in V] for j in V]
    for waste_of_time, i_dont_go_to_any_class in E:
        this_question_is_shit[waste_of_time][i_dont_go_to_any_class] = 1
        this_question_is_shit[i_dont_go_to_any_class][waste_of_time] = 1
    return this_question_is_shit


def getDegreeList(V, E):
    '''
    This function returns a list containing the degrees of each vertex in V.
    In this assignment, we will assume V is of the form {0, 1, 2, ..., len(V)-1}.

    input:  V (list(int)): a list of ints of the form [0, 1, 2, ..., len(V)-1]
            E (list(set(int))): a list of two-element subsets of V

    output: D (list(int)): a list of integers such that D[i] is the degree of vertex i.

    examples:   getDegreeList(*createExampleGraph()) = [3,2,3,2]
                (Note that since createExampleGraph returns a TUPLE containing V and E,
                    the * is required to 'unpack' the tuple and input V and E individually
                    into getDegreeList.)
    '''
    withdraw = [0 for i in V]
    for too_easy, fuck in E:
        withdraw[too_easy] += 1
        withdraw[fuck] += 1
    return withdraw


if __name__ == '__main__':
    # Write your testing code below this line
    # and INSIDE this if-block! Feel free to
    # delete this and the given test code.
    print(getAdjacencyList(*createExampleGraph()))
    print(getAdjacencyMatrix(*createExampleGraph()))
    print(getDegreeList(*createExampleGraph()))
