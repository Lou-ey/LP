from Node import Node

class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("All out of space!")

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove
            return item_to_remove.get_value() if item_to_remove else None
        else:
            print("Stack is empty")
        self.size -= 1
        return None

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value() if self.top_item else None
        else:
            print("Stack is empty")
        return None

    def has_space(self):
        if self.limit > self.size:
            return True
        return False

    def is_empty(self):
        if self.size == 0:
            return True
        return False

pizza_stack = Stack(6)
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")
pizza_stack.push("pizza #7")
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()