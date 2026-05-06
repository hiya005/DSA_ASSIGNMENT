# applications/parentheses_checker.py
from structures.stack_sll import Stack

def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if not stack.top or stack.pop() != pairs[ch]:
                return False

    return stack.top is None