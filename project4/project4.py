"""
Math 560
Project 4
Fall 2021

Partner 1: Zezhong Zhang (zz258)
Partner 2: Yitong Wang (yw471)
Date: 11/04/2021
"""

# Import p4tests.
import math

from p4tests import *

################################################################################

"""
ED: the edit distance function

INPUTS
src: the previous string to be edited
dest: the final string to be edited to
prob: optional error

OUTPUTS
dist: the number of steps to edit distance
edits:
"""
def ED(src, dest, prob='ED'):
    # Check the problem to ensure it is a valid choice.
    if (prob != 'ED') and (prob != 'ASM'):
        raise Exception('Invalid problem choice!')

    # set length of src and dest
    m = len(src)
    n = len(dest)

    # initialize dp table
    dp = [[0 for x in range(m+1)] for y in range(n+1)]
    # initialize first row and column to be like [0, 1, 2, 3, ...]
    for i in range(m+1):
        dp[0][i] = i
    for j in range(n+1):
        dp[j][0] = j

    # dp loop
    for i in range(1, n+1):
        for j in range(1, m+1):
            if src[j-1]==dest[i-1]:
                # if matches
                replace = dp[i-1][j-1]
            else :
                # if doest match
                replace = 1 + dp[i-1][j-1]
            # no matter if matches, set value of insertion and deletion condition
            insert = 1 + dp[i-1][j]
            delete = 1 + dp[i][j-1]

            # update the dp table based on the best case
            if replace <= insert and replace <= delete:
                # execute substitude or math
                dp[i][j] = replace
            elif insert <= delete:
                # execute insertion
                dp[i][j] = insert
            else:
                # execute delete
                dp[i][j] = delete

    # set distance answer to be dp[column length][row length]
    dist = dp[n][m]
    # initialize edits
    edits = []
    # initialize i, j for finding the path back
    i = n
    j = m
    # trace back to print the edit process
    while dp[i][j] > 0:
        # find the write step (insert, delete, match, substitution)
        if j>0 and dp[i][j] == dp[i][j-1]+1:
            # delete was the last step
            edits.append(('delete', src[j-1], j-1))
            j-=1
        elif j>0 and i>0 and dp[i][j] == dp[i-1][j-1] and src[j-1] == dest[i-1]:
            # match was the last step
            edits.append(('match', src[j-1], j-1))
            i-=1
            j-=1
        elif j>0 and i>0 and dp[i][j] == 1+ dp[i-1][j-1]:
            # sub was the last step
            edits.append(('sub', dest[i - 1], j - 1))
            i -= 1
            j -= 1
        else:
            # insert was the last step
            edits.append(('insert', dest[i-1], j))
            i-=1

    return dist, edits

################################################################################

"""
Main function.
"""
if __name__ == "__main__":
    edTests(False)
    print()
    compareGenomes(True, 30, 300, 'ED')
    print()
    compareRandStrings(True, 30, 300, 'ED')
    print()
    compareGenomes(True, 30, 300, 'ASM')
    print()
    compareRandStrings(True, 30, 300, 'ASM')
