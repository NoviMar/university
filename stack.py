class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

stack = Stack()

with open('file.txt') as file:
    for line in file:
        stack.push(line.strip())

while True:
    item = stack.pop()
    if item is None:
        break
    print(item)