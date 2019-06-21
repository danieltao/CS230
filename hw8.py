import itertools


############### HELPER FUNCTIONS #################

def findCycle(M):
    """
    This function returns a cycle (represented by a list of vertices) containing a given
        vertex v using only vertices in list 'path' and reachable vertices not yet in 'visited'
        if such a cycle exists, otherwise it returns None.

    Input:
        M, list[list[int]]: a symmetric matrix representing an undirected connected graph
            where M[i][j] is None if there is no edge between vertex i and vertex j, otherwise
            it is the weight of the edge between them. Again, the graph represented by M is assumed
            to be connected!

    Output:
        C, list[int]: a list of distinct vertices (ints) for which any two consecutive vertices
            are adjacent according to M, as well as the first and last vertices in C.
    """

    assert isSymmetric(M), "input graph not symmetric"
    assert isConnected(M), "input graph not connected"

    n = len(M)
    visited = set()
    path = []

    for v in range(n):

        if v not in visited:

            cycle = findCycleFrom(v, M, path, visited)

            if cycle is not None:
                return cycle

    return cycle


def isSymmetric(M):
    """
    This function returns True if the matrix M is symmetric (and square), and False otherwise.
    """

    n = len(M)
    if list(map(len, M)) != [n] * n:
        # if M is not square
        return False

    return all(all(M[i][j] == M[j][i] for j in range(i + 1, n)) for i in range(n))


def isConnected(M):
    """
    This function returns True if the graph represented by M is connected, and False otherwise.
    """

    n = len(M)
    visited = set()
    path = []

    findCycleFrom(0, M, path, visited)
    return len(visited) == n


def createExampleGraph():
    """
    This function returns the matrix found on the handout for testing purposes.
    """
    M = [
        [None, 12, -5, 3, 4],
        [12, None, None, -8, None],
        [-5, None, None, 5, None],
        [3, -8, 5, None, 11],
        [4, None, None, 11, None],
    ]
    return M


def findCycleFrom(v, M, path, visited):
    """
    NOTE: This function is NOT to be called directly and intended for use by isConnected(M) and
        findCycle(M). It is essentially a recursive implementation of DFS.

    This function returns a cycle (represented by a list of vertices) containing a given
        vertex v using only vertices in list 'path' and reachable vertices not yet in 'visited'
        if such a cycle exists, otherwise it returns None.

    Input:
        v, int: an integer between 0 and len(M) representing vertex v.
        M, list[list[int]]: a symmetric matrix representing an undirected connected graph
            where M[i][j] is None if there is no edge between vertex i and vertex j, otherwise
            it is the weight of the edge between them. Again, the graph represented by M is assumed
            to be connected!
        path, list[int]: the list of vertices visited in order by DFS to the input vertex v.
        visited, set[int]: a set of vertices visited by DFS.

    Output:
        C, list[int]: a list of distinct vertices (ints) for which any two consecutive vertices
            are adjacent according to M, as well as the first and last vertices in C.
    """

    assert v not in path, "called on vertex already in path"
    assert v not in visited, "called on vertex already visited"

    visited.add(v)
    path.append(v)

    cycle = None
    for u in neighbors(v, M):

        if u in path and path[-2] != u:  # if on path and not immediately before v (path[-1])
            assert u in visited, "found vertex in path that is not visited"

            # u is preceding v in the path, and just found edge (v,u),
            #   so the subpath from u to v with (v,u) makes a cycle.

            i = path.index(u)
            cycle = path[i:]

        elif u in visited:  # and not in path
            continue

        else:  # u not visited
            new_cycle = findCycleFrom(u, M, path, visited)

            if new_cycle is not None:
                cycle = new_cycle

    assert path[-1] == v, "last vertex in path different than current vertex"
    path.pop()

    return cycle


def neighbors(u, M):
    """
    NOTE: This function is NOT to be called directly and intended for use by isConnected(M) and
        findCycle(M).

    This function returns the vertices adjacent to vertex u in the graph
        represented by M.
    """
    return [v for v, w in enumerate(M[u]) if w is not None]


################ INCOMPLETE FUNCTIONS #################

def findMST(M):
    """
    This function returns the total weight of the minimum spanning tree (MST) of the undirected connected graph G
    represented by the input matrix M using the specific algorithm as follows:

        While the graph G contains a cycle:
            1) find a cycle in G, then
            2) delete the heaviest edge in the cycle from G.

    To do so, you can use the function "findCycle(M)" given above. You might find the given functions isConnected(M)
    and isSymmetric(M) useful when testing your implementation.

    Input:
        M, list[list[int]]: a symmetric matrix representing an undirected connected graph
            where M[i][j] is None if there is no edge between vertex i and vertex j, otherwise
            it is the weight of the edge between them. Again, the graph represented by M is assumed
            to be connected!

    Output:
        T: list[list[int]]: a symmetric matrix representing an MST of the input graph M.

    Example:
        See the handout for example code and a figure.
    """

    # TODO: Finish implementing this function.
    if len(M) < 3:
        return M
    circle = findCycle(M)
    while circle:
        heavy, r = -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, (-1,-1)
        for i, v in enumerate(circle):
            if i==len(circle)-1:
                i=-1
            if M[v][circle[i+1]] > heavy:
                heavy = M[v][circle[i+1]]
                r = (v, circle[i+1])
        M[r[0]][r[1]] = None
        M[r[1]][r[0]] = None
        nn = 0
        for i in M:
            for j in i:
                if j:
                    nn+=1
        if nn<3:
            break
        circle = findCycle(M)
    return M


if __name__ == '__main__':
    # Write your testing code below this line
    # and INSIDE this if-block! Feel free to
    # delete this and the given test code.

    X = [[None,2,-3], [2,None,-4],[-3,-4,None]]
#    X = createExampleGraph()
    print("Matrix of graph:")
    for x in X:
        print(x)

    print()

    T = findMST(X)
    print("MST of graph:")
    for t in T:
        print(t)