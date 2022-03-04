#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None
        self.tail = None

        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            next = self.current
            self.current = self.current.next
            return next

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []
        node = self.head
        while node is not None:
            items.append(node.data)
            node = node.next
        return items

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) loops through all elements regardless to count."""
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) no loops because tail is tracked."""
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node
            self.size = 1
        else:
            self.tail.next = node
            self.tail = self.tail.next
            self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) no loops because head is tracked."""
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node
            self.size = 1
        else:
            node.next = self.head
            self.head = node
            self.size += 1

    def find(self, matcher):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) no loops if head matches.
        Worst case running time: O(n) all elements looped if last node
        matches or none do."""
        node = self.head
        while node is not None:
            if matcher(node.data):
                return node.data
            node = node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) no loops if empty, head matches, or
            head.next matches.
        Worst case running time: O(n) loops otherwise."""
        if not self.is_empty():
            if self.head.data == item:
                if self.head is self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                return  # Return once node is deleted.
            else:
                node = self.head
                while node.next is not None:
                    if node.next.data == item:
                        if node.next is self.tail:
                            self.tail = node
                        node.next = node.next.next
                        return  # Return once node is deleted.
                    node = node.next

        raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
