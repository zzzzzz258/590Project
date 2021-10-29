"""
Math 560
Project 2
Fall 2021

p2queue.py

Partner 1: Zezhong Zhang (zz258)
Partner 2: Yitong Wang (yw471)
Date: 10/29/2021
"""

"""
Queue Class
"""
class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    size     # The size of this queue
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 3.
    Note: the queue is initally filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        self.size = size
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.queue)) + ' ]\n'
        s += ('Front: %d' % self.front) + '\n'
        s += ('Rear: %d' % self.rear) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        s += ('size: %d' % self.size) + '\n'
        return s

    """
    isFull function to check if the queue is full.
    """
    def isFull(self):
        # queue is full when head reaches rear and size != 0 (they also reach when size is 0)
        return self.front == self.rear and self.numElems != 0

    """
    isEmpty function to check if the queue is empty.
    """
    def isEmpty(self):
        # is empty if size = 0
        return self.size == 0

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """
    def resize(self):
        # initialize a new array with double size
        newQueue = [None for x in range(0, 2*self.size)]
        # copy previous array to new, rearrange it
        newQueue[0:self.size - self.front] = self.queue[self.front:self.size]
        newQueue[self.size-self.front:self.size] = self.queue[0:self.front]
        # assign the newQueue to object
        self.queue = newQueue
        # reset front, rear, size
        self.front = 0
        self.rear = self.numElems
        self.size *= 2
        return

    """
    push function to push a value into the rear of the queue.
    """
    def push(self, val):
        # resize queue if the queue is full
        if self.isFull():
            self.resize()
        # insert the element into the rear position
        self.queue[self.rear] = val
        # update rear and numElems
        self.rear += 1
        self.numElems += 1
        # flip to the start of array rear is invalid
        if self.rear == self.size :
            self.rear = 0
        return

    """
    pop function to pop the value from the front of the queue.
    """
    def pop(self):
        # only pop if queue is not empty
        if not self.isEmpty():
            # assign out to the front element
            out = self.queue[self.front]
            # update front and numElems
            self.front += 1
            self.numElems -= 1
            # flip front to the start of array if is invalid
            if self.rear == self.size:
                self.rear = 0
            # return out
            return out
        # return None if empty
        return None

"""
helper function to test
"""
if __name__ == "__main__":
    q = Queue(3)
    q.push(2)
    q.push(0)
    q.pop()
    print(q)
    q.push(9)
    q.push(10)
    q.push("*")
    print(q)