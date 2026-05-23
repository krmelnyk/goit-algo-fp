class Node:
    """A single node of a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A minimal singly linked list wrapper used for the task demonstrations."""

    def __init__(self, values=None):
        self.head = None
        if values:
            for value in values:
                self.append(value)

    def append(self, data):
        """Append a new value to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def to_list(self):
        """Return linked-list values as a regular Python list."""
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values

    def print_list(self):
        """Print list values in a readable linked-list form."""
        print(" -> ".join(map(str, self.to_list())))

    def reverse(self):
        """Reverse this list in place and return the list instance."""
        self.head = reverse_linked_list(self.head)
        return self

    def sort(self):
        """Sort this list in place using merge sort and return the list instance."""
        self.head = merge_sort(self.head)
        return self


def reverse_linked_list(head):
    """Reverse a singly linked list by changing node references."""
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


def get_middle(head):
    """Find the middle node to split the list into two halves for merge sort."""
    if head is None:
        return None

    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_sorted_nodes(left, right):
    """Merge two sorted node chains and return the head of the merged chain."""
    dummy = Node(0)
    tail = dummy

    while left and right:
        if left.data <= right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    tail.next = left if left else right
    return dummy.next


def merge_sort(head):
    """Sort a linked list using recursive merge sort and return the new head."""
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    right_head = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(right_head)
    return merge_sorted_nodes(left, right)


def merge_sorted_lists(first, second):
    """Merge two sorted LinkedList instances into a new sorted LinkedList."""
    merged = LinkedList()
    merged.head = merge_sorted_nodes(first.head, second.head)
    return merged
