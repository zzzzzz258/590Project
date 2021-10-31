"""
Math 560
Project 2
Fall 2021

project2.py

Partner 1: Zezhong Zhang (zz258)
Partner 2: Yitong Wang (yw471)
Date: 11/3/2021
"""

# Import math and other p2 files.
import math
from p2tests import *
from p2stack import Stack
from p2queue import Queue

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The path from maze.start to maze.exit.
"""
def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')

    # reset the maze: set dist = 0, prev = None, visited = False for all vertices
    for vertex in maze.adjList:
        vertex.dist = 0
        vertex.prev = None
        vertex.visited = False

    # reset path to be empty (as my understanding)
    maze.path = []

    # initialize the stack and queue for dfs and bfs
    s = Stack()
    q = Queue()

    # BFS
    if (alg == 'BFS') :
        # put the first vertex into queue
        q.push(maze.start)
        # bfs loop
        while not q.isEmpty():
            # pop out the current vertex from queue and mark it as visited
            curr = q.pop()
            # skip if curr is visited
            if (curr.visited):
                continue
            curr.visited = True
            # check if this is exit
            if (curr == maze.exit):
                # put the path into maze.path
                maze.path.append(curr.rank)
                while curr!=maze.start:
                    curr = curr.prev
                    maze.path.insert(0, curr.rank)
                break
            # add all current vertex's neighbor to queue
            for nextV in curr.neigh:
                if not nextV.visited:
                    # set nextV's previous node
                    nextV.prev = curr
                    q.push(nextV)

    # DFS
    else :
        # do dfs in a recursive helper function
        dfs(maze, maze.start, s)


    return maze.path


"""
Recursive DFS function
    
INPUTS
maze: the graph
vertex: current vertex we are visiting    
stack: a stack storing the current path of dfs
"""
def dfs(maze, vertex, stack):
    # if maze.path is already filled, return
    if maze.path != []:
        return
    # if this is the exit, stop and print path to maze.path
    if (vertex == maze.exit):
        maze.path.append(vertex.rank)
        while not stack.isEmpty():
            maze.path.insert(0, stack.pop().rank)
        return
    # add current vertex to stack, mark it as visited
    stack.push(vertex)
    vertex.visited = True
    # dfs all its neighbours
    for nextV in vertex.neigh:
        # only visit if unvisited
        if not nextV.visited:
            dfs(maze, nextV, stack)
    # no exit from this vertex, remove from stack
    stack.pop()


"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)
