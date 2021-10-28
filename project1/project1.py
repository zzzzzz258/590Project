"""
Math 560
Project 1
Fall 2021

Partner 1: Zezhong Zhang
Partner 2: Yitong Wang
Date: 10/21/2021
"""

from math import floor

"""
SelectionSort

Sort a list in place by selection sort

INPUTS
listToSort: original list to be sorted

OUTPUTS
return: sorted list
"""
def SelectionSort(listToSort):
    # loop over all elments in list
    for i in range(len(listToSort)):
        # set the current (first in unsorted list) element as min
        min = listToSort[i]
        # loop over all the unsorted (following) list
        for j in range(i+1, len(listToSort)):
            # if find a new min, swap it with the first element in unsorted list
            if min > listToSort[j]:
                # swap min and new found min
                temp = min
                min = listToSort[j]
                listToSort[j] = temp
        # set the first element in unsorted list to be the minimal of the rest
        listToSort[i] = min

    return listToSort

"""
InsertionSort

Sort a list in place by insertion sort

INPUTS
listToSort: original list to be sorted

OUTPUTS
return: sorted list
"""
def InsertionSort(listToSort):
    len_=len(listToSort)
    #loop over all elements in list
    for i in range (0,len_):
        #loop over the already sorted list
        for j in range (0,i):
            #comoare the new one with each element in the already sorted list,inssert it 
         if(listToSort[i]<listToSort[j]):
            temp=listToSort[j]
            listToSort[j]=listToSort[i]
            listToSort[i]=temp            
    return listToSort
"""
BubbleSort

Sort a list in place by bubble sort

INPUTS
listToSort: original list to be sorted

OUTPUTS
return: sorted list
"""
def BubbleSort(listToSort):
    len_=len(listToSort)
    #one loop find the biggest one in list,loop for len times to arrange the list 
    for j in range (1,len_):
        flag = 0
        #loop over all elements in list,find the biggest one
        for i in range(0,len_-1):
            #from the first elemnt,compare with the next one,put the small one to the front 
            if(listToSort[i]>listToSort[i+1]):
                temp=listToSort[i]
                listToSort[i]=listToSort[i+1]
                listToSort[i+1]=temp
                flag = 1
        if flag == 0:
            break
    return listToSort

"""
merge

Helper function in merge sort. 


INPUTS
listToSort: final list to store sorted list
left: the 1st sorted list to merge
right: the 2nd list to merge
"""
def merge(left,right,listToSort):
    #i indicate the location it point to in the left list;
    #j indicate the location it point to in the right list;
    i,j = 0,0    
    while i+j<len(listToSort):
        #if() means the element in the left is the small one
        if j==len(right) or (i<len(left) and left[i]<right[j]):
            listToSort[i+j] = left[i]
            i += 1
        else:
            listToSort[i+j] = right[j]
            j += 1

"""
MergeSort

Sort a list in place by merge sort

INPUTS
listToSort: original list to be sorted

OUTPUTS
return: sorted list
"""
def MergeSort(listToSort):
    len_=len(listToSort)
    if len_ < 2:
     return
    #split the list in two parts
    num=int(len_/2)
    left = listToSort[0:num] 
    right = listToSort[num:len_]
    #recursive call,split the sublists in two parts,repeat until every elements was seperated  
    MergeSort(left)
    MergeSort(right)
    #call the function,merge     
    merge(left,right,listToSort)
    return listToSort

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.

INPUTS:
listToSort: the unsorted list to be sorted
i: the left bound of this sorting step(inclusive), default set as 0
j: the right bound of this sorting step(exclusive), default set as None(length of listToSort)

OUTPUTS:
return: the sorted list
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)

    # if only one element left, return it
    if j <= (i+1):
        return listToSort

    # find a pivot which is the middle number in array
    m = floor((i+j)/2)

    # partition array, put all numbers smaller to left and all numbers bigger to right
    # set left pointer as l
    l = i
    # set right pointer as r
    r = j-1
    while l<r:
        # stop at pivot or an element bigger than pivot
        while (l < m) and (listToSort[l] < listToSort[m]):
            l+=1
        # stop at pivot or an element smaller than pivot
        while (r > m) and (listToSort[r] >= listToSort[m]):
            r-=1
        # swap the two elements
        if r > l :
            # swap the two
            temp = listToSort[r]
            listToSort[r] = listToSort[l]
            listToSort[l] = temp
            # if m is one of them, reset m
            if m==l:
                m = r
            elif m == r:
                m = l

    # recursively sort left part and right part
    QuickSort(listToSort, i, m)
    QuickSort(listToSort, m+1, j)

    # return sorted list
    return listToSort

"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('UNSORTED measureTime')
    print()
    measureTime()
    print()
    print('SORTED measureTime')
    print()
    measureTime(True)
