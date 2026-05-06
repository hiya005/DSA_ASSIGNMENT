# structures/stack_sll.py
from .sll import Node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new = Node(data)
        new.next = self.top
        self.top = new

    def pop(self):
        if not self.top:
            return "Underflow"
        val = self.top.data
        self.top = self.top.next
        return val

    def peek(self):
        return self.top.data if self.top else None