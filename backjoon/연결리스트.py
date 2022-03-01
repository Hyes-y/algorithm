# 1021 회전하는 큐
# 메모리 : 32352KB   /   시간 : 7424ms   / 코드 길이 : 429B




# 1406 에디터
# 메모리 : 	181720KB   /   시간 : 568ms   / 코드 길이 : 2241B

import sys

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class NodeManager:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.cur = self.tail

    def add(self, data):
        node = self.cur
        new_node = Node(data)
        
        node.next = new_node
        new_node.prev = node
        self.tail = new_node
        
        self.cur = new_node

    def plus(self, data):
        node = self.cur
        new_node = Node(data)

        if not node.prev:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.cur = new_node.next
        else:
            new_node.prev = node.prev
            node.prev.next = new_node
            new_node.next = node
            node.prev = new_node
            self.cur = node

    
    def delete(self):
        node = self.cur

        if not node.prev:
            pass

        elif not node.prev.prev:
            node.prev = None
            self.head = node

        else:    
            node.prev.prev.next = node
            node.prev = node.prev.prev
        

    def move(self, direction):
        if direction == 'L':
            if self.cur.prev:
                self.cur = self.cur.prev
            else:
                self.cur = self.head

        else:
            if self.cur.next:
                self.cur = self.cur.next
            else:
                self.cur = self.tail
    
    def desc(self):
        node = self.head
        while node.next:
            print(node.data, end='')
            node = node.next
        



sentence = sys.stdin.readline().rstrip()

editor = NodeManager(sentence[0])

for i in range(1, len(sentence)):
    editor.add(sentence[i])

editor.add('tail')

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    func = sys.stdin.readline().rstrip()
    if len(func) > 1:
        func, data = func.split(' ')
    
    if func == 'L':
        editor.move('L')
    elif func == 'D':
        editor.move('D')
    elif func == 'B':
        editor.delete()
    elif func == 'P':
        editor.plus(data)

editor.desc()