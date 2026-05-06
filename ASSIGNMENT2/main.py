import os
from structures import *
from applications import is_balanced

os.makedirs("results", exist_ok=True)

output = ""

# Dynamic Array
da = DynamicArray()
for i in range(5):
    da.append(i)

output += f"Dynamic Array: {da.display()}\n"

# SLL
sll = SinglyLinkedList()
sll.insert_begin(1)
sll.insert_end(2)
sll.insert_end(3)
output += f"SLL: {sll.traverse()}\n"

# DLL
dll = DoublyLinkedList()
dll.insert_begin(10)
dll.insert_after(10, 20)
output += f"DLL: {dll.traverse()}\n"

# Stack
stack = Stack()
stack.push(10)
stack.push(20)
output += f"Stack Pop: {stack.pop()}\n"

# Queue
q = Queue()
q.enqueue(1)
q.enqueue(2)
output += f"Queue Dequeue: {q.dequeue()}\n"

# Parentheses
expr = "{[()]}"
output += f"Balanced '{expr}': {is_balanced(expr)}\n"

print(output)

with open("results/output.txt", "w") as f:
    f.write(output)