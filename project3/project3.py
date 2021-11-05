"""
Math 560
Project 3
Fall 2021

Partner 1: Zezhong Zhang (zz258)
Partner 2: Yitong Wang (yw471)
Date: 11/03/2021
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage

find all negative cost cycles

INPUTS
adjacent list of exchange rates graph
adjacent matrix of exchange rates graph
tolerance number, 

OUTPUTS
single list of of vertex ranks corresponding to the negative cost cycle
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
    # initialization
    for v in adjList:
        # set distance to 0 if this is start vertex
        if v.rank == 0:
            v.dist = 0
        # set distance to infinite if this is not start vertex
        else:
            v.dist = math.inf
        # set previous vertex to None
        v.prev = None

    # bellman-ford
    # loop |V|-1 times
    for i in range(len(adjList)-1):
        # loop over all vertex in graph
        for v in adjList:
            # loop over all neighbor if current vertex
            for n in v.neigh:
                # update considering tolerance
                if n.dist > v.dist + adjMat[v.rank][n.rank] + tol:
                    # update distance to start
                    n.dist = v.dist + adjMat[v.rank][n.rank]
                    # update previous vertex
                    n.prev = v

    # testing
    # for v in adjList:
        # print(v.rank, v.dist, v.prev)


    # vertex that changed in the final iteration
    finalChange = []
    # an extra iteration to find a negative loop
    for v in adjList:
        # loop over all neighbor if current vertex
        for n in v.neigh:
            # update considering tolerance
            if n.dist > v.dist + adjMat[v.rank][n.rank] + tol:
                # update distance to start
                n.dist = v.dist + adjMat[v.rank][n.rank]
                # update previous vertex
                n.prev = v
                # add changed vertex into the list to be checked
                finalChange.append(n)


    # initialize ans to be empty list
    ans = []
    # traverse changed vertexes in final iteration
    for v in finalChange:
        # clear ans
        ans.clear()
        # assign temp t to v
        t = v
        # while t is not None and ans is not a cycle, append previous to ans
        while (not t.rank in ans) and t != None:
            ans.append(t.rank)
            t = t.prev
        # add t to cycle to make it a cycle
        ans.append(t.rank)
        # return ans if a cycle is made
        if ans[0] == ans[-1]:
            return ans

    # return empty list if no negative cycle is found
    return []






################################################################################

"""
rates2mat

convert raw exchange rates to log exchange rates

INPUTS
rates: a 2D list representing the original exchange rates

OUTPUS
logRates: a 2D list representing the log exchange rates
"""
def rates2mat(rates):
    logRates = [[math.log2(c) for c in r] for r in rates]
    return logRates

"""
Main function.
"""
if __name__ == "__main__":
    testRates()

