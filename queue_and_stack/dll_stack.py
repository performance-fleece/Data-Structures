import sys
sys.path.append('C:\\Git\\python-lambda\\Data-Structures')
from doubly_linked_list.doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)


    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
            

        else:
            return None


    def len(self):
        return self.size


