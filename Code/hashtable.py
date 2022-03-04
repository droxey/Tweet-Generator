#!python
import random
from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = []
        for i in range(init_size):
            self.buckets.append(LinkedList())

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = []
        for key, val in self.items():
            items.append('{!r}: {!r}'.format(key, val))
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # (1) Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]

        # FIXME: THIS CODE IS ALWAYS WRONG (DO NOT ITERATE OVER BUCKETS if you know the key)
        # for bucket in self.buckets:
        #     ...

        # (2) Attempt to find key-value entry in bucket (if it exists)
        # (2a) Define inner function (closure that caputures local key variable)
        def matches_key(entry):
            # if entry[0] == key:
            #     return True
            # else:
            #     return False
            return entry[0] == key
        # Use matching function as callback for find_if_matches
        entry = bucket.find_if_matches(matches_key)

        # (2b) Alternative: Define matching function inline as a lambda (anonymous function)
        entry = bucket.find_if_matches(lambda entry: entry[0] == key)
        # entry = bucket.find_if_matches(lambda k, v: k == key)  # lambda argument tuple unpacking

        # (3) If found, return value associated with given key
        if entry is not None:
            value = entry[1]
            return value
        # (3) Otherwise, raise error to tell user get failed
        else:
            raise KeyError('Key not found: {}'.format(key))

        # END OF GOOD SOLUTIONS (requires LinkedList::find_if_matches function)

        # (2c) Equivalent non-compartmentalized code if LinkedList::find_if_matches doesn't exist
        entry = None
        node = bucket.head
        # Loop over nodes in this bucket (linked list)
        while node is not None:
            entry = node.data
            # Check if key-value entry matches the key we're looking for
            if entry[0] == key:
                value = entry[1]
                return value
            # Otherwise, move to the next node in the linked list
            else:
                node = node.next
        # Could not find entry associated with given key (after while loop completes)
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # index = ...
        # bucket = ...

        # TODO: Check if key-value entry exists in bucket
        # entry = bucket.find_if_matches(...)

        # TODO: If found, update value associated with given key
        # bucket.delete(entry)
        # new_entry = (key, value)
        # bucket.append(new_entry)

        # Alternative if you implemented LinkedList::update(old, new) stretch challenge
        # bucket.replace(entry, new_entry)

        # TODO: Otherwise, insert given key-value entry into bucket
        # entry = (key, value)
        # bucket.append(entry)

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
