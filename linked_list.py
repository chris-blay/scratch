#!/usr/bin/python3

import unittest


class _Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self):
        # Start with a dummy head so iteration is more straightforward.
        self.head = _Node()

    def __len__(self):
        '''return length of list.'''
        count = 0
        current = self.head
        while current.next:
            count += 1
            current = current.next
        return count

    def append(self, value):
        '''append value to end.'''
        current = self.head
        while current.next:
            current = current.next
        current.next = _Node(value, current.next)
        

    def appendfront(self, value):
        '''append value to front.'''
        current = self.head
        while True:
            current.next = _Node(value, current.next)
            break

    def clear(self):
        '''remove all values.'''
        if self.head.next != None:
            self.head.next = self.head.next.next
            clear(self)

    def count(self, value):
        '''return number of occurrences of value.'''
        current = self.head
        count = 0
        while current.next:
            if current.next.value == value:
                count += 1
                current = current.next
            else:
                current = current.next
        return count

    def index(self, value):
        '''
        return first index of value.
        Raises ValueError if the value is not present.
        '''
        current = self.head
        count = 0
        while current.next:
            if current.next.value == value:
                return count
            else: 
                current = current.next
                count += 1
        raise ValueError('Could not find %r in list' % value)

    def pop(self):
        '''remove and return last item.'''
        current = self.head
        if current.next == None:
            return None
        while current.next.next:
            current = current.next
        popped = current.next.value
        current.next = current.next.next
        return popped

    def popfront(self):
        '''remove and return first item.'''
        current = self.head
        if current.next == None:
            return None
        popped = current.next.value
        current.next = current.next.next
        return popped

    def remove(self, value):
        '''
        remove first occurrence of value.
        Raises ValueError if the value is not present.
        '''
        current = self.head
        if current.next == None:
            raise ValueError('List is empty, brah.')
        while current.next.next:
            if current.next.value == value:
                current.next = current.next.next
                break
            else:
                current = current.next
            raise ValueError('%r not in here, son!' % value)

    def getindex(self, index):
        current = self.head
        count = 0
        while count != index:
            if current.next == None:
                raise IndexError('List not that long.')
            else:
                count += 1
                current = current.next
        return current.next.value



class LinkedListTestCase(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList()

    def test_length_empty(self):
        self.assertEqual(0, len(self.list))

    def test_index_while_empty(self):
        self.assertRaises(ValueError, lambda: self.list.index(42))

    def test_remove_while_empty(self):
        self.assertRaises(ValueError, lambda: self.list.remove(42))

    def test_count_while_empty(self):
        self.assertEqual(0, self.list.count(42))

    def test_length(self):
        self.list.append(42)
        self.assertEqual(1, len(self.list))

    def test_index(self):
        self.list.append(42)
        self.assertEqual(0, self.list.index(42))

    def test_remove(self):
        self.list.append(42)
        self.list.remove(42)

    def test_count(self):
        self.list.append(42)
        self.assertEqual(1, self.list.count(42))

    # TODO: Add more test cases as needed.


if __name__ == '__main__':
    unittest.main()

