# structures/sll.py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert_end(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def delete(self, value):
        temp = self.head

        if temp and temp.data == value:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next

    def traverse(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result