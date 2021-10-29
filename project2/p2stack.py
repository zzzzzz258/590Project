"""
Math 560
Project 2
Fall 2021

p2stack.py

Partner 1: Zezhong Zhang (zz258)
Partner 2: Yitong Wang (yw471)
Date: 10/29/2021
"""

"""
Stack Class
"""
class Stack:

    """
    Class attributes:
    stack    # The array for the stack.
    top      # The index of the top of the stack.
    numElems # The number of elements in the stack.
    size     # The size of the stack
    """

    """
    __init__ function to initialize the Stack.
    Note: intially the size of the stack defaults to 3.
    Note: the stack is initally filled with None values.
    Note: since nothing is on the stack, top is -1.
    """
    def __init__(self, size=3):
        self.stack = [None for x in range(0,size)]
        self.top = -1
        self.numElems = 0
        self.size = size
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.stack)) + ' ]\n'
        s += ('Top: %d' % self.top) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        s += ('size: %d' % self.size) + '\n'
        return s

    """
    isFull function to check if the stack is full.
    
    OUTPUT:
    true if stack if full, false otherwise
    """
    def isFull(self):
        return self.numElems >= self.size

    """
    isEmpty function to check if the stack is empty.
    
    OUTPUTS:
    true if stack if empty, false otherwise
    """
    def isEmpty(self):
        return self.numElems == 0

    """
    resize function to resize the stack by DOUBLING its size.
    """
    def resize(self):
        # double the size attribute
        self.size *= 2
        # initialize a new array and copy everything to it
        self.stack = self.stack * 2
        return

    """
    push function to push a value onto the stack.
    """
    def push(self, val):
        # resize (double) stack size if stack if full
        if (self.isFull()):
            self.resize()

        # update top and push the val at the top of stack
        self.top+=1
        self.stack[self.top] = val

        # update numElems
        self.numElems+=1
        return

    """
    pop function to pop the value off the top of the stack.
    """
    def pop(self):
        # do nothing if the stack if empty
        if (not self.isEmpty()):
            # remove the top element from stack
            # updating top and numElems
            self.top-=1
            self.numElems-=1
            return self.stack[self.top+1]
        else :
            return None


"""
Testing function to test stack.
"""
if __name__ == "__main__":
    s1 = Stack(5)
    s1.push(1)
    s1.push(4)
    s1.push("9")
    print(s1)
    s1.pop()
    s1.push(9)
    s1.push(3)
    s1.push(10)
    print(s1)
    s1.push(1312421)
    print(s1)
    s1.pop()
    print(s1)
