from linkedlist import LinkedList

def find_max(linked_list):
    print("--------------------------")
    print("Finding the maximum value of:\n{0}".format(linked_list.stringify_list()))
    if linked_list.head_node is None:
        return None
    current_node = linked_list.head_node
    max_value = current_node.value
    while current_node is not None:
        if current_node.value > max_value:
            max_value = current_node.value
        current_node = current_node.next_node
    return max_value

ll = LinkedList(6)
ll.insert_beginning(32)
ll.insert_beginning(-12)
ll.insert_beginning(48)
ll.insert_beginning(2)
ll.insert_beginning(1)
print("The maximum value in this linked list is {0}\n".format(find_max(ll)))
ll_2 = LinkedList(60)
ll_2.insert_beginning(12)
ll_2.insert_beginning(22)
ll_2.insert_beginning(-10)
print("The maximum value in this linked list is {0}\n".format(find_max(ll_2)))
ll_3 = LinkedList("A")
ll_3.insert_beginning("X")
ll_3.insert_beginning("V")
ll_3.insert_beginning("L")
ll_3.insert_beginning("D")
ll_3.insert_beginning("Q")
print("The maximum value in this linked list is {0}\n".format(find_max(ll_3)))
#Runtime
runtime = "N"
print("The runtime of find_max is O({0})".format(runtime))