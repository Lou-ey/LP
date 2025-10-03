from Node import Node

class Stack:
    def __init__(self):
        self.top_item = None

    def peek(self):
        return self.top_item.get_value() if self.top_item else None