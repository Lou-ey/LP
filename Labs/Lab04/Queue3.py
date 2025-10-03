from Node import Node

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def peek(self):
        is_empty = self.is_empty()
        if is_empty:
            return 'Nothing to see here'
        return self.head.get_value() if self.head else None

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size is None:
            return True
        elif self.max_size > self.get_size:
            return True
        return False

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print(f'Adding {item_to_add.get_value()} to the queue!')
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print('Sorry, no more room!')