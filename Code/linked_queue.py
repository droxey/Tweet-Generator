from linkedlist import LinkedList


class LinkedQueue(object):
    """Queue implementation using our Linked List class."""

    def __init__(self, items=None):
        self.items = LinkedList(items)

    def __str__(self):
        """Return a formatted string representation of this queue."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'LinkedQueue({!r})'.format(self.items())

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items.head is not None:
            item = self.items.head.data
            self.items.head = self.items.head.next
            return item

    def items(self):
        return self.items.items()


if __name__ == "__main__":
    queue = LinkedQueue(['one', 'two', 'three'])

    print('Enqueue "four"')
    queue.enqueue('four')
    print(queue.items())

    print('Dequeue')
    print(queue.dequeue())
    print(queue.items())
