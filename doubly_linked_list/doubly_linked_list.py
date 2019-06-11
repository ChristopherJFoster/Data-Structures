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

    def add_to_head(self, value):
        if self.length == 0:
            self.head = ListNode(value)
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length += 1
        if self.length == 1:
            self.tail = self.head

    def remove_from_head(self):
        old_head_val = self.head.value
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = self.head
        return old_head_val

    def add_to_tail(self, value):
        if self.length == 0:
            self.tail = ListNode(value)
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1
        if self.length == 1:
            self.head = self.tail

    def remove_from_tail(self):
        old_tail_val = self.tail.value
        self.tail = self.tail.prev
        self.length -= 1
        if self.length == 0:
            self.head = self.tail
        return old_tail_val

    def move_to_front(self, node):
        if node == self.head:
            return
        else:
            if node != self.tail:
                node.next.prev = node.prev
            node.prev.next = node.next
            node.next = self.head
            node.next.prev = node
            self.head = node

    def move_to_end(self, node):
        if node == self.tail:
            return
        else:
            if node != self.head:
                node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.tail
            node.prev.next = node
            self.tail = node

    def delete(self, node):
        if self.head == node:
            self.remove_from_head()
        elif self.tail == node:
            self.remove_from_tail()
        else:
            node.delete(node)
            self.length -= 1

    def get_max(self):
        pass
