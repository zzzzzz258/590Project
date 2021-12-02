"""
Math 560
Project 5
Fall 2021

Partner 1:
Partner 2:
Date:
"""

# Import math, itertools, and time.
import math
import itertools
import time

# Import the Priority Queue.
from p5priorityQueue import *

################################################################################

"""
Prim's Algorithm

INPUT
adjList: adjacent list of map
adjMat: adjacent matrix of map
"""
def prim(adjList, adjMat):
    # initialize cost, prev and visited values for each vertex in adjacency list
    for v in adjList:
        v.cost = math.inf
        v.prev = None
        v.visited = False

    pq = PriorityQueue()

    # always select the first vertex in adjList as the root of the tree
    adjList[0].visited = True
    adjList[0].cost = 0
    for n in adjList[0].neigh:
        n.cost = adjMat[0][n.rank]
        n.prev = adjList[0]
        pq.insert(n)

    # find the lightest cost edge and add it to the tree
    while not pq.isEmpty():
        # add the lightest cost edge to the tree (pop out from the priority queue)
        curr = pq.deleteMin()
        curr.visited = True
        for n in curr.neigh:
            if not n.visited:
                # if find lighter way, update
                if adjMat[curr.rank][n.rank] < n.cost:
                    n.cost = adjMat[curr.rank][n.rank]
                    n.prev = curr

    return

################################################################################

"""
Kruskal's Algorithm
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.
return the list of edges in MST
"""
def kruskal(adjList, edgeList):
    # initialize the list of edges we choose
    X = []
    # initialize all singleton sets
    for v in adjList:
        makeset(v)
    # loop edges in order
    for e in edgeList:
        u = e.vertices[0]
        v = e.vertices[1]
        # if they are not in the same set(this edge wont make a cycle), select
        # this edge and merge the union
        if find(u) != find(v):
            X.append(e)
            union(u, v)

    return X

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.

return
we use a list instead of 
"""
def makeset(v):
    v.pi = None
    v.height = 0
    return

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.

"""
def find(v):
    if v.pi != None:
        return find(v.pi)
    return v

"""
union: this function will union the sets of vertices v and u.
"""
def union(u,v):
    find(v).pi = find(u)
    return

################################################################################

"""
TSP

INPUTS
adjList: 
start: start Vertex
"""
def tsp(adjList, start):
    tour = []
    # initialize the vertices visited status
    for v in adjList:
        v.visited = False
    # DFS
    toVisit = []
    toVisit.append(start)
    while len(toVisit) > 0:
        curr = toVisit.pop()
        curr.visited = True
        tour.append(curr.rank)
        for n in curr.mstN:
            if not n.visited:
                toVisit.append(n)

    tour.append(start.rank)
    return tour

################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p5tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
