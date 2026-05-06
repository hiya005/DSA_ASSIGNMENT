# structures/queue_sll.py
from .sll import Node

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new = Node(data)
        if not self.rear:
            self.front = self.rear = new
            return
        self.rear.next = new
        self.rear = new

    def dequeue(self):
        if not self.front:
            return "Underflow"
        val = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return val