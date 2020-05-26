"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):

        new_node = ListNode(value)
        self.length += 1
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # if self.head is None:
        #     return

        # self.length -= 1
        # if self.head == self.tail:
        #     removed = self.head.value
        #     self.head = None
        #     self.tail = None
        #     return removed
        # else:
        #     removed = self.head.value
        #     new_head = self.head.next
        #     new_head.prev = None
        #     self.head = new_head
        #     return removed
        removed = self.head.value
        self.delete(self.head)
        return removed

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        # if self.head is None:
        #     return

        # self.length -= 1

        # if self.head == self.tail:
        #     removed = self.tail.value
        #     self.head = None
        #     self.tail = None
        #     return removed

        # else:
        #     removed = self.tail.value
        #     new_tail = self.tail.prev
        #     new_tail.next = None
        #     self.tail = new_tail
        #     return removed
        removed = self.tail.value
        self.delete(self.tail)
        return removed

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # if self.head == self.tail or node == self.head:
        #     print("already head or head/tail same")
        #     return
        # else:
        #     current_node = node
        #     current_node.prev.next = current_node.next
        #     current_node.next = self.head
        #     self.head.prev = current_node
        #     self.head = current_node
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # if head
        # if tail
        # if middle
        # if empty
        if not self.head:
            print("empty list")
            return
        self.length -= 1
        # if head is tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # if head
        if node == self.head:
            self.head = node.next
            self.head.prev = None
        # if tail
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        # if middle
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        if self.length == 0:
            return None

        max_value = self.head.value
        current = self.head.next
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value

    # def reversemiddle(self)
