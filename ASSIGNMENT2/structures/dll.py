class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new = DLLNode(data)
        if self.head:
            self.head.prev = new
            new.next = self.head
        self.head = new

    def insert_after(self, target, data):
        temp = self.head

        while temp:
            if temp.data == target:
                new = DLLNode(data)
                new.next = temp.next
                new.prev = temp

                if temp.next:
                    temp.next.prev = new

                temp.next = new
                return
            temp = temp.next

    def delete_pos(self, pos):
        if not self.head:
            return

        temp = self.head

        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        count = 0
        while temp and count < pos:
            temp = temp.next
            count += 1

        if not temp:
            return

        if temp.prev:
            temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    def traverse(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result