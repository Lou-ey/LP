from Node import Node

class LinkedList:
    def __init__(self, value=None):
        self.value = value
        if value is not None:
            self.head = Node(value)

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head)
        self.head = new_node

    def stringify_list(self):
        stringified_list = ""
        current_node = self.head
        while current_node:
            stringified_list += f"{current_node.get_value()} --> "
            current_node = current_node.get_next_node()
        stringified_list += "None"
        return stringified_list

    def get_head_node(self):
        return self.head

    def remove_first_instance_node(self, value_to_remove):
        current_node = self.head
        while current_node:
            next_node = current_node.get_next_node()

            if current_node and current_node.get_value() == value_to_remove:
                self.head = current_node.get_next_node() # change head to the next node
                current_node = None
            elif next_node and next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())
                next_node = None
            current_node = next_node

    def remove_all_instances_nodes(self, value_to_remove):
        current_node = self.head
        if current_node and current_node.get_value() == value_to_remove:
            self.head = current_node.get_next_node()
            current_node = None
        while current_node:
            next_node = current_node.get_next_node()
            if next_node and next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())
                next_node = None
            current_node = next_node

    def swap_nodes(self, val1, val2):
        if val1 == val2:
            return

        node1 = node2 = None
        node1_prev = node2_prev = None
        current_node = self.head

        while current_node and current_node.get_value() != val1:
            node1_prev = current_node
            current_node = current_node.get_next_node()
        node1 = current_node

        current_node = self.head
        while current_node and current_node.get_value() != val2:
            node2_prev = current_node
            current_node = current_node.get_next_node()
        node2 = current_node

        if not node1 or not node2:
            print("One or both values not found, no swap possible.")
            return

        if node1_prev:
            node1_prev.set_next_node(node2)
        else:
            self.head = node2

        if node2_prev:
            node2_prev.set_next_node(node1)
        else:
            self.head = node1

        temp = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp)

def nth_last_node(linked_list, n):
    nth_last_pointer = None
    tail_pointer = linked_list.get_head_node()
    count = 0

    while tail_pointer:
        count += 1

        if count >= n:
            if nth_last_pointer is None:
                nth_last_pointer = linked_list.get_head_node()
            else:
                nth_last_pointer = nth_last_pointer.get_next_node()

        tail_pointer = tail_pointer.get_next_node()

    return nth_last_pointer

def middle_node(linked_list):
    fast_pointer = linked_list.get_head_node()
    slow_one = linked_list.get_head_node()

    while fast_pointer is not None:
        fast_pointer = fast_pointer.get_next_node()
        if fast_pointer != slow_one and fast_pointer is not None:
            fast_pointer = fast_pointer.get_next_node()
            slow_one = slow_one.get_next_node()
    return slow_one

