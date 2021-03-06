class Stack(object):
    def __init__(self):
        self.data = []     

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return (len(self.data) == 0)

    def push(self, value):
        self.data.append(value)

    def top(self):
        if self.isEmpty():
            raise RuntimeError("StackEmptyException")
        return self.data[len(self.data) - 1]

    def pop(self):
        if self.isEmpty():
            raise RuntimeError("StackEmptyException")
        return self.data.pop()

    def printStack(self):
        print(self.data)

def sortedInsert(stk, element) :
    if stk.isEmpty() or element > stk.top() :
        stk.push(element)
    else :
        temp = stk.pop()
        sortedInsert(stk, element)
        stk.push(temp)

def sortStack(stk):
    if stk.isEmpty() == False :
        temp = stk.pop()
        sortStack(stk)
        sortedInsert(stk, temp)

def sortStack2(stk):
    stk2 = Stack()
    while stk.isEmpty() == False :
        temp = stk.pop()
        while stk2.isEmpty() == False and stk2.top() < temp :
            stk.push(stk2.pop())
        stk2.push(temp)

    while stk2.isEmpty() == False :
        stk.push(stk2.pop())


def bottomInsert(stk, element) :
    if stk.isEmpty() :
        stk.push(element)
    else :
        temp = stk.pop()
        bottomInsert(stk, element)
        stk.push(temp)

def reverseStack(stk):
    if stk.isEmpty() == False :
        temp = stk.pop()
        reverseStack(stk)
        bottomInsert(stk, temp)

from collections import deque
class Queue(object):
    
    def __init__(self):
        self.data = deque([])

    def add(self, value):
        self.data.append(value)

    def remove(self):
        value = self.data.popleft()
        return value
    
    def isEmpty(self):
        return (len(self.data) == 0)

    def size(self):
        return len(self.data)
    
    def printQueue(self):
        print(self.data)

def reverseStack2(stk):
    que = Queue()
    while stk.isEmpty() == False :
        que.add(stk.pop())

    while que.isEmpty() == False :
        stk.push(que.remove())


def reverseKElementInStack(stk, k):
    que = Queue()
    i = 1
    while stk.isEmpty() == False and i < k:
        que.add(stk.pop())

    while que.isEmpty() == False :
        stk.push(que.remove())

def reverseQueue(que):
    stk = Stack()
    while que.isEmpty() == False :
        stk.push(que.remove())

    while stk.isEmpty() == False :
        que.add(stk.pop())

def reverseKElementInQueue(que, k):
    stk = Stack()
    i = 1
    while que.isEmpty() == False and i < k:
        stk.push(que.remove())

    while stk.isEmpty() == False :
        que.add(stk.pop())

    diff = que.size() - k
    while diff > 0 :
        temp = que.remove()
        que.add(temp)
        diff -= 1



stk = Stack()
stk.push(-2)
stk.push(13)
stk.push(16)
stk.push(-6)
stk.push(40)
stk.printStack()
reverseStack2(stk)
stk.printStack()
sortStack2(stk)
stk.printStack()


